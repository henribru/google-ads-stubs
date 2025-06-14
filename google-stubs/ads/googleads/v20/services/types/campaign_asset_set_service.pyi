import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import campaign_asset_set as gagr_campaign_asset_set
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignAssetSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignAssetSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignAssetSetOperation(proto.Message):
    create: gagr_campaign_asset_set.CampaignAssetSet
    remove: str

class MutateCampaignAssetSetsResponse(proto.Message):
    results: MutableSequence['MutateCampaignAssetSetResult']
    partial_failure_error: status_pb2.Status

class MutateCampaignAssetSetResult(proto.Message):
    resource_name: str
    campaign_asset_set: gagr_campaign_asset_set.CampaignAssetSet
