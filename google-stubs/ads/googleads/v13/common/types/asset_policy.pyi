from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v13.enums.types.asset_link_primary_status import (
    AssetLinkPrimaryStatusEnum,
)
from google.ads.googleads.v13.enums.types.asset_link_primary_status_reason import (
    AssetLinkPrimaryStatusReasonEnum,
)
from google.ads.googleads.v13.enums.types.asset_offline_evaluation_error_reasons import (
    AssetOfflineEvaluationErrorReasonsEnum,
)
from google.ads.googleads.v13.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v13.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

class AdAssetPolicySummary(proto.Message):
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

class AssetDisapproved(proto.Message):
    offline_evaluation_error_reasons: MutableSequence[
        AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    ]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        offline_evaluation_error_reasons: MutableSequence[
            AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
        ] = ...
    ) -> None: ...

class AssetLinkPrimaryStatusDetails(proto.Message):
    reason: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    asset_disapproved: AssetDisapproved
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        reason: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason = ...,
        status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus = ...,
        asset_disapproved: AssetDisapproved = ...
    ) -> None: ...
