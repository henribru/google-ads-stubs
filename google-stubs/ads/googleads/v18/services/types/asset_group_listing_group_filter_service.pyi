import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import asset_group_listing_group_filter as gagr_asset_group_listing_group_filter
from google.protobuf import field_mask_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetGroupListingGroupFiltersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetGroupListingGroupFilterOperation']
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AssetGroupListingGroupFilterOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_asset_group_listing_group_filter.AssetGroupListingGroupFilter
    update: gagr_asset_group_listing_group_filter.AssetGroupListingGroupFilter
    remove: str

class MutateAssetGroupListingGroupFiltersResponse(proto.Message):
    results: MutableSequence['MutateAssetGroupListingGroupFilterResult']

class MutateAssetGroupListingGroupFilterResult(proto.Message):
    resource_name: str
    asset_group_listing_group_filter: gagr_asset_group_listing_group_filter.AssetGroupListingGroupFilter
