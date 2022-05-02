import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateAdParametersRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class AdParameterOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAdParametersResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateAdParameterResult(proto.Message):
    resource_name: Incomplete
    ad_parameter: Incomplete
