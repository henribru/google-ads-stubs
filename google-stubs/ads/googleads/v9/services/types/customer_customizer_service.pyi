from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateCustomerCustomizersRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CustomerCustomizerOperation(proto.Message):
    create: Any
    remove: Any

class MutateCustomerCustomizersResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateCustomerCustomizerResult(proto.Message):
    resource_name: Any
    customer_customizer: Any
