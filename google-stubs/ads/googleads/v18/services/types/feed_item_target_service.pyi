import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import feed_item_target as gagr_feed_item_target
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateFeedItemTargetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['FeedItemTargetOperation']
    partial_failure: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType
    validate_only: bool

class FeedItemTargetOperation(proto.Message):
    create: gagr_feed_item_target.FeedItemTarget
    remove: str

class MutateFeedItemTargetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateFeedItemTargetResult']

class MutateFeedItemTargetResult(proto.Message):
    resource_name: str
    feed_item_target: gagr_feed_item_target.FeedItemTarget
