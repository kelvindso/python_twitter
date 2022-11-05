# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints  # noqa: E501

    The version of the OpenAPI document: 2.49
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, conint

from pydantic import ValidationError

class CashtagEntity(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    end: conint(strict=True, ge=0) = Field(..., description="Index (zero-based) at which position this entity ends.  The index is exclusive.")
    start: conint(strict=True, ge=0) = Field(..., description="Index (zero-based) at which position this entity starts.  The index is inclusive.")
    tag: StrictStr = ...

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.to_dict())

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CashtagEntity:
        """Create an instance of CashtagEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CashtagEntity:
        """Create an instance of CashtagEntity from a dict"""
        if type(obj) is not dict:
            return CashtagEntity.parse_obj(obj)

        return CashtagEntity.parse_obj({
            "end": obj.get("end"),
            "start": obj.get("start"),
            "tag": obj.get("tag")
        })


