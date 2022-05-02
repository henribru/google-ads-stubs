import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v10.resources.types import feed_item_set as feed_item_set

__protobuf__: Incomplete

class MutateFeedItemSetsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class FeedItemSetOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateFeedItemSetsResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateFeedItemSetResult(proto.Message):
    resource_name: Incomplete
