# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FineTuningJobEvent(BaseModel):
    """
    Fine-tuning job event object
    """ # noqa: E501
    id: StrictStr
    created_at: StrictInt
    level: StrictStr
    message: StrictStr
    object: StrictStr
    __properties: ClassVar[List[str]] = ["id", "created_at", "level", "message", "object"]

    @field_validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('info', 'warn', 'error',):
            raise ValueError("must be one of enum values ('info', 'warn', 'error')")
        return value

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('fine_tuning.job.event',):
            raise ValueError("must be one of enum values ('fine_tuning.job.event')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FineTuningJobEvent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FineTuningJobEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "level": obj.get("level"),
            "message": obj.get("../message"),
            "object": obj.get("object")
        })
        return _obj


