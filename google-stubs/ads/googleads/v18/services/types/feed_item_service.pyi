import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import feed_item as gagr_feed_item
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateFeedItemsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['FeedItemOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class FeedItemOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_feed_item.FeedItem
    update: gagr_feed_item.FeedItem
    remove: str

class MutateFeedItemsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateFeedItemResult']

class MutateFeedItemResult(proto.Message):
    resource_name: str
    feed_item: gagr_feed_item.FeedItem
