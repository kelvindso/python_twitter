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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr

from pydantic import ValidationError

class List(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    follower_count: Optional[StrictInt] = None
    id: constr(strict=True, regex=r'/^[0-9]{1,19}$/') = Field(..., description="The unique identifier of this List.")
    member_count: Optional[StrictInt] = None
    name: StrictStr = Field(..., description="The name of this List.")
    owner_id: Optional[constr(strict=True, regex=r'/^[0-9]{1,19}$/')] = Field(None, description="Unique identifier of this User. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
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
    def from_json(cls, json_str: str) -> List:
        """Create an instance of List from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> List:
        """Create an instance of List from a dict"""
        if type(obj) is not dict:
            return List.parse_obj(obj)

        return List.parse_obj({
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "follower_count": obj.get("follower_count"),
            "id": obj.get("id"),
            "member_count": obj.get("member_count"),
            "name": obj.get("name"),
            "owner_id": obj.get("owner_id"),
            "private": obj.get("private")
        })


