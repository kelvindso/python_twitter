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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr
from twitter.models import RulesRequestSummary
from pydantic import ValidationError

class RulesResponseMetadata(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    next_token: Optional[constr(strict=True, min_length=1)] = Field(None, description="The next token.")
    result_count: Optional[StrictInt] = Field(None, description="Number of Rules in result set.")
    sent: StrictStr = ...
    summary: Optional[RulesRequestSummary] = None

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
    def from_json(cls, json_str: str) -> RulesResponseMetadata:
        """Create an instance of RulesResponseMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RulesResponseMetadata:
        """Create an instance of RulesResponseMetadata from a dict"""
        if type(obj) is not dict:
            return RulesResponseMetadata.parse_obj(obj)

        return RulesResponseMetadata.parse_obj({
            "next_token": obj.get("next_token"),
            "result_count": obj.get("result_count"),
            "sent": obj.get("sent"),
            "summary": RulesRequestSummary.from_dict(obj.get("summary"))
        })


