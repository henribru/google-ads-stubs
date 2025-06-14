import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import asset_set_asset as gagr_asset_set_asset
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetSetAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetSetAssetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AssetSetAssetOperation(proto.Message):
    create: gagr_asset_set_asset.AssetSetAsset
    remove: str

class MutateAssetSetAssetsResponse(proto.Message):
    results: MutableSequence['MutateAssetSetAssetResult']
    partial_failure_error: status_pb2.Status

class MutateAssetSetAssetResult(proto.Message):
    resource_name: str
    asset_set_asset: gagr_asset_set_asset.AssetSetAsset
