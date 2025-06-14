import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import feed_item_set
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateFeedItemSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['FeedItemSetOperation']
    partial_failure: bool
    validate_only: bool

class FeedItemSetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: feed_item_set.FeedItemSet
    update: feed_item_set.FeedItemSet
    remove: str

class MutateFeedItemSetsResponse(proto.Message):
    results: MutableSequence['MutateFeedItemSetResult']
    partial_failure_error: status_pb2.Status

class MutateFeedItemSetResult(proto.Message):
    resource_name: str
