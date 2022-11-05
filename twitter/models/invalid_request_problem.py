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
from twitter.models import InvalidRequestProblemAllOfErrors, Problem
from pydantic import ValidationError

class InvalidRequestProblem(Problem):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    errors: Optional[List[InvalidRequestProblemAllOfErrors]] = None

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
    def from_json(cls, json_str: str) -> InvalidRequestProblem:
        """Create an instance of InvalidRequestProblem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvalidRequestProblem:
        """Create an instance of InvalidRequestProblem from a dict"""
        if type(obj) is not dict:
            return InvalidRequestProblem.parse_obj(obj)

        return InvalidRequestProblem.parse_obj({
            "detail": obj.get("detail"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "errors": [InvalidRequestProblemAllOfErrors.from_dict(_item) for _item in obj.get("errors")]
        })


