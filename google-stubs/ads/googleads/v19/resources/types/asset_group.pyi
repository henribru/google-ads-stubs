import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import ad_strength as gage_ad_strength, ad_strength_action_item_type, asset_coverage_video_aspect_ratio_requirement, asset_field_type as gage_asset_field_type, asset_group_primary_status, asset_group_primary_status_reason, asset_group_status
from typing import MutableSequence

__protobuf__: Incomplete

class AssetGroup(proto.Message):
    resource_name: str
    id: int
    campaign: str
    name: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    status: asset_group_status.AssetGroupStatusEnum.AssetGroupStatus
    primary_status: asset_group_primary_status.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    primary_status_reasons: MutableSequence[asset_group_primary_status_reason.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
    path1: str
    path2: str
    ad_strength: gage_ad_strength.AdStrengthEnum.AdStrength
    asset_coverage: AssetCoverage

class AssetCoverage(proto.Message):
    ad_strength_action_items: MutableSequence['AdStrengthActionItem']

class AdStrengthActionItem(proto.Message):
    class AddAssetDetails(proto.Message):
        asset_field_type: gage_asset_field_type.AssetFieldTypeEnum.AssetFieldType
        asset_count: int
        video_aspect_ratio_requirement: asset_coverage_video_aspect_ratio_requirement.AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
    action_item_type: ad_strength_action_item_type.AdStrengthActionItemTypeEnum.AdStrengthActionItemType
    add_asset_details: AddAssetDetails
