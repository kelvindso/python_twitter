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
from pydantic import BaseModel, Field, StrictStr
from twitter.models import Variant
from pydantic import ValidationError

class AnimatedGifAllOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    preview_image_url: Optional[StrictStr] = None
    variants: Optional[List[Variant]] = Field(None, description="An array of all available variants of the media.")

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
    def from_json(cls, json_str: str) -> AnimatedGifAllOf:
        """Create an instance of AnimatedGifAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in variants (list)
        _items = []
        if self.variants:
            for _item in self.variants:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variants'] = _items

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AnimatedGifAllOf:
        """Create an instance of AnimatedGifAllOf from a dict"""
        if type(obj) is not dict:
            return AnimatedGifAllOf.parse_obj(obj)

        return AnimatedGifAllOf.parse_obj({
            "preview_image_url": obj.get("preview_image_url"),
            "variants": [Variant.from_dict(_item) for _item in obj.get("variants")]
        })


