import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign as gagr_campaign
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign.Campaign
    update: gagr_campaign.Campaign
    remove: str

class MutateCampaignsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignResult']

class MutateCampaignResult(proto.Message):
    resource_name: str
    campaign: gagr_campaign.Campaign
