from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.common.types import policy as policy

__protobuf__: Any

class GetAdRequest(proto.Message):
    resource_name: Any

class MutateAdsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    response_content_type: Any
    validate_only: Any

class AdOperation(proto.Message):
    update_mask: Any
    policy_validation_parameter: Any
    update: Any

class MutateAdsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdResult(proto.Message):
    resource_name: Any
    ad: Any
