from typing import Any

import proto

from google.ads.googleads.v11.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v11.enums.types.ad_group_ad_status import AdGroupAdStatusEnum
from google.ads.googleads.v11.enums.types.ad_strength import AdStrengthEnum
from google.ads.googleads.v11.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v11.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v11.resources.types.ad import Ad

class AdGroupAd(proto.Message):
    resource_name: str
    status: AdGroupAdStatusEnum.AdGroupAdStatus
    ad_group: str
    ad: Ad
    policy_summary: AdGroupAdPolicySummary
    ad_strength: AdStrengthEnum.AdStrength
    action_items: list[str]
    labels: list[str]
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
        action_items: list[str] = ...,
        labels: list[str] = ...
    ) -> None: ...

class AdGroupAdPolicySummary(proto.Message):
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
