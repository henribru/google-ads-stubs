import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    lead_form_field_user_input_type as lead_form_field_user_input_type,
)

__protobuf__: Incomplete

class LeadFormSubmissionData(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    asset: Incomplete
    campaign: Incomplete
    lead_form_submission_fields: Incomplete
    ad_group: Incomplete
    ad_group_ad: Incomplete
    gclid: Incomplete
    submission_date_time: Incomplete

class LeadFormSubmissionField(proto.Message):
    field_type: Incomplete
    field_value: Incomplete
