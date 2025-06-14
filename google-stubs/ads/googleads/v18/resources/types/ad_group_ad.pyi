import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import policy
from google.ads.googleads.v18.enums.types import ad_group_ad_primary_status, ad_group_ad_primary_status_reason, ad_group_ad_status, ad_strength as gage_ad_strength, asset_automation_status as gage_asset_automation_status, asset_automation_type as gage_asset_automation_type, policy_approval_status, policy_review_status
from google.ads.googleads.v18.resources.types import ad as gagr_ad
from typing import MutableSequence

__protobuf__: Incomplete

class AdGroupAd(proto.Message):
    resource_name: str
    status: ad_group_ad_status.AdGroupAdStatusEnum.AdGroupAdStatus
    ad_group: str
    ad: gagr_ad.Ad
    policy_summary: AdGroupAdPolicySummary
    ad_strength: gage_ad_strength.AdStrengthEnum.AdStrength
    action_items: MutableSequence[str]
    labels: MutableSequence[str]
    primary_status: ad_group_ad_primary_status.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    primary_status_reasons: MutableSequence[ad_group_ad_primary_status_reason.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason]
    ad_group_ad_asset_automation_settings: MutableSequence['AdGroupAdAssetAutomationSetting']

class AdGroupAdPolicySummary(proto.Message):
    policy_topic_entries: MutableSequence[policy.PolicyTopicEntry]
    review_status: policy_review_status.PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: policy_approval_status.PolicyApprovalStatusEnum.PolicyApprovalStatus

class AdGroupAdAssetAutomationSetting(proto.Message):
    asset_automation_type: gage_asset_automation_type.AssetAutomationTypeEnum.AssetAutomationType
    asset_automation_status: gage_asset_automation_status.AssetAutomationStatusEnum.AssetAutomationStatus
