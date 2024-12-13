# coding: utf-8

from typing import ClassVar, Tuple, Union

from fastapi.responses import StreamingResponse  # noqa: F401

from openapi_server.models.create_chat_completion.create_chat_completion_request import CreateChatCompletionRequest
from openapi_server.models.create_chat_completion.create_chat_completion_response import CreateChatCompletionResponse
from openapi_server.models.create_chat_completion.create_chat_completion_stream_response import CreateChatCompletionStreamResponse


class BaseChatApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseChatApi.subclasses = BaseChatApi.subclasses + (cls,)
    async def create_chat_completion(
        self,
        create_chat_completion_request: CreateChatCompletionRequest,
    ) -> Union[CreateChatCompletionResponse,str]:
        ...
