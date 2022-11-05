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



from pydantic import BaseModel
from twitter.models import TweetComplianceSchema
from pydantic import ValidationError

class TweetUndropComplianceSchema(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    undrop: TweetComplianceSchema = ...

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
    def from_json(cls, json_str: str) -> TweetUndropComplianceSchema:
        """Create an instance of TweetUndropComplianceSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of undrop
        if self.undrop:
            _dict['undrop'] = self.undrop.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TweetUndropComplianceSchema:
        """Create an instance of TweetUndropComplianceSchema from a dict"""
        if type(obj) is not dict:
            return TweetUndropComplianceSchema.parse_obj(obj)

        return TweetUndropComplianceSchema.parse_obj({
            "undrop": TweetComplianceSchema.from_dict(obj.get("undrop"))
        })


