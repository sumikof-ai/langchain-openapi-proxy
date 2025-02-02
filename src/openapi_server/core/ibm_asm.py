import os
import re
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from graphviz import Digraph

# ==== 設定 ====
LLM = OpenAI(model="text-davinci-003", temperature=0)  # OpenAIのLLMを利用

# ==== アセンブラコードの解析関数 ====
def parse_assembler_code(file_path):
    """アセンブラコードを解析し、命令ごとの説明を生成する"""
    with open(file_path, 'r') as file:
        code_lines = file.readlines()

    parsed_code = []
    for line in code_lines:
        if line.strip() and not line.startswith(";"):  # コメントを除外
            parsed_code.append(line.strip())

    return parsed_code

# ==== JCLの解析関数 ====
def parse_jcl(file_path):
    """JCLを解析して、データセットや実行条件を抽出"""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    datasets = {}
    exec_params = {}
    for line in lines:
        line = line.strip()
        if line.startswith("//") and "DD" in line:  # データセット定義
            parts = re.split(r'\s+', line)
            dd_name = parts[0].replace("//", "")
            dataset = parts[2].split("=")[1] if "DSN=" in parts[2] else "UNKNOWN"
            datasets[dd_name] = dataset
        elif line.startswith("//") and "EXEC" in line:  # 実行パラメータ
            match = re.search(r'PARM=\'(.*?)\'', line)
            if match:
                exec_params["PARM"] = match.group(1)

    return {"datasets": datasets, "exec_params": exec_params}

# ==== フローチャート生成 ====
def generate_flowchart(assembler_lines, output_file="flowchart"):
    """アセンブラコードの処理フローをフローチャートで可視化"""
    dot = Digraph(format="png")
    dot.attr(rankdir='TB')

    for i, line in enumerate(assembler_lines):
        dot.node(str(i), line)

        if i > 0:  # 前のノードと接続
            dot.edge(str(i - 1), str(i))

    output_path = dot.render(output_file)
    return output_path

# ==== ドキュメント生成 ====
def generate_documentation(assembler_file, jcl_file):
    """アセンブラコードとJCLを解析し、ドキュメントを生成"""
    # アセンブラコード解析
    assembler_lines = parse_assembler_code(assembler_file)

    # JCL解析
    jcl_data = parse_jcl(jcl_file)

    # LLMによる命令の説明生成
    prompt_template = """
    以下のアセンブラコードの処理内容を説明してください:
    {code}
    """
    prompt = PromptTemplate(input_variables=["code"], template=prompt_template)
    llm_chain = LLMChain(llm=LLM, prompt=prompt)

    explanations = []
    for line in assembler_lines:
        explanation = llm_chain.run({"code": line})
        explanations.append(f"{line} ; {explanation}")

    # フローチャート生成
    flowchart_path = generate_flowchart(assembler_lines)

    # ドキュメント出力
    documentation = {
        "Assembler Code": "\n".join(explanations),
        "JCL Info": jcl_data,
        "Flowchart": flowchart_path,
    }

    return documentation




def analyze_module_dependencies(module_files):
    """
    複数モジュール間の依存関係を解析する。
    - モジュール内のCALL命令やラベルを解析して依存関係を特定する。
    :param module_files: モジュールファイルのリスト
    :return: 依存関係の辞書形式
    """
    dependencies = {}
    label_to_module = {}

    # ラベルを事前に収集
    for module in module_files:
        with open(module, 'r') as file:
            lines = file.readlines()
            for line in lines:
                match = re.match(r'^(\w+):', line)  # ラベルを検出
                if match:
                    label = match.group(1)
                    label_to_module[label] = module

    # 各モジュールの依存関係を解析
    for module in module_files:
        dependencies[module] = []
        with open(module, 'r') as file:
            lines = file.readlines()
            for line in lines:
                match = re.search(r'CALL\s+(\w+)', line)  # CALL命令を検出
                if match:
                    called_label = match.group(1)
                    if called_label in label_to_module:
                        dependencies[module].append(label_to_module[called_label])

    return dependencies

def generate_advanced_flowchart(assembler_files, dependencies, output_file="advanced_flowchart"):
    """
    高度なフローチャートを生成する。
    - 複数モジュール間の依存関係や条件分岐を考慮する。
    :param assembler_files: アセンブラファイルのリスト
    :param dependencies: モジュール間の依存関係辞書
    :param output_file: 出力ファイル名
    :return: フローチャート画像のパス
    """
    dot = Digraph(format="png")
    dot.attr(rankdir='TB')

    # 各モジュールをノードとして追加
    for module in assembler_files:
        dot.node(module, label=f"Module: {os.path.basename(module)}", shape="box")

    # モジュール間の依存関係をエッジとして追加
    for module, dependent_modules in dependencies.items():
        for dep_module in dependent_modules:
            dot.edge(module, dep_module)

    # 各モジュール内の処理を可視化
    for module in assembler_files:
        with open(module, 'r') as file:
            lines = file.readlines()
            prev_node = None
            for i, line in enumerate(lines):
                node_id = f"{module}_{i}"
                dot.node(node_id, line.strip(), shape="ellipse")

                # 条件分岐やループの処理
                if "BE" in line or "BNE" in line:
                    condition = line.strip()
                    dot.node(f"{node_id}_cond", label=f"Condition: {condition}", shape="diamond")
                    dot.edge(prev_node, f"{node_id}_cond")
                else:
                    if prev_node:
                        dot.edge(prev_node, node_id)
                prev_node = node_id

    output_path = dot.render(output_file)
    return output_path

#
#{
#    "datasets": {
#        "INFILE": "INPUT.DATASET",
#        "OUTFILE": "OUTPUT.DATASET"
#    },
#    "exec_params": {
#        "PARM": "MODE=TEST"
#    }
#}
# ==== 実行例 ====
if __name__ == "__main__":
    assembler_files = ["module1.asm", "module2.asm", "module3.asm"]  # アセンブラモジュールのリスト
    jcl_file = "example.jcl"  # JCLコードのパス

    # モジュール間の依存関係を解析
    dependencies = analyze_module_dependencies(assembler_files)

    # 高度なフローチャートを生成
    flowchart_path = generate_advanced_flowchart(assembler_files, dependencies)

    # 各モジュールのドキュメント化
    for assembler_file in assembler_files:
        doc = generate_documentation(assembler_file, jcl_file)

        print(f"=== {os.path.basename(assembler_file)} の解析結果 ===")
        print(doc["Assembler Code"])
        print("\n=== JCL情報 ===")
        print(doc["JCL Info"])

    print("\n=== 高度なフローチャート ===")
    print(f"フローチャートは {flowchart_path} に保存されました。")

