from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.resources.types import (
    keyword_plan_campaign_keyword as keyword_plan_campaign_keyword,
)

__protobuf__: Any

class GetKeywordPlanCampaignKeywordRequest(proto.Message):
    resource_name: Any

class MutateKeywordPlanCampaignKeywordsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class KeywordPlanCampaignKeywordOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateKeywordPlanCampaignKeywordsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateKeywordPlanCampaignKeywordResult(proto.Message):
    resource_name: Any
