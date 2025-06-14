import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign_bid_modifier as gagr_campaign_bid_modifier
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignBidModifiersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignBidModifierOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignBidModifierOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign_bid_modifier.CampaignBidModifier
    update: gagr_campaign_bid_modifier.CampaignBidModifier
    remove: str

class MutateCampaignBidModifiersResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignBidModifierResult']

class MutateCampaignBidModifierResult(proto.Message):
    resource_name: str
    campaign_bid_modifier: gagr_campaign_bid_modifier.CampaignBidModifier
