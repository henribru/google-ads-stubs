import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import (
    feed_item_set_link as feed_item_set_link,
)

__protobuf__: Incomplete

class MutateFeedItemSetLinksRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class FeedItemSetLinkOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateFeedItemSetLinksResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateFeedItemSetLinkResult(proto.Message):
    resource_name: Incomplete
