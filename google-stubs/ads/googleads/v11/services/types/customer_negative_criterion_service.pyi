import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCustomerNegativeCriteriaRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CustomerNegativeCriterionOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCustomerNegativeCriteriaResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateCustomerNegativeCriteriaResult(proto.Message):
    resource_name: Incomplete
    customer_negative_criterion: Incomplete