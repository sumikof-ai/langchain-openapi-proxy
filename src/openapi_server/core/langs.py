import json
from logging import getLogger
from typing import List

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from openapi_server.models.create_chat_completion.create_chat_completion_request import (
    CreateChatCompletionRequest,
)

logger = getLogger(__name__)

# メッセージを送信する非同期関数
async def send_message(messages):
    print(f"send_message => {messages}")
    prompt = ChatPromptTemplate(messages=messages,template_format='jinja2')
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        base_url="http://localhost:8080/v1",
        max_completion_tokens=2048,
        logprobs=False,
        n=1,
        top_p=1,
        presence_penalty=0,
        temperature=1,
    )
    llm
    chain = prompt | llm
    res = chain.astream({"code": messages})
    async for msg in res:
        yield msg.content


def make_choice(delta):
    return {
        "index": 0,
        "logprobs": None,
        "delta": delta,
        "finish_reason": None,
    }


def make_prompt_message(messages: List):
    def make_prompt(message):
        dic = {"system": "system", "user": "human", "assistant": "ai"}
        jsonobj = message.to_dict()
        role = dic[jsonobj["role"]]
        return (role, jsonobj["content"])

    return [make_prompt(message) for message in messages]


async def chat_streaming(
    create_chat_completion_request: CreateChatCompletionRequest, response_base
):
    response_base["choices"] = [
        make_choice({"role": "assistant", "content": "", "refusal": None})
    ]
    response_str = f"data: {json.dumps(response_base)}\n\n"
    logger.debug(response_str)
    yield response_str

    prompt_message = make_prompt_message(create_chat_completion_request.messages)
    async for chunk in send_message(prompt_message):
        response_base["choices"] = [make_choice({"content": chunk})]
        response_str = f"data: {json.dumps(response_base)}\n\n"
        logger.debug(response_str)
        yield response_str

    yield "data: [DONE]\n"
