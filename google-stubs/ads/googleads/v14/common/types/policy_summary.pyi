from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v14.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v14.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

_M = TypeVar("_M")

class PolicySummary(proto.Message):
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
