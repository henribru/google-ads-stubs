from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v15.enums.types.asset_link_primary_status import (
    AssetLinkPrimaryStatusEnum,
)
from google.ads.googleads.v15.enums.types.asset_link_primary_status_reason import (
    AssetLinkPrimaryStatusReasonEnum,
)
from google.ads.googleads.v15.enums.types.asset_offline_evaluation_error_reasons import (
    AssetOfflineEvaluationErrorReasonsEnum,
)
from google.ads.googleads.v15.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v15.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)

_M = TypeVar("_M")

class AdAssetPolicySummary(proto.Message):
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

class AssetDisapproved(proto.Message):
    offline_evaluation_error_reasons: MutableSequence[
        AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        offline_evaluation_error_reasons: MutableSequence[
            AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["offline_evaluation_error_reasons"]
    ) -> bool: ...

class AssetLinkPrimaryStatusDetails(proto.Message):
    reason: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    asset_disapproved: AssetDisapproved
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        reason: AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason = ...,
        status: AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus = ...,
        asset_disapproved: AssetDisapproved = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["reason", "status", "asset_disapproved"]
    ) -> bool: ...
