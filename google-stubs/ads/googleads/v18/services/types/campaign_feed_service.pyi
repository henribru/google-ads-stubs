import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign_feed as gagr_campaign_feed
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignFeedsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignFeedOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignFeedOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign_feed.CampaignFeed
    update: gagr_campaign_feed.CampaignFeed
    remove: str

class MutateCampaignFeedsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignFeedResult']

class MutateCampaignFeedResult(proto.Message):
    resource_name: str
    campaign_feed: gagr_campaign_feed.CampaignFeed
