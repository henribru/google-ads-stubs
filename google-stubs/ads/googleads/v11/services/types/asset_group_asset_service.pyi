import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import (
    asset_group_asset as asset_group_asset,
)

__protobuf__: Incomplete

class MutateAssetGroupAssetsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class AssetGroupAssetOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateAssetGroupAssetsResponse(proto.Message):
    results: Incomplete
    partial_failure_error: Incomplete

class MutateAssetGroupAssetResult(proto.Message):
    resource_name: Incomplete
