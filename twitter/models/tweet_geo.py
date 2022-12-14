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
from pydantic import BaseModel, Field, StrictStr
from twitter.models import Point
from pydantic import ValidationError

class TweetGeo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    coordinates: Optional[Point] = None
    place_id: Optional[StrictStr] = Field(None, description="The identifier for this place.")

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
    def from_json(cls, json_str: str) -> TweetGeo:
        """Create an instance of TweetGeo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of coordinates
        if self.coordinates:
            _dict['coordinates'] = self.coordinates.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TweetGeo:
        """Create an instance of TweetGeo from a dict"""
        if type(obj) is not dict:
            return TweetGeo.parse_obj(obj)

        return TweetGeo.parse_obj({
            "coordinates": Point.from_dict(obj.get("coordinates")),
            "place_id": obj.get("place_id")
        })


