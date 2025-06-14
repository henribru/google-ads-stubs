import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import asset_policy, policy_summary as gagc_policy_summary
from google.ads.googleads.v19.enums.types import asset_field_type, asset_link_primary_status, asset_link_primary_status_reason, asset_link_status, asset_performance_label, asset_source
from typing import MutableSequence

__protobuf__: Incomplete

class AssetGroupAsset(proto.Message):
    resource_name: str
    asset_group: str
    asset: str
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType
    status: asset_link_status.AssetLinkStatusEnum.AssetLinkStatus
    primary_status: asset_link_primary_status.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    primary_status_reasons: MutableSequence[asset_link_primary_status_reason.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason]
    primary_status_details: MutableSequence[asset_policy.AssetLinkPrimaryStatusDetails]
    performance_label: asset_performance_label.AssetPerformanceLabelEnum.AssetPerformanceLabel
    policy_summary: gagc_policy_summary.PolicySummary
    source: asset_source.AssetSourceEnum.AssetSource
