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


from typing import List, Literal, Optional
from pydantic import BaseModel, Field, conint, constr

from pydantic import ValidationError

class TweetCreateRequestPoll(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    duration_minutes: conint(strict=True, le=10080, ge=5) = Field(..., description="Duration of the poll in minutes.")
    options: List[constr(strict=True, max_length=25, min_length=1)] = ...
    reply_settings: Optional[Literal['following', 'mentionedUsers']] = Field(None, description="Settings to indicate who can reply to the Tweet.")

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
    def from_json(cls, json_str: str) -> TweetCreateRequestPoll:
        """Create an instance of TweetCreateRequestPoll from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TweetCreateRequestPoll:
        """Create an instance of TweetCreateRequestPoll from a dict"""
        if type(obj) is not dict:
            return TweetCreateRequestPoll.parse_obj(obj)

        return TweetCreateRequestPoll.parse_obj({
            "duration_minutes": obj.get("duration_minutes"),
            "options": obj.get("options"),
            "reply_settings": obj.get("reply_settings")
        })


