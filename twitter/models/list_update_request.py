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


from typing import Optional
from pydantic import BaseModel, StrictBool, constr

from pydantic import ValidationError

class ListUpdateRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    description: Optional[constr(strict=True, max_length=100, min_length=0)] = None
    name: Optional[constr(strict=True, max_length=25, min_length=1)] = None
    private: Optional[StrictBool] = None

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
    def from_json(cls, json_str: str) -> ListUpdateRequest:
        """Create an instance of ListUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListUpdateRequest:
        """Create an instance of ListUpdateRequest from a dict"""
        if type(obj) is not dict:
            return ListUpdateRequest.parse_obj(obj)

        return ListUpdateRequest.parse_obj({
            "description": obj.get("description"),
            "name": obj.get("name"),
            "private": obj.get("private")
        })

