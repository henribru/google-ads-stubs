from typing import Any

import proto

from google.ads.googleads.v7.resources.types import campaign_asset as campaign_asset

__protobuf__: Any

class GetCampaignAssetRequest(proto.Message):
    resource_name: Any

class MutateCampaignAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class CampaignAssetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCampaignAssetsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignAssetResult(proto.Message):
    resource_name: Any
