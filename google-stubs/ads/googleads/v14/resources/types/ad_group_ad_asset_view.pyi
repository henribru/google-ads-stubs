from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v14.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v14.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)
from google.ads.googleads.v14.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v14.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v14.enums.types.served_asset_field_type import (
    ServedAssetFieldTypeEnum,
)

_M = TypeVar("_M")

class AdGroupAdAssetPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_topic_entries: MutableSequence[PolicyTopicEntry] = ...,
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
    pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_ad: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        enabled: bool = ...,
        policy_summary: AdGroupAdAssetPolicySummary = ...,
        performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...
    ) -> None: ...
