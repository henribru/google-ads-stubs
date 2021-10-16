from typing import Any

import proto

__protobuf__: Any

class GetLabelRequest(proto.Message):
    resource_name: Any

class MutateLabelsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class LabelOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateLabelsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateLabelResult(proto.Message):
    resource_name: Any
    label: Any