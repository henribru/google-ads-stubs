import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import asset as gagr_asset
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetOperation']
    partial_failure: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType
    validate_only: bool

class AssetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_asset.Asset
    update: gagr_asset.Asset

class MutateAssetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAssetResult']

class MutateAssetResult(proto.Message):
    resource_name: str
    asset: gagr_asset.Asset
