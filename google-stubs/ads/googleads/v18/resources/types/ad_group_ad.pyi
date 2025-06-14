from google.ads.googleads.v18.enums.types.policy_approval_status import PolicyApprovalStatusEnum
from google.ads.googleads.v18.enums.types.policy_review_status import PolicyReviewStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v18.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v18.enums.types.asset_automation_status import AssetAutomationStatusEnum
from google.ads.googleads.v18.enums.types.asset_automation_type import AssetAutomationTypeEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.ad_group_ad_primary_status_reason import AdGroupAdPrimaryStatusReasonEnum
from google.ads.googleads.v18.enums.types.ad_group_ad_primary_status import AdGroupAdPrimaryStatusEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v18.enums.types.ad_strength import AdStrengthEnum
from google.ads.googleads.v18.resources.types.ad import Ad
from google.ads.googleads.v18.enums.types.ad_group_ad_status import AdGroupAdStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
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
    primary_status_reasons: MutableSequence[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
    ad_group_ad_asset_automation_settings: MutableSequence[AdGroupAdAssetAutomationSetting]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., status: AdGroupAdStatusEnum.AdGroupAdStatus = ..., ad_group: str = ..., ad: Ad = ..., policy_summary: AdGroupAdPolicySummary = ..., ad_strength: AdStrengthEnum.AdStrength = ..., action_items: MutableSequence[str] = ..., labels: MutableSequence[str] = ..., primary_status: AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus = ..., primary_status_reasons: MutableSequence[AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason] = ..., ad_group_ad_asset_automation_settings: MutableSequence[AdGroupAdAssetAutomationSetting] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "status", "ad_group", "ad", "policy_summary", "ad_strength", "action_items", "labels", "primary_status", "primary_status_reasons", "ad_group_ad_asset_automation_settings"]) -> bool: ...
class AdGroupAdAssetAutomationSetting(proto.Message):
    asset_automation_type: AssetAutomationTypeEnum.AssetAutomationType
    asset_automation_status: AssetAutomationStatusEnum.AssetAutomationStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, asset_automation_type: AssetAutomationTypeEnum.AssetAutomationType = ..., asset_automation_status: AssetAutomationStatusEnum.AssetAutomationStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["asset_automation_type", "asset_automation_status"]) -> bool: ...
class AdGroupAdPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, policy_topic_entries: MutableSequence[PolicyTopicEntry] = ..., review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ..., approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["policy_topic_entries", "review_status", "approval_status"]) -> bool: ...
