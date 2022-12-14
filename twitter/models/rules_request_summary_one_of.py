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



from pydantic import BaseModel, Field, StrictInt

from pydantic import ValidationError

class RulesRequestSummaryOneOf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created: StrictInt = Field(..., description="Number of user-specified stream filtering rules that were created.")
    invalid: StrictInt = Field(..., description="Number of invalid user-specified stream filtering rules.")
    not_created: StrictInt = Field(..., description="Number of user-specified stream filtering rules that were not created.")
    valid: StrictInt = Field(..., description="Number of valid user-specified stream filtering rules.")

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
    def from_json(cls, json_str: str) -> RulesRequestSummaryOneOf:
        """Create an instance of RulesRequestSummaryOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RulesRequestSummaryOneOf:
        """Create an instance of RulesRequestSummaryOneOf from a dict"""
        if type(obj) is not dict:
            return RulesRequestSummaryOneOf.parse_obj(obj)

        return RulesRequestSummaryOneOf.parse_obj({
            "created": obj.get("created"),
            "invalid": obj.get("invalid"),
            "not_created": obj.get("not_created"),
            "valid": obj.get("valid")
        })


