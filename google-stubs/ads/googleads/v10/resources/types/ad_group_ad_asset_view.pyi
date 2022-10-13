from typing import Any

import proto

from google.ads.googleads.v10.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v10.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v10.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)
from google.ads.googleads.v10.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v10.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

class AdGroupAdAssetPolicySummary(proto.Message):
    policy_topic_entries: list[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_topic_entries: list[PolicyTopicEntry] = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...
    ) -> None: ...

class AdGroupAdAssetView(proto.Message):
    resource_name: str
    ad_group_ad: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    enabled: bool
    policy_summary: AdGroupAdAssetPolicySummary
    performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_ad: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        enabled: bool = ...,
        policy_summary: AdGroupAdAssetPolicySummary = ...,
        performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...
    ) -> None: ...
