import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.common.types import policy as policy

__protobuf__: Incomplete

class GetAdRequest(proto.Message):
    resource_name: Incomplete

class MutateAdsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    response_content_type: Incomplete
    validate_only: Incomplete

class AdOperation(proto.Message):
    update_mask: Incomplete
    policy_validation_parameter: Incomplete
    update: Incomplete

class MutateAdsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdResult(proto.Message):
    resource_name: Incomplete
    ad: Incomplete
