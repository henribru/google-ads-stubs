import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.common.types import policy as policy

__protobuf__: Incomplete

class MutateAdGroupAdsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class AdGroupAdOperation(proto.Message):
    update_mask: Incomplete
    policy_validation_parameter: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAdGroupAdsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdGroupAdResult(proto.Message):
    resource_name: Incomplete
    ad_group_ad: Incomplete
