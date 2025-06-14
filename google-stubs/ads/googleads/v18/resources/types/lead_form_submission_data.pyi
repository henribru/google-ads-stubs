from google.ads.googleads.v18.enums.types.lead_form_field_user_input_type import LeadFormFieldUserInputTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomLeadFormSubmissionField(proto.Message):
    question_text: str
    field_value: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., question_text: str = ..., field_value: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["question_text", "field_value"]) -> bool: ...
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
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., id: str = ..., asset: str = ..., campaign: str = ..., lead_form_submission_fields: MutableSequence[LeadFormSubmissionField] = ..., custom_lead_form_submission_fields: MutableSequence[CustomLeadFormSubmissionField] = ..., ad_group: str = ..., ad_group_ad: str = ..., gclid: str = ..., submission_date_time: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "asset", "campaign", "lead_form_submission_fields", "custom_lead_form_submission_fields", "ad_group", "ad_group_ad", "gclid", "submission_date_time"]) -> bool: ...
class LeadFormSubmissionField(proto.Message):
    field_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    field_value: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., field_type: LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType = ..., field_value: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["field_type", "field_value"]) -> bool: ...
