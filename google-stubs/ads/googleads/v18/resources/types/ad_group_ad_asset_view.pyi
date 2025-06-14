import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import policy
from google.ads.googleads.v18.enums.types import asset_field_type, asset_performance_label, asset_source, policy_approval_status, policy_review_status, served_asset_field_type
from typing import MutableSequence

__protobuf__: Incomplete

class AdGroupAdAssetView(proto.Message):
    resource_name: str
    ad_group_ad: str
    asset: str
    field_type: asset_field_type.AssetFieldTypeEnum.AssetFieldType
    enabled: bool
    policy_summary: AdGroupAdAssetPolicySummary
    performance_label: asset_performance_label.AssetPerformanceLabelEnum.AssetPerformanceLabel
    pinned_field: served_asset_field_type.ServedAssetFieldTypeEnum.ServedAssetFieldType
    source: asset_source.AssetSourceEnum.AssetSource

class AdGroupAdAssetPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry]
    review_status: policy_review_status.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: policy_approval_status.PolicyApprovalStatusEnum.PolicyApprovalStatus
