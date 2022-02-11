from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetCustomerNegativeCriterionRequest(proto.Message):
    resource_name: Any

class MutateCustomerNegativeCriteriaRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CustomerNegativeCriterionOperation(proto.Message):
    create: Any
    remove: Any

class MutateCustomerNegativeCriteriaResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCustomerNegativeCriteriaResult(proto.Message):
    resource_name: Any
    customer_negative_criterion: Any
