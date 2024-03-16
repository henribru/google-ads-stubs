from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v16.enums.types.ad_group_ad_primary_status import (
    AdGroupAdPrimaryStatusEnum,
)
from google.ads.googleads.v16.enums.types.ad_group_ad_primary_status_reason import (
    AdGroupAdPrimaryStatusReasonEnum,
)
from google.ads.googleads.v16.enums.types.ad_group_ad_status import AdGroupAdStatusEnum
from google.ads.googleads.v16.enums.types.ad_strength import AdStrengthEnum
from google.ads.googleads.v16.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v16.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v16.resources.types.ad import Ad

_M = TypeVar("_M")

class AdGroupAd(proto.Message):
    resource_name: str
    status: AdGroupAdStatusEnum.AdGroupAdStatus
    ad_group: str
    ad: Ad
    policy_summary: AdGroupAdPolicySummary
    ad_strength: AdStrengthEnum.AdStrength
    action_items: MutableSequence[str]
    labels: MutableSequence[str]
    primary_status: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    primary_status_reasons: MutableSequence[
        AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        status: AdGroupAdStatusEnum.AdGroupAdStatus = ...,
        ad_group: str = ...,
        ad: Ad = ...,
        policy_summary: AdGroupAdPolicySummary = ...,
        ad_strength: AdStrengthEnum.AdStrength = ...,
        action_items: MutableSequence[str] = ...,
        labels: MutableSequence[str] = ...,
        primary_status: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus = ...,
        primary_status_reasons: MutableSequence[
            AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "status",
            "ad_group",
            "ad",
            "policy_summary",
            "ad_strength",
            "action_items",
            "labels",
            "primary_status",
            "primary_status_reasons",
        ],
    ) -> bool: ...

class AdGroupAdPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        policy_topic_entries: MutableSequence[PolicyTopicEntry] = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["policy_topic_entries", "review_status", "approval_status"]
    ) -> bool: ...
