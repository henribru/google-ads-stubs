from typing import Any

import proto

__protobuf__: Any

class GetCustomerFeedRequest(proto.Message):
    resource_name: Any

class MutateCustomerFeedsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CustomerFeedOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCustomerFeedsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCustomerFeedResult(proto.Message):
    resource_name: Any
    customer_feed: Any
