import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import asset_group_asset
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetGroupAssetOperation']
    partial_failure: bool
    validate_only: bool

class AssetGroupAssetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: asset_group_asset.AssetGroupAsset
    update: asset_group_asset.AssetGroupAsset
    remove: str

class MutateAssetGroupAssetsResponse(proto.Message):
    results: MutableSequence['MutateAssetGroupAssetResult']
    partial_failure_error: status_pb2.Status

class MutateAssetGroupAssetResult(proto.Message):
    resource_name: str
