from typing import Any

import proto
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class MutateCampaignAssetSetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class CampaignAssetSetOperation(proto.Message):
    create: Any
    remove: Any

class MutateCampaignAssetSetsResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateCampaignAssetSetResult(proto.Message):
    resource_name: Any
    campaign_asset_set: Any
