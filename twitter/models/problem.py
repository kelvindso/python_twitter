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
import twitter.models


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr

from pydantic import ValidationError

class Problem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    detail: Optional[StrictStr] = None
    status: Optional[StrictInt] = None
    title: StrictStr = ...
    type: StrictStr = ...

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = 'type'

    # discriminator mappings
    __discriminator_value_class_map = {
        'ClientDisconnectedProblem': 'ClientDisconnectedProblem',
        'ClientForbiddenProblem': 'ClientForbiddenProblem',
        'ConflictProblem': 'ConflictProblem',
        'ConnectionExceptionProblem': 'ConnectionExceptionProblem',
        'DisallowedResourceProblem': 'DisallowedResourceProblem',
        'DuplicateRuleProblem': 'DuplicateRuleProblem',
        'FieldUnauthorizedProblem': 'FieldUnauthorizedProblem',
        'GenericProblem': 'GenericProblem',
        'InvalidRequestProblem': 'InvalidRequestProblem',
        'InvalidRuleProblem': 'InvalidRuleProblem',
        'NonCompliantRulesProblem': 'NonCompliantRulesProblem',
        'OperationalDisconnectProblem': 'OperationalDisconnectProblem',
        'ResourceNotFoundProblem': 'ResourceNotFoundProblem',
        'ResourceUnauthorizedProblem': 'ResourceUnauthorizedProblem',
        'ResourceUnavailableProblem': 'ResourceUnavailableProblem',
        'RulesCapProblem': 'RulesCapProblem',
        'UnsupportedAuthenticationProblem': 'UnsupportedAuthenticationProblem',
        'UsageCapExceededProblem': 'UsageCapExceededProblem'
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.to_dict())

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Union(ClientDisconnectedProblem, ClientForbiddenProblem, ConflictProblem, ConnectionExceptionProblem, DisallowedResourceProblem, DuplicateRuleProblem, FieldUnauthorizedProblem, GenericProblem, InvalidRequestProblem, InvalidRuleProblem, NonCompliantRulesProblem, OperationalDisconnectProblem, ResourceNotFoundProblem, ResourceUnauthorizedProblem, ResourceUnavailableProblem, RulesCapProblem, UnsupportedAuthenticationProblem, UsageCapExceededProblem, Problem):
        """Create an instance of Problem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Union(ClientDisconnectedProblem, ClientForbiddenProblem, ConflictProblem, ConnectionExceptionProblem, DisallowedResourceProblem, DuplicateRuleProblem, FieldUnauthorizedProblem, GenericProblem, InvalidRequestProblem, InvalidRuleProblem, NonCompliantRulesProblem, OperationalDisconnectProblem, ResourceNotFoundProblem, ResourceUnauthorizedProblem, ResourceUnavailableProblem, RulesCapProblem, UnsupportedAuthenticationProblem, UsageCapExceededProblem, Problem):
        """Create an instance of Problem from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(twitter.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError("Problem failed to lookup discriminator value from " +
                             json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                             ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


