from typing import Any

import proto

__protobuf__: Any

class GetAdParameterRequest(proto.Message):
    resource_name: Any

class MutateAdParametersRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdParameterOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAdParametersResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdParameterResult(proto.Message):
    resource_name: Any
    ad_parameter: Any
