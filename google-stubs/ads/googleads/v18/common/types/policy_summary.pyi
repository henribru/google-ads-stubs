from google.ads.googleads.v18.enums.types.policy_approval_status import PolicyApprovalStatusEnum
from google.ads.googleads.v18.enums.types.policy_review_status import PolicyReviewStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.policy import PolicyTopicEntry
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class PolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, policy_topic_entries: MutableSequence[PolicyTopicEntry] = ..., review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ..., approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["policy_topic_entries", "review_status", "approval_status"]) -> bool: ...
