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


from typing import List, Optional
from pydantic import BaseModel, Field
from twitter.models import Expansions, FilteredStreamingTweetResponseMatchingRulesInner, Problem, Tweet
from pydantic import ValidationError

class FilteredStreamingTweetResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    data: Optional[Tweet] = None
    errors: Optional[List[Problem]] = None
    includes: Optional[Expansions] = None
    matching_rules: Optional[List[FilteredStreamingTweetResponseMatchingRulesInner]] = Field(None, description="The list of rules which matched the Tweet")

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
    def from_json(cls, json_str: str) -> FilteredStreamingTweetResponse:
        """Create an instance of FilteredStreamingTweetResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of includes
        if self.includes:
            _dict['includes'] = self.includes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in matching_rules (list)
        _items = []
        if self.matching_rules:
            for _item in self.matching_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matching_rules'] = _items

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FilteredStreamingTweetResponse:
        """Create an instance of FilteredStreamingTweetResponse from a dict"""
        if type(obj) is not dict:
            return FilteredStreamingTweetResponse.parse_obj(obj)

        return FilteredStreamingTweetResponse.parse_obj({
            "data": Tweet.from_dict(obj.get("data")),
            "errors": [Problem.from_dict(_item) for _item in obj.get("errors")],
            "includes": Expansions.from_dict(obj.get("includes")),
            "matching_rules": [FilteredStreamingTweetResponseMatchingRulesInner.from_dict(_item) for _item in obj.get("matching_rules")]
        })

