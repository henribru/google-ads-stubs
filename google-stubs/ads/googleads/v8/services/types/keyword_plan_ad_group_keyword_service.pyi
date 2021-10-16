from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.resources.types import (
    keyword_plan_ad_group_keyword as keyword_plan_ad_group_keyword,
)

__protobuf__: Any

class GetKeywordPlanAdGroupKeywordRequest(proto.Message):
    resource_name: Any

class MutateKeywordPlanAdGroupKeywordsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class KeywordPlanAdGroupKeywordOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateKeywordPlanAdGroupKeywordsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateKeywordPlanAdGroupKeywordResult(proto.Message):
    resource_name: Any
