from typing import Any

import proto

__protobuf__: Any

class GetAdGroupFeedRequest(proto.Message):
    resource_name: Any

class MutateAdGroupFeedsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class AdGroupFeedOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAdGroupFeedsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateAdGroupFeedResult(proto.Message):
    resource_name: Any
    ad_group_feed: Any
