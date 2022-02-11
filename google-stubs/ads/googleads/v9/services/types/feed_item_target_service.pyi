from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetFeedItemTargetRequest(proto.Message):
    resource_name: Any

class MutateFeedItemTargetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    response_content_type: Any
    validate_only: Any

class FeedItemTargetOperation(proto.Message):
    create: Any
    remove: Any

class MutateFeedItemTargetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateFeedItemTargetResult(proto.Message):
    resource_name: Any
    feed_item_target: Any
