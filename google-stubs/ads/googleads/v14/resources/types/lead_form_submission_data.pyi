from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.lead_form_field_user_input_type import (
    LeadFormFieldUserInputTypeEnum,
)

_M = TypeVar("_M")

class CustomLeadFormSubmissionField(proto.Message):
    question_text: str
    field_value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        question_text: str = ...,
        field_value: str = ...
    ) -> None: ...

class LeadFormSubmissionData(proto.Message):
    resource_name: str
    id: str
    asset: str
    campaign: str
    lead_form_submission_fields: MutableSequence[LeadFormSubmissionField]
    custom_lead_form_submission_fields: MutableSequence[CustomLeadFormSubmissionField]
    ad_group: str
    ad_group_ad: str
    gclid: str
    submission_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: str = ...,
        asset: str = ...,
        campaign: str = ...,
        lead_form_submission_fields: MutableSequence[LeadFormSubmissionField] = ...,
        custom_lead_form_submission_fields: MutableSequence[
            CustomLeadFormSubmissionField
        ] = ...,
        ad_group: str = ...,
        ad_group_ad: str = ...,
        gclid: str = ...,
        submission_date_time: str = ...
    ) -> None: ...

class LeadFormSubmissionField(proto.Message):
    field_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    field_value: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        field_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType = ...,
        field_value: str = ...
    ) -> None: ...
