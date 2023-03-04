from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v13.enums.types.ad_group_ad_status import AdGroupAdStatusEnum
from google.ads.googleads.v13.enums.types.ad_strength import AdStrengthEnum
from google.ads.googleads.v13.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v13.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v13.resources.types.ad import Ad

class AdGroupAd(proto.Message):
    resource_name: str
    status: AdGroupAdStatusEnum.AdGroupAdStatus
    ad_group: str
    ad: Ad
    policy_summary: AdGroupAdPolicySummary
    ad_strength: AdStrengthEnum.AdStrength
    action_items: MutableSequence[str]
    labels: MutableSequence[str]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        status: AdGroupAdStatusEnum.AdGroupAdStatus = ...,
        ad_group: str = ...,
        ad: Ad = ...,
        policy_summary: AdGroupAdPolicySummary = ...,
        ad_strength: AdStrengthEnum.AdStrength = ...,
        action_items: MutableSequence[str] = ...,
        labels: MutableSequence[str] = ...
    ) -> None: ...

class AdGroupAdPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_topic_entries: MutableSequence[PolicyTopicEntry] = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...
    ) -> None: ...
