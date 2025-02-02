# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401



from pydantic import BaseModel, ValidationError, field_validator
from openapi_server.models.chat_completion.chat_completion_request_assistant_message import ChatCompletionRequestAssistantMessage
from openapi_server.models.chat_completion.chat_completion_request_function_message import ChatCompletionRequestFunctionMessage
from openapi_server.models.chat_completion.chat_completion_request_system_message import ChatCompletionRequestSystemMessage
from openapi_server.models.chat_completion.chat_completion_request_tool_message import ChatCompletionRequestToolMessage
from openapi_server.models.chat_completion.chat_completion_request_user_message import ChatCompletionRequestUserMessage
from typing import Union, List, Optional, Dict
from typing_extensions import Literal
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self
from logging import getLogger
logger = getLogger(__name__)
CHATCOMPLETIONREQUESTMESSAGE_ONE_OF_SCHEMAS = ["ChatCompletionRequestAssistantMessage", "ChatCompletionRequestFunctionMessage", "ChatCompletionRequestSystemMessage", "ChatCompletionRequestToolMessage", "ChatCompletionRequestUserMessage"]

class ChatCompletionRequestMessage(BaseModel):
    """
    ChatCompletionRequestMessage
    """
    # data type: ChatCompletionRequestSystemMessage
    oneof_schema_1_validator: Optional[ChatCompletionRequestSystemMessage] = None
    # data type: ChatCompletionRequestUserMessage
    oneof_schema_2_validator: Optional[ChatCompletionRequestUserMessage] = None
    # data type: ChatCompletionRequestAssistantMessage
    oneof_schema_3_validator: Optional[ChatCompletionRequestAssistantMessage] = None
    # data type: ChatCompletionRequestToolMessage
    oneof_schema_4_validator: Optional[ChatCompletionRequestToolMessage] = None
    # data type: ChatCompletionRequestFunctionMessage
    oneof_schema_5_validator: Optional[ChatCompletionRequestFunctionMessage] = None
    actual_instance: Optional[Union[ChatCompletionRequestAssistantMessage, ChatCompletionRequestFunctionMessage, ChatCompletionRequestSystemMessage, ChatCompletionRequestToolMessage, ChatCompletionRequestUserMessage]] = None
    one_of_schemas: List[str] = Literal["ChatCompletionRequestAssistantMessage", "ChatCompletionRequestFunctionMessage", "ChatCompletionRequestSystemMessage", "ChatCompletionRequestToolMessage", "ChatCompletionRequestUserMessage"]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)
            tempinstance = self.from_dict(kwargs)
            logger.debug(tempinstance.to_dict())
            self.actual_instance = tempinstance.actual_instance

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ChatCompletionRequestMessage.model_construct()
        error_messages = []
        match = 0
        # print('actual_instance_must_validate_oneof')
        # validate data type: ChatCompletionRequestSystemMessage
        if not isinstance(v, ChatCompletionRequestSystemMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChatCompletionRequestSystemMessage`")
        else:
            # print('ChatCompletionRequestSystemMessageだよ')
            match += 1
        # validate data type: ChatCompletionRequestUserMessage
        if not isinstance(v, ChatCompletionRequestUserMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChatCompletionRequestUserMessage`")
        else:
            # print('ChatCompletionRequestUserMessageだよ')
            match += 1
        # validate data type: ChatCompletionRequestAssistantMessage
        if not isinstance(v, ChatCompletionRequestAssistantMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChatCompletionRequestAssistantMessage`")
        else:
            match += 1
        # validate data type: ChatCompletionRequestToolMessage
        if not isinstance(v, ChatCompletionRequestToolMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChatCompletionRequestToolMessage`")
        else:
            match += 1
        # validate data type: ChatCompletionRequestFunctionMessage
        if not isinstance(v, ChatCompletionRequestFunctionMessage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ChatCompletionRequestFunctionMessage`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ChatCompletionRequestMessage with oneOf schemas: ChatCompletionRequestAssistantMessage, ChatCompletionRequestFunctionMessage, ChatCompletionRequestSystemMessage, ChatCompletionRequestToolMessage, ChatCompletionRequestUserMessage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ChatCompletionRequestMessage with oneOf schemas: ChatCompletionRequestAssistantMessage, ChatCompletionRequestFunctionMessage, ChatCompletionRequestSystemMessage, ChatCompletionRequestToolMessage, ChatCompletionRequestUserMessage. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ChatCompletionRequestSystemMessage
        try:
            instance.actual_instance = ChatCompletionRequestSystemMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChatCompletionRequestUserMessage
        try:
            instance.actual_instance = ChatCompletionRequestUserMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChatCompletionRequestAssistantMessage
        try:
            instance.actual_instance = ChatCompletionRequestAssistantMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChatCompletionRequestToolMessage
        try:
            instance.actual_instance = ChatCompletionRequestToolMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ChatCompletionRequestFunctionMessage
        try:
            instance.actual_instance = ChatCompletionRequestFunctionMessage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ChatCompletionRequestMessage with oneOf schemas: ChatCompletionRequestAssistantMessage, ChatCompletionRequestFunctionMessage, ChatCompletionRequestSystemMessage, ChatCompletionRequestToolMessage, ChatCompletionRequestUserMessage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ChatCompletionRequestMessage with oneOf schemas: ChatCompletionRequestAssistantMessage, ChatCompletionRequestFunctionMessage, ChatCompletionRequestSystemMessage, ChatCompletionRequestToolMessage, ChatCompletionRequestUserMessage. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


