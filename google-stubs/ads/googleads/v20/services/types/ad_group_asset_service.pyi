import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import ad_group_asset as gagr_ad_group_asset
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupAssetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupAssetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_ad_group_asset.AdGroupAsset
    update: gagr_ad_group_asset.AdGroupAsset
    remove: str

class MutateAdGroupAssetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupAssetResult']

class MutateAdGroupAssetResult(proto.Message):
    resource_name: str
    ad_group_asset: gagr_ad_group_asset.AdGroupAsset
