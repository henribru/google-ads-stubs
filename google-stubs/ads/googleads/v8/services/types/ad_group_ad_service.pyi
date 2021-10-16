from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v8.common.types import policy as policy

__protobuf__: Any

class GetAdGroupAdRequest(proto.Message):
    resource_name: Any

class MutateAdGroupAdsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdGroupAdOperation(proto.Message):
    update_mask: Any
    policy_validation_parameter: Any
    create: Any
    update: Any
    remove: Any

class MutateAdGroupAdsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupAdResult(proto.Message):
    resource_name: Any
    ad_group_ad: Any
