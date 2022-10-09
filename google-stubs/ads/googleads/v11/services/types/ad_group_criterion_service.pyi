import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.common.types import policy as policy

__protobuf__: Incomplete

class MutateAdGroupCriteriaRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class AdGroupCriterionOperation(proto.Message):
    update_mask: Incomplete
    exempt_policy_violation_keys: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAdGroupCriteriaResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdGroupCriterionResult(proto.Message):
    resource_name: Incomplete
    ad_group_criterion: Incomplete
