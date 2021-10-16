from typing import Any

import proto

__protobuf__: Any

class GetAdGroupCriterionRequest(proto.Message):
    resource_name: Any

class MutateAdGroupCriteriaRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdGroupCriterionOperation(proto.Message):
    update_mask: Any
    exempt_policy_violation_keys: Any
    create: Any
    update: Any
    remove: Any

class MutateAdGroupCriteriaResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupCriterionResult(proto.Message):
    resource_name: Any
    ad_group_criterion: Any
