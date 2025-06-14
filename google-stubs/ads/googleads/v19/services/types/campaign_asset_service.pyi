import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import campaign_asset as gagr_campaign_asset
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignAssetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignAssetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign_asset.CampaignAsset
    update: gagr_campaign_asset.CampaignAsset
    remove: str

class MutateCampaignAssetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignAssetResult']

class MutateCampaignAssetResult(proto.Message):
    resource_name: str
    campaign_asset: gagr_campaign_asset.CampaignAsset
