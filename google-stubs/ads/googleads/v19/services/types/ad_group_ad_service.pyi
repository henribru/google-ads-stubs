import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import policy
from google.ads.googleads.v19.enums.types import asset_field_type as gage_asset_field_type, response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import ad_group_ad as gagr_ad_group_ad
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdGroupAdsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdGroupAdOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdGroupAdOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    policy_validation_parameter: policy.PolicyValidationParameter
    create: gagr_ad_group_ad.AdGroupAd
    update: gagr_ad_group_ad.AdGroupAd
    remove: str

class MutateAdGroupAdsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdGroupAdResult']

class MutateAdGroupAdResult(proto.Message):
    resource_name: str
    ad_group_ad: gagr_ad_group_ad.AdGroupAd

class RemoveAutomaticallyCreatedAssetsRequest(proto.Message):
    ad_group_ad: str
    assets_with_field_type: MutableSequence['AssetsWithFieldType']

class AssetsWithFieldType(proto.Message):
    asset: str
    asset_field_type: gage_asset_field_type.AssetFieldTypeEnum.AssetFieldType
