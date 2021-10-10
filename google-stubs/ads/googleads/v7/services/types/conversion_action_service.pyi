from typing import Any

import proto

__protobuf__: Any

class GetConversionActionRequest(proto.Message):
    resource_name: Any

class MutateConversionActionsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class ConversionActionOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateConversionActionsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateConversionActionResult(proto.Message):
    resource_name: Any
    conversion_action: Any
