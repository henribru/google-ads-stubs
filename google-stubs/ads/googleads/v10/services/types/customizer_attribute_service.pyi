import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCustomizerAttributesRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class CustomizerAttributeOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    remove: Incomplete

class MutateCustomizerAttributesResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateCustomizerAttributeResult(proto.Message):
    resource_name: Incomplete
    customizer_attribute: Incomplete
