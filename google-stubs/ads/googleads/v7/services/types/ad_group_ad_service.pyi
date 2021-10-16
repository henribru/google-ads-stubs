from typing import Any

import proto

__protobuf__: Any

class GetAdGroupAdRequest(proto.Message):
    resource_name: Any

class MutateAdGroupAdsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdGroupAdOperation(proto.Message):
    update_mask: Any
    policy_validation_parameter: Any
    create: Any
    update: Any
    remove: Any

class MutateAdGroupAdsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupAdResult(proto.Message):
    resource_name: Any
    ad_group_ad: Any
