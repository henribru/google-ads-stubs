from typing import Any

import proto

__protobuf__: Any

class GetSharedCriterionRequest(proto.Message):
    resource_name: Any

class MutateSharedCriteriaRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class SharedCriterionOperation(proto.Message):
    create: Any
    remove: Any

class MutateSharedCriteriaResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateSharedCriterionResult(proto.Message):
    resource_name: Any
    shared_criterion: Any
