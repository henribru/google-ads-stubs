import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import keyword_plan_campaign
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateKeywordPlanCampaignsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['KeywordPlanCampaignOperation']
    partial_failure: bool
    validate_only: bool

class KeywordPlanCampaignOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: keyword_plan_campaign.KeywordPlanCampaign
    update: keyword_plan_campaign.KeywordPlanCampaign
    remove: str

class MutateKeywordPlanCampaignsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateKeywordPlanCampaignResult']

class MutateKeywordPlanCampaignResult(proto.Message):
    resource_name: str
