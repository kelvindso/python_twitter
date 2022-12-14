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
from twitter.models import CashtagEntity, FullTextEntitiesAnnotationsInner, HashtagEntity, MentionEntity, UrlEntity
from pydantic import ValidationError

class FullTextEntities(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    annotations: Optional[List[FullTextEntitiesAnnotationsInner]] = None
    cashtags: Optional[List[CashtagEntity]] = None
    hashtags: Optional[List[HashtagEntity]] = None
    mentions: Optional[List[MentionEntity]] = None
    urls: Optional[List[UrlEntity]] = None

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
    def from_json(cls, json_str: str) -> FullTextEntities:
        """Create an instance of FullTextEntities from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in annotations (list)
        _items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['annotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cashtags (list)
        _items = []
        if self.cashtags:
            for _item in self.cashtags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cashtags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hashtags (list)
        _items = []
        if self.hashtags:
            for _item in self.hashtags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['hashtags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mentions (list)
        _items = []
        if self.mentions:
            for _item in self.mentions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mentions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in urls (list)
        _items = []
        if self.urls:
            for _item in self.urls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['urls'] = _items

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FullTextEntities:
        """Create an instance of FullTextEntities from a dict"""
        if type(obj) is not dict:
            return FullTextEntities.parse_obj(obj)

        return FullTextEntities.parse_obj({
            "annotations": [FullTextEntitiesAnnotationsInner.from_dict(_item) for _item in obj.get("annotations")],
            "cashtags": [CashtagEntity.from_dict(_item) for _item in obj.get("cashtags")],
            "hashtags": [HashtagEntity.from_dict(_item) for _item in obj.get("hashtags")],
            "mentions": [MentionEntity.from_dict(_item) for _item in obj.get("mentions")],
            "urls": [UrlEntity.from_dict(_item) for _item in obj.get("urls")]
        })


