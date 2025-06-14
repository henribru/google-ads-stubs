import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import keyword_plan_campaign_keyword
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateKeywordPlanCampaignKeywordsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['KeywordPlanCampaignKeywordOperation']
    partial_failure: bool
    validate_only: bool

class KeywordPlanCampaignKeywordOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: keyword_plan_campaign_keyword.KeywordPlanCampaignKeyword
    update: keyword_plan_campaign_keyword.KeywordPlanCampaignKeyword
    remove: str

class MutateKeywordPlanCampaignKeywordsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateKeywordPlanCampaignKeywordResult']

class MutateKeywordPlanCampaignKeywordResult(proto.Message):
    resource_name: str
