from logging import getLogger
from typing import Union

from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from openapi_server.apis.chat_api_base import BaseChatApi
from openapi_server.core import langs
from openapi_server.models.create_chat_completion.create_chat_completion_request import (
    CreateChatCompletionRequest,
)
from openapi_server.models.create_chat_completion.create_chat_completion_response import (
    CreateChatCompletionResponse,
)

logger = getLogger(__name__)

class StreamResponseRecord(BaseModel): ...


class ChatApiImpl(BaseChatApi):
    async def create_chat_completion(
        self,
        create_chat_completion_request: CreateChatCompletionRequest,
    ) -> Union[CreateChatCompletionResponse, str]:
        logger.warning(f"request body => {create_chat_completion_request.to_json()}")
        response_base = {
            "id": "123",
            "created": 123,
            "model": create_chat_completion_request.model,
            "object": "chat.completion",
        }
        if create_chat_completion_request.stream:
            response_base["object"] = "chat.completion.chunk"
            # You can add the logic here to manipulate the stream_response before returning it
            return StreamingResponse(
                langs.chat_streaming(create_chat_completion_request, response_base),
                media_type="text/event-stream",
            )
        else:
            response_base["choices"] = [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "こんにちわにゃー",
                        "refusal": None,
                    },
                    "logprobs": None,
                }
            ]
            return CreateChatCompletionResponse(**response_base)
