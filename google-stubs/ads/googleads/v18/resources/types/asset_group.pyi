import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import ad_strength as gage_ad_strength, asset_group_primary_status, asset_group_primary_status_reason, asset_group_status
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
