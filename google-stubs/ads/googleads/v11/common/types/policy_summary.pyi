from typing import Any

import proto

from google.ads.googleads.v11.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v11.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v11.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

class PolicySummary(proto.Message):
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
