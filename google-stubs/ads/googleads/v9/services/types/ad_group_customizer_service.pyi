from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateAdGroupCustomizersRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdGroupCustomizerOperation(proto.Message):
    create: Any
    remove: Any

class MutateAdGroupCustomizersResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateAdGroupCustomizerResult(proto.Message):
    resource_name: Any
    ad_group_customizer: Any
