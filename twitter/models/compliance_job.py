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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr
from twitter.models import ComplianceJobStatus, ComplianceJobType
from pydantic import ValidationError

class ComplianceJob(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created_at: datetime = Field(..., description="Creation time of the compliance job.")
    download_expires_at: datetime = Field(..., description="Expiration time of the download URL.")
    download_url: StrictStr = Field(..., description="URL from which the user will retrieve their compliance results.")
    id: constr(strict=True, regex=r'/^[0-9]{1,19}$/') = Field(..., description="Compliance Job ID.")
    name: Optional[constr(strict=True, max_length=64)] = Field(None, description="User-provided name for a compliance job.")
    status: ComplianceJobStatus = ...
    type: ComplianceJobType = ...
    upload_expires_at: datetime = Field(..., description="Expiration time of the upload URL.")
    upload_url: StrictStr = Field(..., description="URL to which the user will upload their Tweet or user IDs.")

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
    def from_json(cls, json_str: str) -> ComplianceJob:
        """Create an instance of ComplianceJob from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ComplianceJob:
        """Create an instance of ComplianceJob from a dict"""
        if type(obj) is not dict:
            return ComplianceJob.parse_obj(obj)

        return ComplianceJob.parse_obj({
            "created_at": obj.get("created_at"),
            "download_expires_at": obj.get("download_expires_at"),
            "download_url": obj.get("download_url"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": ComplianceJobStatus.from_dict(obj.get("status")),
            "type": ComplianceJobType.from_dict(obj.get("type")),
            "upload_expires_at": obj.get("upload_expires_at"),
            "upload_url": obj.get("upload_url")
        })


