from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.resources.types import (
    keyword_plan_ad_group as keyword_plan_ad_group,
)

__protobuf__: Any

class GetKeywordPlanAdGroupRequest(proto.Message):
    resource_name: Any

class MutateKeywordPlanAdGroupsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class KeywordPlanAdGroupOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateKeywordPlanAdGroupsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateKeywordPlanAdGroupResult(proto.Message):
    resource_name: Any
