import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import feed as gagr_feed
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['FeedOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class FeedOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_feed.Feed
    update: gagr_feed.Feed
    remove: str

class MutateFeedsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateFeedResult']

class MutateFeedResult(proto.Message):
    resource_name: str
    feed: gagr_feed.Feed
