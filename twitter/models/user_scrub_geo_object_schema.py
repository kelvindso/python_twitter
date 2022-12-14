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

from pydantic import BaseModel, Field, constr
from twitter.models import UserComplianceSchemaUser
from pydantic import ValidationError

class UserScrubGeoObjectSchema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    event_at: datetime = Field(..., description="Event time.")
    up_to_tweet_id: constr(strict=True, regex=r'/^[0-9]{1,19}$/') = Field(..., description="Unique identifier of this Tweet. This is returned as a string in order to avoid complications with languages and tools that cannot handle large integers.")
    user: UserComplianceSchemaUser = ...

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
    def from_json(cls, json_str: str) -> UserScrubGeoObjectSchema:
        """Create an instance of UserScrubGeoObjectSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserScrubGeoObjectSchema:
        """Create an instance of UserScrubGeoObjectSchema from a dict"""
        if type(obj) is not dict:
            return UserScrubGeoObjectSchema.parse_obj(obj)

        return UserScrubGeoObjectSchema.parse_obj({
            "event_at": obj.get("event_at"),
            "up_to_tweet_id": obj.get("up_to_tweet_id"),
            "user": UserComplianceSchemaUser.from_dict(obj.get("user"))
        })


