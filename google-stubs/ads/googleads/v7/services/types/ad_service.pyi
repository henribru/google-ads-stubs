from typing import Any

import proto

__protobuf__: Any

class GetAdRequest(proto.Message):
    resource_name: Any

class MutateAdsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    response_content_type: Any
    validate_only: Any

class AdOperation(proto.Message):
    update_mask: Any
    policy_validation_parameter: Any
    update: Any

class MutateAdsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdResult(proto.Message):
    resource_name: Any
    ad: Any
