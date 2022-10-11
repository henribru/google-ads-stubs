import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateAdGroupCriterionCustomizersRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class AdGroupCriterionCustomizerOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateAdGroupCriterionCustomizersResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateAdGroupCriterionCustomizerResult(proto.Message):
    resource_name: Incomplete
    ad_group_criterion_customizer: Incomplete