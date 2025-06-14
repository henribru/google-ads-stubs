import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import ad_group_feed as gagr_ad_group_feed
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupFeedOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupFeedOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_ad_group_feed.AdGroupFeed
    update: gagr_ad_group_feed.AdGroupFeed
    remove: str

class MutateAdGroupFeedsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupFeedResult']

class MutateAdGroupFeedResult(proto.Message):
    resource_name: str
    ad_group_feed: gagr_ad_group_feed.AdGroupFeed
