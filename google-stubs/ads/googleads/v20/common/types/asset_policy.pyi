import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import policy
from google.ads.googleads.v20.enums.types import asset_link_primary_status, asset_link_primary_status_reason, asset_offline_evaluation_error_reasons, policy_approval_status, policy_review_status
from typing import MutableSequence

__protobuf__: Incomplete

class AdAssetPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry]
    review_status: policy_review_status.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: policy_approval_status.PolicyApprovalStatusEnum.PolicyApprovalStatus

class AssetLinkPrimaryStatusDetails(proto.Message):
    reason: asset_link_primary_status_reason.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    status: asset_link_primary_status.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    asset_disapproved: AssetDisapproved

class AssetDisapproved(proto.Message):
    offline_evaluation_error_reasons: MutableSequence[asset_offline_evaluation_error_reasons.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons]
