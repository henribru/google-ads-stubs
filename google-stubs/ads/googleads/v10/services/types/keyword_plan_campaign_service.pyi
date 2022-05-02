import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.resources.types import (
    keyword_plan_campaign as keyword_plan_campaign,
)

__protobuf__: Incomplete

class MutateKeywordPlanCampaignsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class KeywordPlanCampaignOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateKeywordPlanCampaignsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateKeywordPlanCampaignResult(proto.Message):
    resource_name: Incomplete
