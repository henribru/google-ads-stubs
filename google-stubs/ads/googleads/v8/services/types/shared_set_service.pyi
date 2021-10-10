from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetSharedSetRequest(proto.Message):
    resource_name: Any

class MutateSharedSetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class SharedSetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateSharedSetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateSharedSetResult(proto.Message):
    resource_name: Any
    shared_set: Any
