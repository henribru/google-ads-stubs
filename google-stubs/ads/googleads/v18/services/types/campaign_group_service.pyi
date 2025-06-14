import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign_group as gagr_campaign_group
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignGroupOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignGroupOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign_group.CampaignGroup
    update: gagr_campaign_group.CampaignGroup
    remove: str

class MutateCampaignGroupsResponse(proto.Message):
    results: MutableSequence['MutateCampaignGroupResult']
    partial_failure_error: status_pb2.Status

class MutateCampaignGroupResult(proto.Message):
    resource_name: str
    campaign_group: gagr_campaign_group.CampaignGroup
