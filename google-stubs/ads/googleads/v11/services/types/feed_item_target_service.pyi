import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateFeedItemTargetsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    response_content_type: Incomplete
    validate_only: Incomplete

class FeedItemTargetOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateFeedItemTargetsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateFeedItemTargetResult(proto.Message):
    resource_name: Incomplete
    feed_item_target: Incomplete
