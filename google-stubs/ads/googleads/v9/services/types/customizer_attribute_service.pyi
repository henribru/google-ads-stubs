from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateCustomizerAttributesRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CustomizerAttributeOperation(proto.Message):
    update_mask: Any
    create: Any
    remove: Any

class MutateCustomizerAttributesResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateCustomizerAttributeResult(proto.Message):
    resource_name: Any
    customizer_attribute: Any
