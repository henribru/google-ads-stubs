import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import asset_set as gagr_asset_set
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AssetSetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_asset_set.AssetSet
    update: gagr_asset_set.AssetSet
    remove: str

class MutateAssetSetsResponse(proto.Message):
    results: MutableSequence['MutateAssetSetResult']
    partial_failure_error: status_pb2.Status

class MutateAssetSetResult(proto.Message):
    resource_name: str
    asset_set: gagr_asset_set.AssetSet
