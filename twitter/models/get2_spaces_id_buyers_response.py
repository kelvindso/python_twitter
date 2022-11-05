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
from pydantic import BaseModel
from twitter.models import Expansions, Get2ListsIdFollowersResponseMeta, Problem, User
from pydantic import ValidationError

class Get2SpacesIdBuyersResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    data: Optional[List[User]] = None
    errors: Optional[List[Problem]] = None
    includes: Optional[Expansions] = None
    meta: Optional[Get2ListsIdFollowersResponseMeta] = None

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
    def from_json(cls, json_str: str) -> Get2SpacesIdBuyersResponse:
        """Create an instance of Get2SpacesIdBuyersResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item in self.data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['data'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Get2SpacesIdBuyersResponse:
        """Create an instance of Get2SpacesIdBuyersResponse from a dict"""
        if type(obj) is not dict:
            return Get2SpacesIdBuyersResponse.parse_obj(obj)

        return Get2SpacesIdBuyersResponse.parse_obj({
            "data": [User.from_dict(_item) for _item in obj.get("data")],
            "errors": [Problem.from_dict(_item) for _item in obj.get("errors")],
            "includes": Expansions.from_dict(obj.get("includes")),
            "meta": Get2ListsIdFollowersResponseMeta.from_dict(obj.get("meta"))
        })


