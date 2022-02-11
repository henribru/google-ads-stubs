from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v9.resources.types import (
    asset_group_asset as asset_group_asset,
)

__protobuf__: Any

class GetAssetGroupAssetRequest(proto.Message):
    resource_name: Any

class MutateAssetGroupAssetsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class AssetGroupAssetOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateAssetGroupAssetsResponse(proto.Message):
    results: Any
    partial_failure_error: Any

class MutateAssetGroupAssetResult(proto.Message):
    resource_name: Any
