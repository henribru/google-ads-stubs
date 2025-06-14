import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import policy
from google.ads.googleads.v18.enums.types import policy_approval_status, policy_review_status
from typing import MutableSequence

__protobuf__: Incomplete

class PolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry]
    review_status: policy_review_status.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: policy_approval_status.PolicyApprovalStatusEnum.PolicyApprovalStatus
