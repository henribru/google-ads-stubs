import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import lead_form_field_user_input_type
from typing import MutableSequence

__protobuf__: Incomplete

class LeadFormSubmissionData(proto.Message):
    resource_name: str
    id: str
    asset: str
    campaign: str
    lead_form_submission_fields: MutableSequence['LeadFormSubmissionField']
    custom_lead_form_submission_fields: MutableSequence['CustomLeadFormSubmissionField']
    ad_group: str
    ad_group_ad: str
    gclid: str
    submission_date_time: str

class LeadFormSubmissionField(proto.Message):
    field_type: lead_form_field_user_input_type.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    field_value: str

class CustomLeadFormSubmissionField(proto.Message):
    question_text: str
    field_value: str
