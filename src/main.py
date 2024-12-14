# coding: utf-8

from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import JSONResponse
import uvicorn

from fastapi import FastAPI, Request, Response, status

# from openapi_server.apis.assistants_api import router as AssistantsApiRouter
# from openapi_server.apis.audio_api import router as AudioApiRouter
# from openapi_server.apis.audit_logs_api import router as AuditLogsApiRouter
from openapi_server.apis.batch_api import router as BatchApiRouter
from openapi_server.apis.chat_api import router as ChatApiRouter
from openapi_server.apis.completions_api import router as CompletionsApiRouter
from openapi_server.apis.embeddings_api import router as EmbeddingsApiRouter
from openapi_server.apis.files_api import router as FilesApiRouter
from openapi_server.apis.fine_tuning_api import router as FineTuningApiRouter
from openapi_server.apis.images_api import router as ImagesApiRouter
from openapi_server.apis.invites_api import router as InvitesApiRouter
from openapi_server.apis.models_api import router as ModelsApiRouter
from openapi_server.apis.moderations_api import router as ModerationsApiRouter
from openapi_server.apis.projects_api import router as ProjectsApiRouter
from openapi_server.apis.uploads_api import router as UploadsApiRouter
from openapi_server.apis.users_api import router as UsersApiRouter
from openapi_server.apis.vector_stores_api import router as VectorStoresApiRouter

app = FastAPI(
    title="OpenAI API",
    description="The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.",
    version="2.3.0",
    root_path="/v1",
)


@app.exception_handler(RequestValidationError)
async def request_exceptionhandler(request: Request, exc: RequestValidationError):
    print(await request.json())
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.exception_handler(ResponseValidationError)
async def response_exception_handler(response: Response, exc: ResponseValidationError):
    print(await response.json())
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# app.include_router(AssistantsApiRouter)
# app.include_router(AudioApiRouter)
# app.include_router(AuditLogsApiRouter)
app.include_router(BatchApiRouter)
app.include_router(ChatApiRouter)
app.include_router(CompletionsApiRouter)
app.include_router(EmbeddingsApiRouter)
app.include_router(FilesApiRouter)
app.include_router(FineTuningApiRouter)
app.include_router(ImagesApiRouter)
app.include_router(InvitesApiRouter)
app.include_router(ModelsApiRouter)
app.include_router(ModerationsApiRouter)
app.include_router(ProjectsApiRouter)
app.include_router(UploadsApiRouter)
app.include_router(UsersApiRouter)
app.include_router(VectorStoresApiRouter)

if __name__ == "__main__":
    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="[%X]",
    )
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
