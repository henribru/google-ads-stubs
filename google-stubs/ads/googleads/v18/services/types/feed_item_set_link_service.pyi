import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import feed_item_set_link
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateFeedItemSetLinksRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['FeedItemSetLinkOperation']
    partial_failure: bool
    validate_only: bool

class FeedItemSetLinkOperation(proto.Message):
    create: feed_item_set_link.FeedItemSetLink
    remove: str

class MutateFeedItemSetLinksResponse(proto.Message):
    results: MutableSequence['MutateFeedItemSetLinkResult']
    partial_failure_error: status_pb2.Status

class MutateFeedItemSetLinkResult(proto.Message):
    resource_name: str
