from typing import Any

import proto

from google.ads.googleads.v10.enums.types.lead_form_field_user_input_type import (
    LeadFormFieldUserInputTypeEnum,
)

class LeadFormSubmissionData(proto.Message):
    resource_name: str
    id: str
    asset: str
    campaign: str
    lead_form_submission_fields: list[LeadFormSubmissionField]
    ad_group: str
    ad_group_ad: str
    gclid: str
    submission_date_time: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: str = ...,
        asset: str = ...,
        campaign: str = ...,
        lead_form_submission_fields: list[LeadFormSubmissionField] = ...,
        ad_group: str = ...,
        ad_group_ad: str = ...,
        gclid: str = ...,
        submission_date_time: str = ...
    ) -> None: ...

class LeadFormSubmissionField(proto.Message):
    field_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    field_value: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        field_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType = ...,
        field_value: str = ...
    ) -> None: ...
