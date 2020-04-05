from google.ads.google_ads.v2.proto.common import ad_asset_pb2 as ad_asset_pb2

AdAssetPb2 = ad_asset_pb2
AdImageAsset = ad_asset_pb2.AdImageAsset
AdMediaBundleAsset = ad_asset_pb2.AdMediaBundleAsset
AdTextAsset = ad_asset_pb2.AdTextAsset
AdVideoAsset = ad_asset_pb2.AdVideoAsset

from google.ads.google_ads.v2.proto.common import ad_type_infos_pb2 as ad_type_infos_pb2

AdTypeInfosPb2 = ad_type_infos_pb2
AppAdInfo = ad_type_infos_pb2.AppAdInfo
AppEngagementAdInfo = ad_type_infos_pb2.AppEngagementAdInfo
CallOnlyAdInfo = ad_type_infos_pb2.CallOnlyAdInfo
DisplayCallToAction = ad_type_infos_pb2.DisplayCallToAction
DisplayUploadAdInfo = ad_type_infos_pb2.DisplayUploadAdInfo
ExpandedDynamicSearchAdInfo = ad_type_infos_pb2.ExpandedDynamicSearchAdInfo
ExpandedTextAdInfo = ad_type_infos_pb2.ExpandedTextAdInfo
GmailAdInfo = ad_type_infos_pb2.GmailAdInfo
GmailTeaser = ad_type_infos_pb2.GmailTeaser
HotelAdInfo = ad_type_infos_pb2.HotelAdInfo
ImageAdInfo = ad_type_infos_pb2.ImageAdInfo
LegacyAppInstallAdInfo = ad_type_infos_pb2.LegacyAppInstallAdInfo
LegacyResponsiveDisplayAdInfo = ad_type_infos_pb2.LegacyResponsiveDisplayAdInfo
ProductImage = ad_type_infos_pb2.ProductImage
ProductVideo = ad_type_infos_pb2.ProductVideo
ResponsiveDisplayAdInfo = ad_type_infos_pb2.ResponsiveDisplayAdInfo
ResponsiveSearchAdInfo = ad_type_infos_pb2.ResponsiveSearchAdInfo
ShoppingComparisonListingAdInfo = ad_type_infos_pb2.ShoppingComparisonListingAdInfo
ShoppingProductAdInfo = ad_type_infos_pb2.ShoppingProductAdInfo
ShoppingSmartAdInfo = ad_type_infos_pb2.ShoppingSmartAdInfo
TextAdInfo = ad_type_infos_pb2.TextAdInfo
VideoAdInfo = ad_type_infos_pb2.VideoAdInfo
VideoBumperInStreamAdInfo = ad_type_infos_pb2.VideoBumperInStreamAdInfo
VideoNonSkippableInStreamAdInfo = ad_type_infos_pb2.VideoNonSkippableInStreamAdInfo
VideoOutstreamAdInfo = ad_type_infos_pb2.VideoOutstreamAdInfo
VideoTrueViewInStreamAdInfo = ad_type_infos_pb2.VideoTrueViewInStreamAdInfo

from google.ads.google_ads.v2.proto.common import asset_types_pb2 as asset_types_pb2

AssetTypesPb2 = asset_types_pb2
ImageAsset = asset_types_pb2.ImageAsset
ImageDimension = asset_types_pb2.ImageDimension
MediaBundleAsset = asset_types_pb2.MediaBundleAsset
TextAsset = asset_types_pb2.TextAsset
YoutubeVideoAsset = asset_types_pb2.YoutubeVideoAsset

from google.ads.google_ads.v2.proto.common import bidding_pb2 as bidding_pb2

BiddingPb2 = bidding_pb2
Commission = bidding_pb2.Commission
EnhancedCpc = bidding_pb2.EnhancedCpc
ManualCpc = bidding_pb2.ManualCpc
ManualCpm = bidding_pb2.ManualCpm
ManualCpv = bidding_pb2.ManualCpv
MaximizeConversions = bidding_pb2.MaximizeConversions
MaximizeConversionValue = bidding_pb2.MaximizeConversionValue
PageOnePromoted = bidding_pb2.PageOnePromoted
PercentCpc = bidding_pb2.PercentCpc
TargetCpa = bidding_pb2.TargetCpa
TargetCpm = bidding_pb2.TargetCpm
TargetImpressionShare = bidding_pb2.TargetImpressionShare
TargetOutrankShare = bidding_pb2.TargetOutrankShare
TargetRoas = bidding_pb2.TargetRoas
TargetSpend = bidding_pb2.TargetSpend

from google.ads.google_ads.v2.proto.common import (
    click_location_pb2 as click_location_pb2,
)

ClickLocationPb2 = click_location_pb2
ClickLocation = click_location_pb2.ClickLocation

from google.ads.google_ads.v2.proto.common import criteria_pb2 as criteria_pb2

CriteriaPb2 = criteria_pb2
AddressInfo = criteria_pb2.AddressInfo
AdScheduleInfo = criteria_pb2.AdScheduleInfo
AgeRangeInfo = criteria_pb2.AgeRangeInfo
AppPaymentModelInfo = criteria_pb2.AppPaymentModelInfo
CarrierInfo = criteria_pb2.CarrierInfo
ContentLabelInfo = criteria_pb2.ContentLabelInfo
CustomAffinityInfo = criteria_pb2.CustomAffinityInfo
CustomIntentInfo = criteria_pb2.CustomIntentInfo
DeviceInfo = criteria_pb2.DeviceInfo
GenderInfo = criteria_pb2.GenderInfo
GeoPointInfo = criteria_pb2.GeoPointInfo
HotelAdvanceBookingWindowInfo = criteria_pb2.HotelAdvanceBookingWindowInfo
HotelCheckInDayInfo = criteria_pb2.HotelCheckInDayInfo
HotelCityInfo = criteria_pb2.HotelCityInfo
HotelClassInfo = criteria_pb2.HotelClassInfo
HotelCountryRegionInfo = criteria_pb2.HotelCountryRegionInfo
HotelDateSelectionTypeInfo = criteria_pb2.HotelDateSelectionTypeInfo
HotelIdInfo = criteria_pb2.HotelIdInfo
HotelLengthOfStayInfo = criteria_pb2.HotelLengthOfStayInfo
HotelStateInfo = criteria_pb2.HotelStateInfo
IncomeRangeInfo = criteria_pb2.IncomeRangeInfo
InteractionTypeInfo = criteria_pb2.InteractionTypeInfo
IpBlockInfo = criteria_pb2.IpBlockInfo
KeywordInfo = criteria_pb2.KeywordInfo
LanguageInfo = criteria_pb2.LanguageInfo
ListingBrandInfo = criteria_pb2.ListingBrandInfo
ListingCustomAttributeInfo = criteria_pb2.ListingCustomAttributeInfo
ListingDimensionInfo = criteria_pb2.ListingDimensionInfo
ListingGroupInfo = criteria_pb2.ListingGroupInfo
ListingScopeInfo = criteria_pb2.ListingScopeInfo
LocationGroupInfo = criteria_pb2.LocationGroupInfo
LocationInfo = criteria_pb2.LocationInfo
MobileAppCategoryInfo = criteria_pb2.MobileAppCategoryInfo
MobileApplicationInfo = criteria_pb2.MobileApplicationInfo
MobileDeviceInfo = criteria_pb2.MobileDeviceInfo
OperatingSystemVersionInfo = criteria_pb2.OperatingSystemVersionInfo
ParentalStatusInfo = criteria_pb2.ParentalStatusInfo
PlacementInfo = criteria_pb2.PlacementInfo
PreferredContentInfo = criteria_pb2.PreferredContentInfo
ProductBiddingCategoryInfo = criteria_pb2.ProductBiddingCategoryInfo
ProductChannelExclusivityInfo = criteria_pb2.ProductChannelExclusivityInfo
ProductChannelInfo = criteria_pb2.ProductChannelInfo
ProductConditionInfo = criteria_pb2.ProductConditionInfo
ProductItemIdInfo = criteria_pb2.ProductItemIdInfo
ProductTypeInfo = criteria_pb2.ProductTypeInfo
ProximityInfo = criteria_pb2.ProximityInfo
TopicInfo = criteria_pb2.TopicInfo
UnknownListingDimensionInfo = criteria_pb2.UnknownListingDimensionInfo
UserInterestInfo = criteria_pb2.UserInterestInfo
UserListInfo = criteria_pb2.UserListInfo
WebpageConditionInfo = criteria_pb2.WebpageConditionInfo
WebpageInfo = criteria_pb2.WebpageInfo
YouTubeChannelInfo = criteria_pb2.YouTubeChannelInfo
YouTubeVideoInfo = criteria_pb2.YouTubeVideoInfo

from google.ads.google_ads.v2.proto.common import (
    criterion_category_availability_pb2 as criterion_category_availability_pb2,
)

CriterionCategoryAvailabilityPb2 = criterion_category_availability_pb2
CriterionCategoryAvailability = (
    criterion_category_availability_pb2.CriterionCategoryAvailability
)
CriterionCategoryChannelAvailability = (
    criterion_category_availability_pb2.CriterionCategoryChannelAvailability
)
CriterionCategoryLocaleAvailability = (
    criterion_category_availability_pb2.CriterionCategoryLocaleAvailability
)

from google.ads.google_ads.v2.proto.common import (
    custom_parameter_pb2 as custom_parameter_pb2,
)

CustomParameterPb2 = custom_parameter_pb2
CustomParameter = custom_parameter_pb2.CustomParameter

from google.ads.google_ads.v2.proto.common import dates_pb2 as dates_pb2

DatesPb2 = dates_pb2
DateRange = dates_pb2.DateRange

from google.ads.google_ads.v2.proto.common import (
    explorer_auto_optimizer_setting_pb2 as explorer_auto_optimizer_setting_pb2,
)

ExplorerAutoOptimizerSettingPb2 = explorer_auto_optimizer_setting_pb2
ExplorerAutoOptimizerSetting = (
    explorer_auto_optimizer_setting_pb2.ExplorerAutoOptimizerSetting
)

from google.ads.google_ads.v2.proto.common import extensions_pb2 as extensions_pb2

ExtensionsPb2 = extensions_pb2
AffiliateLocationFeedItem = extensions_pb2.AffiliateLocationFeedItem
AppFeedItem = extensions_pb2.AppFeedItem
CallFeedItem = extensions_pb2.CallFeedItem
CalloutFeedItem = extensions_pb2.CalloutFeedItem
HotelCalloutFeedItem = extensions_pb2.HotelCalloutFeedItem
LocationFeedItem = extensions_pb2.LocationFeedItem
PriceFeedItem = extensions_pb2.PriceFeedItem
PriceOffer = extensions_pb2.PriceOffer
PromotionFeedItem = extensions_pb2.PromotionFeedItem
SitelinkFeedItem = extensions_pb2.SitelinkFeedItem
StructuredSnippetFeedItem = extensions_pb2.StructuredSnippetFeedItem
TextMessageFeedItem = extensions_pb2.TextMessageFeedItem

from google.ads.google_ads.v2.proto.common import feed_common_pb2 as feed_common_pb2

FeedCommonPb2 = feed_common_pb2
Money = feed_common_pb2.Money

from google.ads.google_ads.v2.proto.common import final_app_url_pb2 as final_app_url_pb2

FinalAppUrlPb2 = final_app_url_pb2
FinalAppUrl = final_app_url_pb2.FinalAppUrl

from google.ads.google_ads.v2.proto.common import final_url_pb2 as final_url_pb2

FinalUrlPb2 = final_url_pb2

from google.ads.google_ads.v2.proto.common import frequency_cap_pb2 as frequency_cap_pb2

FrequencyCapPb2 = frequency_cap_pb2
FrequencyCapEntry = frequency_cap_pb2.FrequencyCapEntry
FrequencyCapKey = frequency_cap_pb2.FrequencyCapKey

from google.ads.google_ads.v2.proto.common import (
    keyword_plan_common_pb2 as keyword_plan_common_pb2,
)

KeywordPlanCommonPb2 = keyword_plan_common_pb2
KeywordPlanHistoricalMetrics = keyword_plan_common_pb2.KeywordPlanHistoricalMetrics

from google.ads.google_ads.v2.proto.common import (
    matching_function_pb2 as matching_function_pb2,
)

MatchingFunctionPb2 = matching_function_pb2
MatchingFunction = matching_function_pb2.MatchingFunction
Operand = matching_function_pb2.Operand

from google.ads.google_ads.v2.proto.common import metrics_pb2 as metrics_pb2

MetricsPb2 = metrics_pb2
Metrics = metrics_pb2.Metrics

from google.ads.google_ads.v2.proto.common import mutate_pb2 as mutate_pb2

MutatePb2 = mutate_pb2

from google.ads.google_ads.v2.proto.common import (
    offline_user_data_pb2 as offline_user_data_pb2,
)

OfflineUserDataPb2 = offline_user_data_pb2

from google.ads.google_ads.v2.proto.common import policy_pb2 as policy_pb2

PolicyPb2 = policy_pb2
PolicyTopicConstraint = policy_pb2.PolicyTopicConstraint
PolicyTopicEntry = policy_pb2.PolicyTopicEntry
PolicyTopicEvidence = policy_pb2.PolicyTopicEvidence
PolicyValidationParameter = policy_pb2.PolicyValidationParameter
PolicyViolationKey = policy_pb2.PolicyViolationKey

from google.ads.google_ads.v2.proto.common import (
    real_time_bidding_setting_pb2 as real_time_bidding_setting_pb2,
)

RealTimeBiddingSettingPb2 = real_time_bidding_setting_pb2
RealTimeBiddingSetting = real_time_bidding_setting_pb2.RealTimeBiddingSetting

from google.ads.google_ads.v2.proto.common import segments_pb2 as segments_pb2

SegmentsPb2 = segments_pb2
Keyword = segments_pb2.Keyword
Segments = segments_pb2.Segments

from google.ads.google_ads.v2.proto.common import simulation_pb2 as simulation_pb2

SimulationPb2 = simulation_pb2
BidModifierSimulationPoint = simulation_pb2.BidModifierSimulationPoint
BidModifierSimulationPointList = simulation_pb2.BidModifierSimulationPointList
CpcBidSimulationPoint = simulation_pb2.CpcBidSimulationPoint
CpcBidSimulationPointList = simulation_pb2.CpcBidSimulationPointList
CpvBidSimulationPoint = simulation_pb2.CpvBidSimulationPoint
CpvBidSimulationPointList = simulation_pb2.CpvBidSimulationPointList
TargetCpaSimulationPoint = simulation_pb2.TargetCpaSimulationPoint
TargetCpaSimulationPointList = simulation_pb2.TargetCpaSimulationPointList

from google.ads.google_ads.v2.proto.common import tag_snippet_pb2 as tag_snippet_pb2

TagSnippetPb2 = tag_snippet_pb2
TagSnippet = tag_snippet_pb2.TagSnippet

from google.ads.google_ads.v2.proto.common import (
    targeting_setting_pb2 as targeting_setting_pb2,
)

TargetingSettingPb2 = targeting_setting_pb2
TargetingSetting = targeting_setting_pb2.TargetingSetting
TargetRestriction = targeting_setting_pb2.TargetRestriction

from google.ads.google_ads.v2.proto.common import text_label_pb2 as text_label_pb2

TextLabelPb2 = text_label_pb2
TextLabel = text_label_pb2.TextLabel

from google.ads.google_ads.v2.proto.common import (
    url_collection_pb2 as url_collection_pb2,
)

UrlCollectionPb2 = url_collection_pb2
UrlCollection = url_collection_pb2.UrlCollection

from google.ads.google_ads.v2.proto.common import user_lists_pb2 as user_lists_pb2

UserListsPb2 = user_lists_pb2
BasicUserListInfo = user_lists_pb2.BasicUserListInfo
CombinedRuleUserListInfo = user_lists_pb2.CombinedRuleUserListInfo
CrmBasedUserListInfo = user_lists_pb2.CrmBasedUserListInfo
DateSpecificRuleUserListInfo = user_lists_pb2.DateSpecificRuleUserListInfo
ExpressionRuleUserListInfo = user_lists_pb2.ExpressionRuleUserListInfo
LogicalUserListInfo = user_lists_pb2.LogicalUserListInfo
LogicalUserListOperandInfo = user_lists_pb2.LogicalUserListOperandInfo
RuleBasedUserListInfo = user_lists_pb2.RuleBasedUserListInfo
SimilarUserListInfo = user_lists_pb2.SimilarUserListInfo
UserListActionInfo = user_lists_pb2.UserListActionInfo
UserListDateRuleItemInfo = user_lists_pb2.UserListDateRuleItemInfo
UserListLogicalRuleInfo = user_lists_pb2.UserListLogicalRuleInfo
UserListNumberRuleItemInfo = user_lists_pb2.UserListNumberRuleItemInfo
UserListRuleInfo = user_lists_pb2.UserListRuleInfo
UserListRuleItemGroupInfo = user_lists_pb2.UserListRuleItemGroupInfo
UserListRuleItemInfo = user_lists_pb2.UserListRuleItemInfo
UserListStringRuleItemInfo = user_lists_pb2.UserListStringRuleItemInfo

from google.ads.google_ads.v2.proto.common import value_pb2 as value_pb2

ValuePb2 = value_pb2
Value = value_pb2.Value

from google.ads.google_ads.v2.proto.enums import access_reason_pb2 as access_reason_pb2

AccessReasonPb2 = access_reason_pb2
AccessReasonEnum = access_reason_pb2.AccessReasonEnum

from google.ads.google_ads.v2.proto.enums import access_role_pb2 as access_role_pb2

AccessRolePb2 = access_role_pb2
AccessRoleEnum = access_role_pb2.AccessRoleEnum

from google.ads.google_ads.v2.proto.enums import (
    account_budget_proposal_status_pb2 as account_budget_proposal_status_pb2,
)

AccountBudgetProposalStatusPb2 = account_budget_proposal_status_pb2
AccountBudgetProposalStatusEnum = (
    account_budget_proposal_status_pb2.AccountBudgetProposalStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    account_budget_proposal_type_pb2 as account_budget_proposal_type_pb2,
)

AccountBudgetProposalTypePb2 = account_budget_proposal_type_pb2
AccountBudgetProposalTypeEnum = (
    account_budget_proposal_type_pb2.AccountBudgetProposalTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    account_budget_status_pb2 as account_budget_status_pb2,
)

AccountBudgetStatusPb2 = account_budget_status_pb2
AccountBudgetStatusEnum = account_budget_status_pb2.AccountBudgetStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    ad_customizer_placeholder_field_pb2 as ad_customizer_placeholder_field_pb2,
)

AdCustomizerPlaceholderFieldPb2 = ad_customizer_placeholder_field_pb2
AdCustomizerPlaceholderFieldEnum = (
    ad_customizer_placeholder_field_pb2.AdCustomizerPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    ad_group_ad_rotation_mode_pb2 as ad_group_ad_rotation_mode_pb2,
)

AdGroupAdRotationModePb2 = ad_group_ad_rotation_mode_pb2
AdGroupAdRotationModeEnum = ad_group_ad_rotation_mode_pb2.AdGroupAdRotationModeEnum

from google.ads.google_ads.v2.proto.enums import (
    ad_group_ad_status_pb2 as ad_group_ad_status_pb2,
)

AdGroupAdStatusPb2 = ad_group_ad_status_pb2
AdGroupAdStatusEnum = ad_group_ad_status_pb2.AdGroupAdStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    ad_group_criterion_approval_status_pb2 as ad_group_criterion_approval_status_pb2,
)

AdGroupCriterionApprovalStatusPb2 = ad_group_criterion_approval_status_pb2
AdGroupCriterionApprovalStatusEnum = (
    ad_group_criterion_approval_status_pb2.AdGroupCriterionApprovalStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    ad_group_criterion_status_pb2 as ad_group_criterion_status_pb2,
)

AdGroupCriterionStatusPb2 = ad_group_criterion_status_pb2
AdGroupCriterionStatusEnum = ad_group_criterion_status_pb2.AdGroupCriterionStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    ad_group_status_pb2 as ad_group_status_pb2,
)

AdGroupStatusPb2 = ad_group_status_pb2
AdGroupStatusEnum = ad_group_status_pb2.AdGroupStatusEnum

from google.ads.google_ads.v2.proto.enums import ad_group_type_pb2 as ad_group_type_pb2

AdGroupTypePb2 = ad_group_type_pb2
AdGroupTypeEnum = ad_group_type_pb2.AdGroupTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    ad_network_type_pb2 as ad_network_type_pb2,
)

AdNetworkTypePb2 = ad_network_type_pb2
AdNetworkTypeEnum = ad_network_type_pb2.AdNetworkTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    ad_serving_optimization_status_pb2 as ad_serving_optimization_status_pb2,
)

AdServingOptimizationStatusPb2 = ad_serving_optimization_status_pb2
AdServingOptimizationStatusEnum = (
    ad_serving_optimization_status_pb2.AdServingOptimizationStatusEnum
)

from google.ads.google_ads.v2.proto.enums import ad_strength_pb2 as ad_strength_pb2

AdStrengthPb2 = ad_strength_pb2
AdStrengthEnum = ad_strength_pb2.AdStrengthEnum

from google.ads.google_ads.v2.proto.enums import ad_type_pb2 as ad_type_pb2

AdTypePb2 = ad_type_pb2
AdTypeEnum = ad_type_pb2.AdTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    advertising_channel_sub_type_pb2 as advertising_channel_sub_type_pb2,
)

AdvertisingChannelSubTypePb2 = advertising_channel_sub_type_pb2
AdvertisingChannelSubTypeEnum = (
    advertising_channel_sub_type_pb2.AdvertisingChannelSubTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    advertising_channel_type_pb2 as advertising_channel_type_pb2,
)

AdvertisingChannelTypePb2 = advertising_channel_type_pb2
AdvertisingChannelTypeEnum = advertising_channel_type_pb2.AdvertisingChannelTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    affiliate_location_feed_relationship_type_pb2 as affiliate_location_feed_relationship_type_pb2,
)

AffiliateLocationFeedRelationshipTypePb2 = affiliate_location_feed_relationship_type_pb2
AffiliateLocationFeedRelationshipTypeEnum = (
    affiliate_location_feed_relationship_type_pb2.AffiliateLocationFeedRelationshipTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    affiliate_location_placeholder_field_pb2 as affiliate_location_placeholder_field_pb2,
)

AffiliateLocationPlaceholderFieldPb2 = affiliate_location_placeholder_field_pb2
AffiliateLocationPlaceholderFieldEnum = (
    affiliate_location_placeholder_field_pb2.AffiliateLocationPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    age_range_type_pb2 as age_range_type_pb2,
)

AgeRangeTypePb2 = age_range_type_pb2
AgeRangeTypeEnum = age_range_type_pb2.AgeRangeTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    app_campaign_app_store_pb2 as app_campaign_app_store_pb2,
)

AppCampaignAppStorePb2 = app_campaign_app_store_pb2
AppCampaignAppStoreEnum = app_campaign_app_store_pb2.AppCampaignAppStoreEnum

from google.ads.google_ads.v2.proto.enums import (
    app_campaign_bidding_strategy_goal_type_pb2 as app_campaign_bidding_strategy_goal_type_pb2,
)

AppCampaignBiddingStrategyGoalTypePb2 = app_campaign_bidding_strategy_goal_type_pb2
AppCampaignBiddingStrategyGoalTypeEnum = (
    app_campaign_bidding_strategy_goal_type_pb2.AppCampaignBiddingStrategyGoalTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    app_payment_model_type_pb2 as app_payment_model_type_pb2,
)

AppPaymentModelTypePb2 = app_payment_model_type_pb2
AppPaymentModelTypeEnum = app_payment_model_type_pb2.AppPaymentModelTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    app_placeholder_field_pb2 as app_placeholder_field_pb2,
)

AppPlaceholderFieldPb2 = app_placeholder_field_pb2
AppPlaceholderFieldEnum = app_placeholder_field_pb2.AppPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import app_store_pb2 as app_store_pb2

AppStorePb2 = app_store_pb2
AppStoreEnum = app_store_pb2.AppStoreEnum

from google.ads.google_ads.v2.proto.enums import (
    app_url_operating_system_type_pb2 as app_url_operating_system_type_pb2,
)

AppUrlOperatingSystemTypePb2 = app_url_operating_system_type_pb2
AppUrlOperatingSystemTypeEnum = (
    app_url_operating_system_type_pb2.AppUrlOperatingSystemTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    asset_field_type_pb2 as asset_field_type_pb2,
)

AssetFieldTypePb2 = asset_field_type_pb2
AssetFieldTypeEnum = asset_field_type_pb2.AssetFieldTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    asset_performance_label_pb2 as asset_performance_label_pb2,
)

AssetPerformanceLabelPb2 = asset_performance_label_pb2
AssetPerformanceLabelEnum = asset_performance_label_pb2.AssetPerformanceLabelEnum

from google.ads.google_ads.v2.proto.enums import asset_type_pb2 as asset_type_pb2

AssetTypePb2 = asset_type_pb2
AssetTypeEnum = asset_type_pb2.AssetTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    attribution_model_pb2 as attribution_model_pb2,
)

AttributionModelPb2 = attribution_model_pb2
AttributionModelEnum = attribution_model_pb2.AttributionModelEnum

from google.ads.google_ads.v2.proto.enums import (
    bid_modifier_source_pb2 as bid_modifier_source_pb2,
)

BidModifierSourcePb2 = bid_modifier_source_pb2
BidModifierSourceEnum = bid_modifier_source_pb2.BidModifierSourceEnum

from google.ads.google_ads.v2.proto.enums import (
    bidding_source_pb2 as bidding_source_pb2,
)

BiddingSourcePb2 = bidding_source_pb2
BiddingSourceEnum = bidding_source_pb2.BiddingSourceEnum

from google.ads.google_ads.v2.proto.enums import (
    bidding_strategy_status_pb2 as bidding_strategy_status_pb2,
)

BiddingStrategyStatusPb2 = bidding_strategy_status_pb2
BiddingStrategyStatusEnum = bidding_strategy_status_pb2.BiddingStrategyStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    bidding_strategy_type_pb2 as bidding_strategy_type_pb2,
)

BiddingStrategyTypePb2 = bidding_strategy_type_pb2
BiddingStrategyTypeEnum = bidding_strategy_type_pb2.BiddingStrategyTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    billing_setup_status_pb2 as billing_setup_status_pb2,
)

BillingSetupStatusPb2 = billing_setup_status_pb2
BillingSetupStatusEnum = billing_setup_status_pb2.BillingSetupStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    brand_safety_suitability_pb2 as brand_safety_suitability_pb2,
)

BrandSafetySuitabilityPb2 = brand_safety_suitability_pb2
BrandSafetySuitabilityEnum = brand_safety_suitability_pb2.BrandSafetySuitabilityEnum

from google.ads.google_ads.v2.proto.enums import (
    budget_delivery_method_pb2 as budget_delivery_method_pb2,
)

BudgetDeliveryMethodPb2 = budget_delivery_method_pb2
BudgetDeliveryMethodEnum = budget_delivery_method_pb2.BudgetDeliveryMethodEnum

from google.ads.google_ads.v2.proto.enums import budget_period_pb2 as budget_period_pb2

BudgetPeriodPb2 = budget_period_pb2
BudgetPeriodEnum = budget_period_pb2.BudgetPeriodEnum

from google.ads.google_ads.v2.proto.enums import budget_status_pb2 as budget_status_pb2

BudgetStatusPb2 = budget_status_pb2
BudgetStatusEnum = budget_status_pb2.BudgetStatusEnum

from google.ads.google_ads.v2.proto.enums import budget_type_pb2 as budget_type_pb2

BudgetTypePb2 = budget_type_pb2
BudgetTypeEnum = budget_type_pb2.BudgetTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    call_conversion_reporting_state_pb2 as call_conversion_reporting_state_pb2,
)

CallConversionReportingStatePb2 = call_conversion_reporting_state_pb2
CallConversionReportingStateEnum = (
    call_conversion_reporting_state_pb2.CallConversionReportingStateEnum
)

from google.ads.google_ads.v2.proto.enums import (
    call_placeholder_field_pb2 as call_placeholder_field_pb2,
)

CallPlaceholderFieldPb2 = call_placeholder_field_pb2
CallPlaceholderFieldEnum = call_placeholder_field_pb2.CallPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    callout_placeholder_field_pb2 as callout_placeholder_field_pb2,
)

CalloutPlaceholderFieldPb2 = callout_placeholder_field_pb2
CalloutPlaceholderFieldEnum = callout_placeholder_field_pb2.CalloutPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    campaign_criterion_status_pb2 as campaign_criterion_status_pb2,
)

CampaignCriterionStatusPb2 = campaign_criterion_status_pb2
CampaignCriterionStatusEnum = campaign_criterion_status_pb2.CampaignCriterionStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    campaign_draft_status_pb2 as campaign_draft_status_pb2,
)

CampaignDraftStatusPb2 = campaign_draft_status_pb2
CampaignDraftStatusEnum = campaign_draft_status_pb2.CampaignDraftStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    campaign_experiment_status_pb2 as campaign_experiment_status_pb2,
)

CampaignExperimentStatusPb2 = campaign_experiment_status_pb2
CampaignExperimentStatusEnum = (
    campaign_experiment_status_pb2.CampaignExperimentStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    campaign_experiment_traffic_split_type_pb2 as campaign_experiment_traffic_split_type_pb2,
)

CampaignExperimentTrafficSplitTypePb2 = campaign_experiment_traffic_split_type_pb2
CampaignExperimentTrafficSplitTypeEnum = (
    campaign_experiment_traffic_split_type_pb2.CampaignExperimentTrafficSplitTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    campaign_experiment_type_pb2 as campaign_experiment_type_pb2,
)

CampaignExperimentTypePb2 = campaign_experiment_type_pb2
CampaignExperimentTypeEnum = campaign_experiment_type_pb2.CampaignExperimentTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    campaign_serving_status_pb2 as campaign_serving_status_pb2,
)

CampaignServingStatusPb2 = campaign_serving_status_pb2
CampaignServingStatusEnum = campaign_serving_status_pb2.CampaignServingStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    campaign_shared_set_status_pb2 as campaign_shared_set_status_pb2,
)

CampaignSharedSetStatusPb2 = campaign_shared_set_status_pb2
CampaignSharedSetStatusEnum = campaign_shared_set_status_pb2.CampaignSharedSetStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    campaign_status_pb2 as campaign_status_pb2,
)

CampaignStatusPb2 = campaign_status_pb2
CampaignStatusEnum = campaign_status_pb2.CampaignStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    change_status_operation_pb2 as change_status_operation_pb2,
)

ChangeStatusOperationPb2 = change_status_operation_pb2
ChangeStatusOperationEnum = change_status_operation_pb2.ChangeStatusOperationEnum

from google.ads.google_ads.v2.proto.enums import (
    change_status_resource_type_pb2 as change_status_resource_type_pb2,
)

ChangeStatusResourceTypePb2 = change_status_resource_type_pb2
ChangeStatusResourceTypeEnum = (
    change_status_resource_type_pb2.ChangeStatusResourceTypeEnum
)

from google.ads.google_ads.v2.proto.enums import click_type_pb2 as click_type_pb2

ClickTypePb2 = click_type_pb2
ClickTypeEnum = click_type_pb2.ClickTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    content_label_type_pb2 as content_label_type_pb2,
)

ContentLabelTypePb2 = content_label_type_pb2
ContentLabelTypeEnum = content_label_type_pb2.ContentLabelTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    conversion_action_category_pb2 as conversion_action_category_pb2,
)

ConversionActionCategoryPb2 = conversion_action_category_pb2
ConversionActionCategoryEnum = (
    conversion_action_category_pb2.ConversionActionCategoryEnum
)

from google.ads.google_ads.v2.proto.enums import (
    conversion_action_counting_type_pb2 as conversion_action_counting_type_pb2,
)

ConversionActionCountingTypePb2 = conversion_action_counting_type_pb2
ConversionActionCountingTypeEnum = (
    conversion_action_counting_type_pb2.ConversionActionCountingTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    conversion_action_status_pb2 as conversion_action_status_pb2,
)

ConversionActionStatusPb2 = conversion_action_status_pb2
ConversionActionStatusEnum = conversion_action_status_pb2.ConversionActionStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    conversion_action_type_pb2 as conversion_action_type_pb2,
)

ConversionActionTypePb2 = conversion_action_type_pb2
ConversionActionTypeEnum = conversion_action_type_pb2.ConversionActionTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    conversion_adjustment_type_pb2 as conversion_adjustment_type_pb2,
)

ConversionAdjustmentTypePb2 = conversion_adjustment_type_pb2
ConversionAdjustmentTypeEnum = (
    conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    conversion_attribution_event_type_pb2 as conversion_attribution_event_type_pb2,
)

ConversionAttributionEventTypePb2 = conversion_attribution_event_type_pb2
ConversionAttributionEventTypeEnum = (
    conversion_attribution_event_type_pb2.ConversionAttributionEventTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    conversion_lag_bucket_pb2 as conversion_lag_bucket_pb2,
)

ConversionLagBucketPb2 = conversion_lag_bucket_pb2
ConversionLagBucketEnum = conversion_lag_bucket_pb2.ConversionLagBucketEnum

from google.ads.google_ads.v2.proto.enums import (
    conversion_or_adjustment_lag_bucket_pb2 as conversion_or_adjustment_lag_bucket_pb2,
)

ConversionOrAdjustmentLagBucketPb2 = conversion_or_adjustment_lag_bucket_pb2
ConversionOrAdjustmentLagBucketEnum = (
    conversion_or_adjustment_lag_bucket_pb2.ConversionOrAdjustmentLagBucketEnum
)

from google.ads.google_ads.v2.proto.enums import (
    criterion_category_channel_availability_mode_pb2 as criterion_category_channel_availability_mode_pb2,
)

CriterionCategoryChannelAvailabilityModePb2 = (
    criterion_category_channel_availability_mode_pb2
)
CriterionCategoryChannelAvailabilityModeEnum = (
    criterion_category_channel_availability_mode_pb2.CriterionCategoryChannelAvailabilityModeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    criterion_category_locale_availability_mode_pb2 as criterion_category_locale_availability_mode_pb2,
)

CriterionCategoryLocaleAvailabilityModePb2 = (
    criterion_category_locale_availability_mode_pb2
)
CriterionCategoryLocaleAvailabilityModeEnum = (
    criterion_category_locale_availability_mode_pb2.CriterionCategoryLocaleAvailabilityModeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    criterion_system_serving_status_pb2 as criterion_system_serving_status_pb2,
)

CriterionSystemServingStatusPb2 = criterion_system_serving_status_pb2
CriterionSystemServingStatusEnum = (
    criterion_system_serving_status_pb2.CriterionSystemServingStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    criterion_type_pb2 as criterion_type_pb2,
)

CriterionTypePb2 = criterion_type_pb2
CriterionTypeEnum = criterion_type_pb2.CriterionTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    custom_interest_member_type_pb2 as custom_interest_member_type_pb2,
)

CustomInterestMemberTypePb2 = custom_interest_member_type_pb2
CustomInterestMemberTypeEnum = (
    custom_interest_member_type_pb2.CustomInterestMemberTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    custom_interest_status_pb2 as custom_interest_status_pb2,
)

CustomInterestStatusPb2 = custom_interest_status_pb2
CustomInterestStatusEnum = custom_interest_status_pb2.CustomInterestStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    custom_interest_type_pb2 as custom_interest_type_pb2,
)

CustomInterestTypePb2 = custom_interest_type_pb2
CustomInterestTypeEnum = custom_interest_type_pb2.CustomInterestTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    custom_placeholder_field_pb2 as custom_placeholder_field_pb2,
)

CustomPlaceholderFieldPb2 = custom_placeholder_field_pb2
CustomPlaceholderFieldEnum = custom_placeholder_field_pb2.CustomPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    customer_match_upload_key_type_pb2 as customer_match_upload_key_type_pb2,
)

CustomerMatchUploadKeyTypePb2 = customer_match_upload_key_type_pb2
CustomerMatchUploadKeyTypeEnum = (
    customer_match_upload_key_type_pb2.CustomerMatchUploadKeyTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    customer_pay_per_conversion_eligibility_failure_reason_pb2 as customer_pay_per_conversion_eligibility_failure_reason_pb2,
)

CustomerPayPerConversionEligibilityFailureReasonPb2 = (
    customer_pay_per_conversion_eligibility_failure_reason_pb2
)
CustomerPayPerConversionEligibilityFailureReasonEnum = (
    customer_pay_per_conversion_eligibility_failure_reason_pb2.CustomerPayPerConversionEligibilityFailureReasonEnum
)

from google.ads.google_ads.v2.proto.enums import (
    data_driven_model_status_pb2 as data_driven_model_status_pb2,
)

DataDrivenModelStatusPb2 = data_driven_model_status_pb2
DataDrivenModelStatusEnum = data_driven_model_status_pb2.DataDrivenModelStatusEnum

from google.ads.google_ads.v2.proto.enums import day_of_week_pb2 as day_of_week_pb2

DayOfWeekPb2 = day_of_week_pb2
DayOfWeekEnum = day_of_week_pb2.DayOfWeekEnum

from google.ads.google_ads.v2.proto.enums import device_pb2 as device_pb2

DevicePb2 = device_pb2
DeviceEnum = device_pb2.DeviceEnum

from google.ads.google_ads.v2.proto.enums import (
    display_ad_format_setting_pb2 as display_ad_format_setting_pb2,
)

DisplayAdFormatSettingPb2 = display_ad_format_setting_pb2
DisplayAdFormatSettingEnum = display_ad_format_setting_pb2.DisplayAdFormatSettingEnum

from google.ads.google_ads.v2.proto.enums import (
    display_upload_product_type_pb2 as display_upload_product_type_pb2,
)

DisplayUploadProductTypePb2 = display_upload_product_type_pb2
DisplayUploadProductTypeEnum = (
    display_upload_product_type_pb2.DisplayUploadProductTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    distance_bucket_pb2 as distance_bucket_pb2,
)

DistanceBucketPb2 = distance_bucket_pb2
DistanceBucketEnum = distance_bucket_pb2.DistanceBucketEnum

from google.ads.google_ads.v2.proto.enums import (
    dsa_page_feed_criterion_field_pb2 as dsa_page_feed_criterion_field_pb2,
)

DsaPageFeedCriterionFieldPb2 = dsa_page_feed_criterion_field_pb2
DsaPageFeedCriterionFieldEnum = (
    dsa_page_feed_criterion_field_pb2.DsaPageFeedCriterionFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    education_placeholder_field_pb2 as education_placeholder_field_pb2,
)

EducationPlaceholderFieldPb2 = education_placeholder_field_pb2
EducationPlaceholderFieldEnum = (
    education_placeholder_field_pb2.EducationPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    extension_setting_device_pb2 as extension_setting_device_pb2,
)

ExtensionSettingDevicePb2 = extension_setting_device_pb2
ExtensionSettingDeviceEnum = extension_setting_device_pb2.ExtensionSettingDeviceEnum

from google.ads.google_ads.v2.proto.enums import (
    extension_type_pb2 as extension_type_pb2,
)

ExtensionTypePb2 = extension_type_pb2
ExtensionTypeEnum = extension_type_pb2.ExtensionTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    external_conversion_source_pb2 as external_conversion_source_pb2,
)

ExternalConversionSourcePb2 = external_conversion_source_pb2
ExternalConversionSourceEnum = (
    external_conversion_source_pb2.ExternalConversionSourceEnum
)

from google.ads.google_ads.v2.proto.enums import (
    feed_attribute_type_pb2 as feed_attribute_type_pb2,
)

FeedAttributeTypePb2 = feed_attribute_type_pb2
FeedAttributeTypeEnum = feed_attribute_type_pb2.FeedAttributeTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    feed_item_quality_approval_status_pb2 as feed_item_quality_approval_status_pb2,
)

FeedItemQualityApprovalStatusPb2 = feed_item_quality_approval_status_pb2
FeedItemQualityApprovalStatusEnum = (
    feed_item_quality_approval_status_pb2.FeedItemQualityApprovalStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    feed_item_quality_disapproval_reason_pb2 as feed_item_quality_disapproval_reason_pb2,
)

FeedItemQualityDisapprovalReasonPb2 = feed_item_quality_disapproval_reason_pb2
FeedItemQualityDisapprovalReasonEnum = (
    feed_item_quality_disapproval_reason_pb2.FeedItemQualityDisapprovalReasonEnum
)

from google.ads.google_ads.v2.proto.enums import (
    feed_item_status_pb2 as feed_item_status_pb2,
)

FeedItemStatusPb2 = feed_item_status_pb2
FeedItemStatusEnum = feed_item_status_pb2.FeedItemStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    feed_item_target_device_pb2 as feed_item_target_device_pb2,
)

FeedItemTargetDevicePb2 = feed_item_target_device_pb2
FeedItemTargetDeviceEnum = feed_item_target_device_pb2.FeedItemTargetDeviceEnum

from google.ads.google_ads.v2.proto.enums import (
    feed_item_target_status_pb2 as feed_item_target_status_pb2,
)

FeedItemTargetStatusPb2 = feed_item_target_status_pb2

from google.ads.google_ads.v2.proto.enums import (
    feed_item_target_type_pb2 as feed_item_target_type_pb2,
)

FeedItemTargetTypePb2 = feed_item_target_type_pb2
FeedItemTargetTypeEnum = feed_item_target_type_pb2.FeedItemTargetTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    feed_item_validation_status_pb2 as feed_item_validation_status_pb2,
)

FeedItemValidationStatusPb2 = feed_item_validation_status_pb2
FeedItemValidationStatusEnum = (
    feed_item_validation_status_pb2.FeedItemValidationStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    feed_link_status_pb2 as feed_link_status_pb2,
)

FeedLinkStatusPb2 = feed_link_status_pb2
FeedLinkStatusEnum = feed_link_status_pb2.FeedLinkStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    feed_mapping_criterion_type_pb2 as feed_mapping_criterion_type_pb2,
)

FeedMappingCriterionTypePb2 = feed_mapping_criterion_type_pb2
FeedMappingCriterionTypeEnum = (
    feed_mapping_criterion_type_pb2.FeedMappingCriterionTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    feed_mapping_status_pb2 as feed_mapping_status_pb2,
)

FeedMappingStatusPb2 = feed_mapping_status_pb2
FeedMappingStatusEnum = feed_mapping_status_pb2.FeedMappingStatusEnum

from google.ads.google_ads.v2.proto.enums import feed_origin_pb2 as feed_origin_pb2

FeedOriginPb2 = feed_origin_pb2
FeedOriginEnum = feed_origin_pb2.FeedOriginEnum

from google.ads.google_ads.v2.proto.enums import feed_status_pb2 as feed_status_pb2

FeedStatusPb2 = feed_status_pb2
FeedStatusEnum = feed_status_pb2.FeedStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    flight_placeholder_field_pb2 as flight_placeholder_field_pb2,
)

FlightPlaceholderFieldPb2 = flight_placeholder_field_pb2
FlightPlaceholderFieldEnum = flight_placeholder_field_pb2.FlightPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    frequency_cap_event_type_pb2 as frequency_cap_event_type_pb2,
)

FrequencyCapEventTypePb2 = frequency_cap_event_type_pb2
FrequencyCapEventTypeEnum = frequency_cap_event_type_pb2.FrequencyCapEventTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    frequency_cap_level_pb2 as frequency_cap_level_pb2,
)

FrequencyCapLevelPb2 = frequency_cap_level_pb2
FrequencyCapLevelEnum = frequency_cap_level_pb2.FrequencyCapLevelEnum

from google.ads.google_ads.v2.proto.enums import (
    frequency_cap_time_unit_pb2 as frequency_cap_time_unit_pb2,
)

FrequencyCapTimeUnitPb2 = frequency_cap_time_unit_pb2
FrequencyCapTimeUnitEnum = frequency_cap_time_unit_pb2.FrequencyCapTimeUnitEnum

from google.ads.google_ads.v2.proto.enums import gender_type_pb2 as gender_type_pb2

GenderTypePb2 = gender_type_pb2
GenderTypeEnum = gender_type_pb2.GenderTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    geo_target_constant_status_pb2 as geo_target_constant_status_pb2,
)

GeoTargetConstantStatusPb2 = geo_target_constant_status_pb2
GeoTargetConstantStatusEnum = geo_target_constant_status_pb2.GeoTargetConstantStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    geo_targeting_restriction_pb2 as geo_targeting_restriction_pb2,
)

GeoTargetingRestrictionPb2 = geo_targeting_restriction_pb2
GeoTargetingRestrictionEnum = geo_targeting_restriction_pb2.GeoTargetingRestrictionEnum

from google.ads.google_ads.v2.proto.enums import (
    geo_targeting_type_pb2 as geo_targeting_type_pb2,
)

GeoTargetingTypePb2 = geo_targeting_type_pb2
GeoTargetingTypeEnum = geo_targeting_type_pb2.GeoTargetingTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    google_ads_field_category_pb2 as google_ads_field_category_pb2,
)

GoogleAdsFieldCategoryPb2 = google_ads_field_category_pb2
GoogleAdsFieldCategoryEnum = google_ads_field_category_pb2.GoogleAdsFieldCategoryEnum

from google.ads.google_ads.v2.proto.enums import (
    google_ads_field_data_type_pb2 as google_ads_field_data_type_pb2,
)

GoogleAdsFieldDataTypePb2 = google_ads_field_data_type_pb2
GoogleAdsFieldDataTypeEnum = google_ads_field_data_type_pb2.GoogleAdsFieldDataTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    hotel_date_selection_type_pb2 as hotel_date_selection_type_pb2,
)

HotelDateSelectionTypePb2 = hotel_date_selection_type_pb2
HotelDateSelectionTypeEnum = hotel_date_selection_type_pb2.HotelDateSelectionTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    hotel_placeholder_field_pb2 as hotel_placeholder_field_pb2,
)

HotelPlaceholderFieldPb2 = hotel_placeholder_field_pb2
HotelPlaceholderFieldEnum = hotel_placeholder_field_pb2.HotelPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    hotel_price_bucket_pb2 as hotel_price_bucket_pb2,
)

HotelPriceBucketPb2 = hotel_price_bucket_pb2
HotelPriceBucketEnum = hotel_price_bucket_pb2.HotelPriceBucketEnum

from google.ads.google_ads.v2.proto.enums import (
    hotel_rate_type_pb2 as hotel_rate_type_pb2,
)

HotelRateTypePb2 = hotel_rate_type_pb2
HotelRateTypeEnum = hotel_rate_type_pb2.HotelRateTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    income_range_type_pb2 as income_range_type_pb2,
)

IncomeRangeTypePb2 = income_range_type_pb2
IncomeRangeTypeEnum = income_range_type_pb2.IncomeRangeTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    interaction_event_type_pb2 as interaction_event_type_pb2,
)

InteractionEventTypePb2 = interaction_event_type_pb2
InteractionEventTypeEnum = interaction_event_type_pb2.InteractionEventTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    interaction_type_pb2 as interaction_type_pb2,
)

InteractionTypePb2 = interaction_type_pb2
InteractionTypeEnum = interaction_type_pb2.InteractionTypeEnum

from google.ads.google_ads.v2.proto.enums import invoice_type_pb2 as invoice_type_pb2

InvoiceTypePb2 = invoice_type_pb2
InvoiceTypeEnum = invoice_type_pb2.InvoiceTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    job_placeholder_field_pb2 as job_placeholder_field_pb2,
)

JobPlaceholderFieldPb2 = job_placeholder_field_pb2
JobPlaceholderFieldEnum = job_placeholder_field_pb2.JobPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    keyword_match_type_pb2 as keyword_match_type_pb2,
)

KeywordMatchTypePb2 = keyword_match_type_pb2
KeywordMatchTypeEnum = keyword_match_type_pb2.KeywordMatchTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    keyword_plan_competition_level_pb2 as keyword_plan_competition_level_pb2,
)

KeywordPlanCompetitionLevelPb2 = keyword_plan_competition_level_pb2
KeywordPlanCompetitionLevelEnum = (
    keyword_plan_competition_level_pb2.KeywordPlanCompetitionLevelEnum
)

from google.ads.google_ads.v2.proto.enums import (
    keyword_plan_forecast_interval_pb2 as keyword_plan_forecast_interval_pb2,
)

KeywordPlanForecastIntervalPb2 = keyword_plan_forecast_interval_pb2
KeywordPlanForecastIntervalEnum = (
    keyword_plan_forecast_interval_pb2.KeywordPlanForecastIntervalEnum
)

from google.ads.google_ads.v2.proto.enums import (
    keyword_plan_network_pb2 as keyword_plan_network_pb2,
)

KeywordPlanNetworkPb2 = keyword_plan_network_pb2
KeywordPlanNetworkEnum = keyword_plan_network_pb2.KeywordPlanNetworkEnum

from google.ads.google_ads.v2.proto.enums import label_status_pb2 as label_status_pb2

LabelStatusPb2 = label_status_pb2
LabelStatusEnum = label_status_pb2.LabelStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    legacy_app_install_ad_app_store_pb2 as legacy_app_install_ad_app_store_pb2,
)

LegacyAppInstallAdAppStorePb2 = legacy_app_install_ad_app_store_pb2
LegacyAppInstallAdAppStoreEnum = (
    legacy_app_install_ad_app_store_pb2.LegacyAppInstallAdAppStoreEnum
)

from google.ads.google_ads.v2.proto.enums import (
    listing_custom_attribute_index_pb2 as listing_custom_attribute_index_pb2,
)

ListingCustomAttributeIndexPb2 = listing_custom_attribute_index_pb2
ListingCustomAttributeIndexEnum = (
    listing_custom_attribute_index_pb2.ListingCustomAttributeIndexEnum
)

from google.ads.google_ads.v2.proto.enums import (
    listing_group_type_pb2 as listing_group_type_pb2,
)

ListingGroupTypePb2 = listing_group_type_pb2
ListingGroupTypeEnum = listing_group_type_pb2.ListingGroupTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    local_placeholder_field_pb2 as local_placeholder_field_pb2,
)

LocalPlaceholderFieldPb2 = local_placeholder_field_pb2
LocalPlaceholderFieldEnum = local_placeholder_field_pb2.LocalPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    location_extension_targeting_criterion_field_pb2 as location_extension_targeting_criterion_field_pb2,
)

LocationExtensionTargetingCriterionFieldPb2 = (
    location_extension_targeting_criterion_field_pb2
)
LocationExtensionTargetingCriterionFieldEnum = (
    location_extension_targeting_criterion_field_pb2.LocationExtensionTargetingCriterionFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    location_group_radius_units_pb2 as location_group_radius_units_pb2,
)

LocationGroupRadiusUnitsPb2 = location_group_radius_units_pb2
LocationGroupRadiusUnitsEnum = (
    location_group_radius_units_pb2.LocationGroupRadiusUnitsEnum
)

from google.ads.google_ads.v2.proto.enums import (
    location_placeholder_field_pb2 as location_placeholder_field_pb2,
)

LocationPlaceholderFieldPb2 = location_placeholder_field_pb2
LocationPlaceholderFieldEnum = (
    location_placeholder_field_pb2.LocationPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    location_source_type_pb2 as location_source_type_pb2,
)

LocationSourceTypePb2 = location_source_type_pb2

from google.ads.google_ads.v2.proto.enums import (
    manager_link_status_pb2 as manager_link_status_pb2,
)

ManagerLinkStatusPb2 = manager_link_status_pb2
ManagerLinkStatusEnum = manager_link_status_pb2.ManagerLinkStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    matching_function_context_type_pb2 as matching_function_context_type_pb2,
)

MatchingFunctionContextTypePb2 = matching_function_context_type_pb2
MatchingFunctionContextTypeEnum = (
    matching_function_context_type_pb2.MatchingFunctionContextTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    matching_function_operator_pb2 as matching_function_operator_pb2,
)

MatchingFunctionOperatorPb2 = matching_function_operator_pb2
MatchingFunctionOperatorEnum = (
    matching_function_operator_pb2.MatchingFunctionOperatorEnum
)

from google.ads.google_ads.v2.proto.enums import media_type_pb2 as media_type_pb2

MediaTypePb2 = media_type_pb2
MediaTypeEnum = media_type_pb2.MediaTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    merchant_center_link_status_pb2 as merchant_center_link_status_pb2,
)

MerchantCenterLinkStatusPb2 = merchant_center_link_status_pb2
MerchantCenterLinkStatusEnum = (
    merchant_center_link_status_pb2.MerchantCenterLinkStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    message_placeholder_field_pb2 as message_placeholder_field_pb2,
)

MessagePlaceholderFieldPb2 = message_placeholder_field_pb2
MessagePlaceholderFieldEnum = message_placeholder_field_pb2.MessagePlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import mime_type_pb2 as mime_type_pb2

MimeTypePb2 = mime_type_pb2
MimeTypeEnum = mime_type_pb2.MimeTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    minute_of_hour_pb2 as minute_of_hour_pb2,
)

MinuteOfHourPb2 = minute_of_hour_pb2
MinuteOfHourEnum = minute_of_hour_pb2.MinuteOfHourEnum

from google.ads.google_ads.v2.proto.enums import (
    mobile_device_type_pb2 as mobile_device_type_pb2,
)

MobileDeviceTypePb2 = mobile_device_type_pb2
MobileDeviceTypeEnum = mobile_device_type_pb2.MobileDeviceTypeEnum

from google.ads.google_ads.v2.proto.enums import month_of_year_pb2 as month_of_year_pb2

MonthOfYearPb2 = month_of_year_pb2
MonthOfYearEnum = month_of_year_pb2.MonthOfYearEnum

from google.ads.google_ads.v2.proto.enums import (
    mutate_job_status_pb2 as mutate_job_status_pb2,
)

MutateJobStatusPb2 = mutate_job_status_pb2
MutateJobStatusEnum = mutate_job_status_pb2.MutateJobStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    negative_geo_target_type_pb2 as negative_geo_target_type_pb2,
)

NegativeGeoTargetTypePb2 = negative_geo_target_type_pb2
NegativeGeoTargetTypeEnum = negative_geo_target_type_pb2.NegativeGeoTargetTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    offline_user_data_job_failure_reason_pb2 as offline_user_data_job_failure_reason_pb2,
)

OfflineUserDataJobFailureReasonPb2 = offline_user_data_job_failure_reason_pb2

from google.ads.google_ads.v2.proto.enums import (
    offline_user_data_job_status_pb2 as offline_user_data_job_status_pb2,
)

OfflineUserDataJobStatusPb2 = offline_user_data_job_status_pb2

from google.ads.google_ads.v2.proto.enums import (
    offline_user_data_job_type_pb2 as offline_user_data_job_type_pb2,
)

OfflineUserDataJobTypePb2 = offline_user_data_job_type_pb2

from google.ads.google_ads.v2.proto.enums import (
    operating_system_version_operator_type_pb2 as operating_system_version_operator_type_pb2,
)

OperatingSystemVersionOperatorTypePb2 = operating_system_version_operator_type_pb2
OperatingSystemVersionOperatorTypeEnum = (
    operating_system_version_operator_type_pb2.OperatingSystemVersionOperatorTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    page_one_promoted_strategy_goal_pb2 as page_one_promoted_strategy_goal_pb2,
)

PageOnePromotedStrategyGoalPb2 = page_one_promoted_strategy_goal_pb2
PageOnePromotedStrategyGoalEnum = (
    page_one_promoted_strategy_goal_pb2.PageOnePromotedStrategyGoalEnum
)

from google.ads.google_ads.v2.proto.enums import (
    parental_status_type_pb2 as parental_status_type_pb2,
)

ParentalStatusTypePb2 = parental_status_type_pb2
ParentalStatusTypeEnum = parental_status_type_pb2.ParentalStatusTypeEnum

from google.ads.google_ads.v2.proto.enums import payment_mode_pb2 as payment_mode_pb2

PaymentModePb2 = payment_mode_pb2
PaymentModeEnum = payment_mode_pb2.PaymentModeEnum

from google.ads.google_ads.v2.proto.enums import (
    placeholder_type_pb2 as placeholder_type_pb2,
)

PlaceholderTypePb2 = placeholder_type_pb2
PlaceholderTypeEnum = placeholder_type_pb2.PlaceholderTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    placement_type_pb2 as placement_type_pb2,
)

PlacementTypePb2 = placement_type_pb2
PlacementTypeEnum = placement_type_pb2.PlacementTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    policy_approval_status_pb2 as policy_approval_status_pb2,
)

PolicyApprovalStatusPb2 = policy_approval_status_pb2
PolicyApprovalStatusEnum = policy_approval_status_pb2.PolicyApprovalStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    policy_review_status_pb2 as policy_review_status_pb2,
)

PolicyReviewStatusPb2 = policy_review_status_pb2
PolicyReviewStatusEnum = policy_review_status_pb2.PolicyReviewStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    policy_topic_entry_type_pb2 as policy_topic_entry_type_pb2,
)

PolicyTopicEntryTypePb2 = policy_topic_entry_type_pb2
PolicyTopicEntryTypeEnum = policy_topic_entry_type_pb2.PolicyTopicEntryTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    policy_topic_evidence_destination_mismatch_url_type_pb2 as policy_topic_evidence_destination_mismatch_url_type_pb2,
)

PolicyTopicEvidenceDestinationMismatchUrlTypePb2 = (
    policy_topic_evidence_destination_mismatch_url_type_pb2
)
PolicyTopicEvidenceDestinationMismatchUrlTypeEnum = (
    policy_topic_evidence_destination_mismatch_url_type_pb2.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    policy_topic_evidence_destination_not_working_device_pb2 as policy_topic_evidence_destination_not_working_device_pb2,
)

PolicyTopicEvidenceDestinationNotWorkingDevicePb2 = (
    policy_topic_evidence_destination_not_working_device_pb2
)
PolicyTopicEvidenceDestinationNotWorkingDeviceEnum = (
    policy_topic_evidence_destination_not_working_device_pb2.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum
)

from google.ads.google_ads.v2.proto.enums import (
    policy_topic_evidence_destination_not_working_dns_error_type_pb2 as policy_topic_evidence_destination_not_working_dns_error_type_pb2,
)

PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypePb2 = (
    policy_topic_evidence_destination_not_working_dns_error_type_pb2
)
PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum = (
    policy_topic_evidence_destination_not_working_dns_error_type_pb2.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    positive_geo_target_type_pb2 as positive_geo_target_type_pb2,
)

PositiveGeoTargetTypePb2 = positive_geo_target_type_pb2
PositiveGeoTargetTypeEnum = positive_geo_target_type_pb2.PositiveGeoTargetTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    preferred_content_type_pb2 as preferred_content_type_pb2,
)

PreferredContentTypePb2 = preferred_content_type_pb2
PreferredContentTypeEnum = preferred_content_type_pb2.PreferredContentTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    price_extension_price_qualifier_pb2 as price_extension_price_qualifier_pb2,
)

PriceExtensionPriceQualifierPb2 = price_extension_price_qualifier_pb2
PriceExtensionPriceQualifierEnum = (
    price_extension_price_qualifier_pb2.PriceExtensionPriceQualifierEnum
)

from google.ads.google_ads.v2.proto.enums import (
    price_extension_price_unit_pb2 as price_extension_price_unit_pb2,
)

PriceExtensionPriceUnitPb2 = price_extension_price_unit_pb2
PriceExtensionPriceUnitEnum = price_extension_price_unit_pb2.PriceExtensionPriceUnitEnum

from google.ads.google_ads.v2.proto.enums import (
    price_extension_type_pb2 as price_extension_type_pb2,
)

PriceExtensionTypePb2 = price_extension_type_pb2
PriceExtensionTypeEnum = price_extension_type_pb2.PriceExtensionTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    price_placeholder_field_pb2 as price_placeholder_field_pb2,
)

PricePlaceholderFieldPb2 = price_placeholder_field_pb2
PricePlaceholderFieldEnum = price_placeholder_field_pb2.PricePlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    product_bidding_category_level_pb2 as product_bidding_category_level_pb2,
)

ProductBiddingCategoryLevelPb2 = product_bidding_category_level_pb2
ProductBiddingCategoryLevelEnum = (
    product_bidding_category_level_pb2.ProductBiddingCategoryLevelEnum
)

from google.ads.google_ads.v2.proto.enums import (
    product_bidding_category_status_pb2 as product_bidding_category_status_pb2,
)

ProductBiddingCategoryStatusPb2 = product_bidding_category_status_pb2
ProductBiddingCategoryStatusEnum = (
    product_bidding_category_status_pb2.ProductBiddingCategoryStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    product_channel_exclusivity_pb2 as product_channel_exclusivity_pb2,
)

ProductChannelExclusivityPb2 = product_channel_exclusivity_pb2
ProductChannelExclusivityEnum = (
    product_channel_exclusivity_pb2.ProductChannelExclusivityEnum
)

from google.ads.google_ads.v2.proto.enums import (
    product_channel_pb2 as product_channel_pb2,
)

ProductChannelPb2 = product_channel_pb2
ProductChannelEnum = product_channel_pb2.ProductChannelEnum

from google.ads.google_ads.v2.proto.enums import (
    product_condition_pb2 as product_condition_pb2,
)

ProductConditionPb2 = product_condition_pb2
ProductConditionEnum = product_condition_pb2.ProductConditionEnum

from google.ads.google_ads.v2.proto.enums import (
    product_type_level_pb2 as product_type_level_pb2,
)

ProductTypeLevelPb2 = product_type_level_pb2
ProductTypeLevelEnum = product_type_level_pb2.ProductTypeLevelEnum

from google.ads.google_ads.v2.proto.enums import (
    promotion_extension_discount_modifier_pb2 as promotion_extension_discount_modifier_pb2,
)

PromotionExtensionDiscountModifierPb2 = promotion_extension_discount_modifier_pb2
PromotionExtensionDiscountModifierEnum = (
    promotion_extension_discount_modifier_pb2.PromotionExtensionDiscountModifierEnum
)

from google.ads.google_ads.v2.proto.enums import (
    promotion_extension_occasion_pb2 as promotion_extension_occasion_pb2,
)

PromotionExtensionOccasionPb2 = promotion_extension_occasion_pb2
PromotionExtensionOccasionEnum = (
    promotion_extension_occasion_pb2.PromotionExtensionOccasionEnum
)

from google.ads.google_ads.v2.proto.enums import (
    promotion_placeholder_field_pb2 as promotion_placeholder_field_pb2,
)

PromotionPlaceholderFieldPb2 = promotion_placeholder_field_pb2
PromotionPlaceholderFieldEnum = (
    promotion_placeholder_field_pb2.PromotionPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    proximity_radius_units_pb2 as proximity_radius_units_pb2,
)

ProximityRadiusUnitsPb2 = proximity_radius_units_pb2
ProximityRadiusUnitsEnum = proximity_radius_units_pb2.ProximityRadiusUnitsEnum

from google.ads.google_ads.v2.proto.enums import (
    quality_score_bucket_pb2 as quality_score_bucket_pb2,
)

QualityScoreBucketPb2 = quality_score_bucket_pb2
QualityScoreBucketEnum = quality_score_bucket_pb2.QualityScoreBucketEnum

from google.ads.google_ads.v2.proto.enums import (
    reach_plan_ad_length_pb2 as reach_plan_ad_length_pb2,
)

ReachPlanAdLengthPb2 = reach_plan_ad_length_pb2
ReachPlanAdLengthEnum = reach_plan_ad_length_pb2.ReachPlanAdLengthEnum

from google.ads.google_ads.v2.proto.enums import (
    reach_plan_age_range_pb2 as reach_plan_age_range_pb2,
)

ReachPlanAgeRangePb2 = reach_plan_age_range_pb2
ReachPlanAgeRangeEnum = reach_plan_age_range_pb2.ReachPlanAgeRangeEnum

from google.ads.google_ads.v2.proto.enums import (
    real_estate_placeholder_field_pb2 as real_estate_placeholder_field_pb2,
)

RealEstatePlaceholderFieldPb2 = real_estate_placeholder_field_pb2
RealEstatePlaceholderFieldEnum = (
    real_estate_placeholder_field_pb2.RealEstatePlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    recommendation_type_pb2 as recommendation_type_pb2,
)

RecommendationTypePb2 = recommendation_type_pb2
RecommendationTypeEnum = recommendation_type_pb2.RecommendationTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    search_engine_results_page_type_pb2 as search_engine_results_page_type_pb2,
)

SearchEngineResultsPageTypePb2 = search_engine_results_page_type_pb2
SearchEngineResultsPageTypeEnum = (
    search_engine_results_page_type_pb2.SearchEngineResultsPageTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    search_term_match_type_pb2 as search_term_match_type_pb2,
)

SearchTermMatchTypePb2 = search_term_match_type_pb2
SearchTermMatchTypeEnum = search_term_match_type_pb2.SearchTermMatchTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    search_term_targeting_status_pb2 as search_term_targeting_status_pb2,
)

SearchTermTargetingStatusPb2 = search_term_targeting_status_pb2
SearchTermTargetingStatusEnum = (
    search_term_targeting_status_pb2.SearchTermTargetingStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    served_asset_field_type_pb2 as served_asset_field_type_pb2,
)

ServedAssetFieldTypePb2 = served_asset_field_type_pb2
ServedAssetFieldTypeEnum = served_asset_field_type_pb2.ServedAssetFieldTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    shared_set_status_pb2 as shared_set_status_pb2,
)

SharedSetStatusPb2 = shared_set_status_pb2
SharedSetStatusEnum = shared_set_status_pb2.SharedSetStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    shared_set_type_pb2 as shared_set_type_pb2,
)

SharedSetTypePb2 = shared_set_type_pb2
SharedSetTypeEnum = shared_set_type_pb2.SharedSetTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    simulation_modification_method_pb2 as simulation_modification_method_pb2,
)

SimulationModificationMethodPb2 = simulation_modification_method_pb2
SimulationModificationMethodEnum = (
    simulation_modification_method_pb2.SimulationModificationMethodEnum
)

from google.ads.google_ads.v2.proto.enums import (
    simulation_type_pb2 as simulation_type_pb2,
)

SimulationTypePb2 = simulation_type_pb2
SimulationTypeEnum = simulation_type_pb2.SimulationTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    sitelink_placeholder_field_pb2 as sitelink_placeholder_field_pb2,
)

SitelinkPlaceholderFieldPb2 = sitelink_placeholder_field_pb2
SitelinkPlaceholderFieldEnum = (
    sitelink_placeholder_field_pb2.SitelinkPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import slot_pb2 as slot_pb2

SlotPb2 = slot_pb2
SlotEnum = slot_pb2.SlotEnum

from google.ads.google_ads.v2.proto.enums import (
    spending_limit_type_pb2 as spending_limit_type_pb2,
)

SpendingLimitTypePb2 = spending_limit_type_pb2
SpendingLimitTypeEnum = spending_limit_type_pb2.SpendingLimitTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    structured_snippet_placeholder_field_pb2 as structured_snippet_placeholder_field_pb2,
)

StructuredSnippetPlaceholderFieldPb2 = structured_snippet_placeholder_field_pb2
StructuredSnippetPlaceholderFieldEnum = (
    structured_snippet_placeholder_field_pb2.StructuredSnippetPlaceholderFieldEnum
)

from google.ads.google_ads.v2.proto.enums import (
    summary_row_setting_pb2 as summary_row_setting_pb2,
)

SummaryRowSettingPb2 = summary_row_setting_pb2

from google.ads.google_ads.v2.proto.enums import (
    system_managed_entity_source_pb2 as system_managed_entity_source_pb2,
)

SystemManagedEntitySourcePb2 = system_managed_entity_source_pb2
SystemManagedResourceSourceEnum = (
    system_managed_entity_source_pb2.SystemManagedResourceSourceEnum
)

from google.ads.google_ads.v2.proto.enums import (
    target_cpa_opt_in_recommendation_goal_pb2 as target_cpa_opt_in_recommendation_goal_pb2,
)

TargetCpaOptInRecommendationGoalPb2 = target_cpa_opt_in_recommendation_goal_pb2
TargetCpaOptInRecommendationGoalEnum = (
    target_cpa_opt_in_recommendation_goal_pb2.TargetCpaOptInRecommendationGoalEnum
)

from google.ads.google_ads.v2.proto.enums import (
    target_impression_share_location_pb2 as target_impression_share_location_pb2,
)

TargetImpressionShareLocationPb2 = target_impression_share_location_pb2
TargetImpressionShareLocationEnum = (
    target_impression_share_location_pb2.TargetImpressionShareLocationEnum
)

from google.ads.google_ads.v2.proto.enums import (
    targeting_dimension_pb2 as targeting_dimension_pb2,
)

TargetingDimensionPb2 = targeting_dimension_pb2
TargetingDimensionEnum = targeting_dimension_pb2.TargetingDimensionEnum

from google.ads.google_ads.v2.proto.enums import time_type_pb2 as time_type_pb2

TimeTypePb2 = time_type_pb2
TimeTypeEnum = time_type_pb2.TimeTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    tracking_code_page_format_pb2 as tracking_code_page_format_pb2,
)

TrackingCodePageFormatPb2 = tracking_code_page_format_pb2
TrackingCodePageFormatEnum = tracking_code_page_format_pb2.TrackingCodePageFormatEnum

from google.ads.google_ads.v2.proto.enums import (
    tracking_code_type_pb2 as tracking_code_type_pb2,
)

TrackingCodeTypePb2 = tracking_code_type_pb2
TrackingCodeTypeEnum = tracking_code_type_pb2.TrackingCodeTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    travel_placeholder_field_pb2 as travel_placeholder_field_pb2,
)

TravelPlaceholderFieldPb2 = travel_placeholder_field_pb2
TravelPlaceholderFieldEnum = travel_placeholder_field_pb2.TravelPlaceholderFieldEnum

from google.ads.google_ads.v2.proto.enums import (
    user_interest_taxonomy_type_pb2 as user_interest_taxonomy_type_pb2,
)

UserInterestTaxonomyTypePb2 = user_interest_taxonomy_type_pb2
UserInterestTaxonomyTypeEnum = (
    user_interest_taxonomy_type_pb2.UserInterestTaxonomyTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_access_status_pb2 as user_list_access_status_pb2,
)

UserListAccessStatusPb2 = user_list_access_status_pb2
UserListAccessStatusEnum = user_list_access_status_pb2.UserListAccessStatusEnum

from google.ads.google_ads.v2.proto.enums import (
    user_list_closing_reason_pb2 as user_list_closing_reason_pb2,
)

UserListClosingReasonPb2 = user_list_closing_reason_pb2
UserListClosingReasonEnum = user_list_closing_reason_pb2.UserListClosingReasonEnum

from google.ads.google_ads.v2.proto.enums import (
    user_list_combined_rule_operator_pb2 as user_list_combined_rule_operator_pb2,
)

UserListCombinedRuleOperatorPb2 = user_list_combined_rule_operator_pb2
UserListCombinedRuleOperatorEnum = (
    user_list_combined_rule_operator_pb2.UserListCombinedRuleOperatorEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_crm_data_source_type_pb2 as user_list_crm_data_source_type_pb2,
)

UserListCrmDataSourceTypePb2 = user_list_crm_data_source_type_pb2
UserListCrmDataSourceTypeEnum = (
    user_list_crm_data_source_type_pb2.UserListCrmDataSourceTypeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_date_rule_item_operator_pb2 as user_list_date_rule_item_operator_pb2,
)

UserListDateRuleItemOperatorPb2 = user_list_date_rule_item_operator_pb2
UserListDateRuleItemOperatorEnum = (
    user_list_date_rule_item_operator_pb2.UserListDateRuleItemOperatorEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_logical_rule_operator_pb2 as user_list_logical_rule_operator_pb2,
)

UserListLogicalRuleOperatorPb2 = user_list_logical_rule_operator_pb2
UserListLogicalRuleOperatorEnum = (
    user_list_logical_rule_operator_pb2.UserListLogicalRuleOperatorEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_membership_status_pb2 as user_list_membership_status_pb2,
)

UserListMembershipStatusPb2 = user_list_membership_status_pb2
UserListMembershipStatusEnum = (
    user_list_membership_status_pb2.UserListMembershipStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_number_rule_item_operator_pb2 as user_list_number_rule_item_operator_pb2,
)

UserListNumberRuleItemOperatorPb2 = user_list_number_rule_item_operator_pb2
UserListNumberRuleItemOperatorEnum = (
    user_list_number_rule_item_operator_pb2.UserListNumberRuleItemOperatorEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_prepopulation_status_pb2 as user_list_prepopulation_status_pb2,
)

UserListPrepopulationStatusPb2 = user_list_prepopulation_status_pb2
UserListPrepopulationStatusEnum = (
    user_list_prepopulation_status_pb2.UserListPrepopulationStatusEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_rule_type_pb2 as user_list_rule_type_pb2,
)

UserListRuleTypePb2 = user_list_rule_type_pb2
UserListRuleTypeEnum = user_list_rule_type_pb2.UserListRuleTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    user_list_size_range_pb2 as user_list_size_range_pb2,
)

UserListSizeRangePb2 = user_list_size_range_pb2
UserListSizeRangeEnum = user_list_size_range_pb2.UserListSizeRangeEnum

from google.ads.google_ads.v2.proto.enums import (
    user_list_string_rule_item_operator_pb2 as user_list_string_rule_item_operator_pb2,
)

UserListStringRuleItemOperatorPb2 = user_list_string_rule_item_operator_pb2
UserListStringRuleItemOperatorEnum = (
    user_list_string_rule_item_operator_pb2.UserListStringRuleItemOperatorEnum
)

from google.ads.google_ads.v2.proto.enums import (
    user_list_type_pb2 as user_list_type_pb2,
)

UserListTypePb2 = user_list_type_pb2
UserListTypeEnum = user_list_type_pb2.UserListTypeEnum

from google.ads.google_ads.v2.proto.enums import (
    vanity_pharma_display_url_mode_pb2 as vanity_pharma_display_url_mode_pb2,
)

VanityPharmaDisplayUrlModePb2 = vanity_pharma_display_url_mode_pb2
VanityPharmaDisplayUrlModeEnum = (
    vanity_pharma_display_url_mode_pb2.VanityPharmaDisplayUrlModeEnum
)

from google.ads.google_ads.v2.proto.enums import (
    vanity_pharma_text_pb2 as vanity_pharma_text_pb2,
)

VanityPharmaTextPb2 = vanity_pharma_text_pb2
VanityPharmaTextEnum = vanity_pharma_text_pb2.VanityPharmaTextEnum

from google.ads.google_ads.v2.proto.enums import (
    webpage_condition_operand_pb2 as webpage_condition_operand_pb2,
)

WebpageConditionOperandPb2 = webpage_condition_operand_pb2
WebpageConditionOperandEnum = webpage_condition_operand_pb2.WebpageConditionOperandEnum

from google.ads.google_ads.v2.proto.enums import (
    webpage_condition_operator_pb2 as webpage_condition_operator_pb2,
)

WebpageConditionOperatorPb2 = webpage_condition_operator_pb2
WebpageConditionOperatorEnum = (
    webpage_condition_operator_pb2.WebpageConditionOperatorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    access_invitation_error_pb2 as access_invitation_error_pb2,
)

AccessInvitationErrorPb2 = access_invitation_error_pb2
AccessInvitationErrorEnum = access_invitation_error_pb2.AccessInvitationErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    account_budget_proposal_error_pb2 as account_budget_proposal_error_pb2,
)

AccountBudgetProposalErrorPb2 = account_budget_proposal_error_pb2
AccountBudgetProposalErrorEnum = (
    account_budget_proposal_error_pb2.AccountBudgetProposalErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    ad_customizer_error_pb2 as ad_customizer_error_pb2,
)

AdCustomizerErrorPb2 = ad_customizer_error_pb2
AdCustomizerErrorEnum = ad_customizer_error_pb2.AdCustomizerErrorEnum

from google.ads.google_ads.v2.proto.errors import ad_error_pb2 as ad_error_pb2

AdErrorPb2 = ad_error_pb2
AdErrorEnum = ad_error_pb2.AdErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    ad_group_ad_error_pb2 as ad_group_ad_error_pb2,
)

AdGroupAdErrorPb2 = ad_group_ad_error_pb2
AdGroupAdErrorEnum = ad_group_ad_error_pb2.AdGroupAdErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    ad_group_bid_modifier_error_pb2 as ad_group_bid_modifier_error_pb2,
)

AdGroupBidModifierErrorPb2 = ad_group_bid_modifier_error_pb2
AdGroupBidModifierErrorEnum = (
    ad_group_bid_modifier_error_pb2.AdGroupBidModifierErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    ad_group_criterion_error_pb2 as ad_group_criterion_error_pb2,
)

AdGroupCriterionErrorPb2 = ad_group_criterion_error_pb2
AdGroupCriterionErrorEnum = ad_group_criterion_error_pb2.AdGroupCriterionErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    ad_group_error_pb2 as ad_group_error_pb2,
)

AdGroupErrorPb2 = ad_group_error_pb2
AdGroupErrorEnum = ad_group_error_pb2.AdGroupErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    ad_group_feed_error_pb2 as ad_group_feed_error_pb2,
)

AdGroupFeedErrorPb2 = ad_group_feed_error_pb2
AdGroupFeedErrorEnum = ad_group_feed_error_pb2.AdGroupFeedErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    ad_parameter_error_pb2 as ad_parameter_error_pb2,
)

AdParameterErrorPb2 = ad_parameter_error_pb2
AdParameterErrorEnum = ad_parameter_error_pb2.AdParameterErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    ad_sharing_error_pb2 as ad_sharing_error_pb2,
)

AdSharingErrorPb2 = ad_sharing_error_pb2
AdSharingErrorEnum = ad_sharing_error_pb2.AdSharingErrorEnum

from google.ads.google_ads.v2.proto.errors import adx_error_pb2 as adx_error_pb2

AdxErrorPb2 = adx_error_pb2
AdxErrorEnum = adx_error_pb2.AdxErrorEnum

from google.ads.google_ads.v2.proto.errors import asset_error_pb2 as asset_error_pb2

AssetErrorPb2 = asset_error_pb2
AssetErrorEnum = asset_error_pb2.AssetErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    authentication_error_pb2 as authentication_error_pb2,
)

AuthenticationErrorPb2 = authentication_error_pb2
AuthenticationErrorEnum = authentication_error_pb2.AuthenticationErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    authorization_error_pb2 as authorization_error_pb2,
)

AuthorizationErrorPb2 = authorization_error_pb2
AuthorizationErrorEnum = authorization_error_pb2.AuthorizationErrorEnum

from google.ads.google_ads.v2.proto.errors import bidding_error_pb2 as bidding_error_pb2

BiddingErrorPb2 = bidding_error_pb2
BiddingErrorEnum = bidding_error_pb2.BiddingErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    bidding_strategy_error_pb2 as bidding_strategy_error_pb2,
)

BiddingStrategyErrorPb2 = bidding_strategy_error_pb2
BiddingStrategyErrorEnum = bidding_strategy_error_pb2.BiddingStrategyErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    billing_setup_error_pb2 as billing_setup_error_pb2,
)

BillingSetupErrorPb2 = billing_setup_error_pb2
BillingSetupErrorEnum = billing_setup_error_pb2.BillingSetupErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_budget_error_pb2 as campaign_budget_error_pb2,
)

CampaignBudgetErrorPb2 = campaign_budget_error_pb2
CampaignBudgetErrorEnum = campaign_budget_error_pb2.CampaignBudgetErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_criterion_error_pb2 as campaign_criterion_error_pb2,
)

CampaignCriterionErrorPb2 = campaign_criterion_error_pb2
CampaignCriterionErrorEnum = campaign_criterion_error_pb2.CampaignCriterionErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_draft_error_pb2 as campaign_draft_error_pb2,
)

CampaignDraftErrorPb2 = campaign_draft_error_pb2
CampaignDraftErrorEnum = campaign_draft_error_pb2.CampaignDraftErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_error_pb2 as campaign_error_pb2,
)

CampaignErrorPb2 = campaign_error_pb2
CampaignErrorEnum = campaign_error_pb2.CampaignErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_experiment_error_pb2 as campaign_experiment_error_pb2,
)

CampaignExperimentErrorPb2 = campaign_experiment_error_pb2
CampaignExperimentErrorEnum = campaign_experiment_error_pb2.CampaignExperimentErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_feed_error_pb2 as campaign_feed_error_pb2,
)

CampaignFeedErrorPb2 = campaign_feed_error_pb2
CampaignFeedErrorEnum = campaign_feed_error_pb2.CampaignFeedErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    campaign_shared_set_error_pb2 as campaign_shared_set_error_pb2,
)

CampaignSharedSetErrorPb2 = campaign_shared_set_error_pb2
CampaignSharedSetErrorEnum = campaign_shared_set_error_pb2.CampaignSharedSetErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    change_status_error_pb2 as change_status_error_pb2,
)

ChangeStatusErrorPb2 = change_status_error_pb2
ChangeStatusErrorEnum = change_status_error_pb2.ChangeStatusErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    click_view_error_pb2 as click_view_error_pb2,
)

ClickViewErrorPb2 = click_view_error_pb2

from google.ads.google_ads.v2.proto.errors import (
    collection_size_error_pb2 as collection_size_error_pb2,
)

CollectionSizeErrorPb2 = collection_size_error_pb2
CollectionSizeErrorEnum = collection_size_error_pb2.CollectionSizeErrorEnum

from google.ads.google_ads.v2.proto.errors import context_error_pb2 as context_error_pb2

ContextErrorPb2 = context_error_pb2
ContextErrorEnum = context_error_pb2.ContextErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    conversion_action_error_pb2 as conversion_action_error_pb2,
)

ConversionActionErrorPb2 = conversion_action_error_pb2
ConversionActionErrorEnum = conversion_action_error_pb2.ConversionActionErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    conversion_adjustment_upload_error_pb2 as conversion_adjustment_upload_error_pb2,
)

ConversionAdjustmentUploadErrorPb2 = conversion_adjustment_upload_error_pb2
ConversionAdjustmentUploadErrorEnum = (
    conversion_adjustment_upload_error_pb2.ConversionAdjustmentUploadErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    conversion_upload_error_pb2 as conversion_upload_error_pb2,
)

ConversionUploadErrorPb2 = conversion_upload_error_pb2
ConversionUploadErrorEnum = conversion_upload_error_pb2.ConversionUploadErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    country_code_error_pb2 as country_code_error_pb2,
)

CountryCodeErrorPb2 = country_code_error_pb2
CountryCodeErrorEnum = country_code_error_pb2.CountryCodeErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    criterion_error_pb2 as criterion_error_pb2,
)

CriterionErrorPb2 = criterion_error_pb2
CriterionErrorEnum = criterion_error_pb2.CriterionErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    currency_code_error_pb2 as currency_code_error_pb2,
)

CurrencyCodeErrorPb2 = currency_code_error_pb2
CurrencyCodeErrorEnum = currency_code_error_pb2.CurrencyCodeErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    custom_interest_error_pb2 as custom_interest_error_pb2,
)

CustomInterestErrorPb2 = custom_interest_error_pb2
CustomInterestErrorEnum = custom_interest_error_pb2.CustomInterestErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    customer_client_link_error_pb2 as customer_client_link_error_pb2,
)

CustomerClientLinkErrorPb2 = customer_client_link_error_pb2
CustomerClientLinkErrorEnum = customer_client_link_error_pb2.CustomerClientLinkErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    customer_error_pb2 as customer_error_pb2,
)

CustomerErrorPb2 = customer_error_pb2
CustomerErrorEnum = customer_error_pb2.CustomerErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    customer_feed_error_pb2 as customer_feed_error_pb2,
)

CustomerFeedErrorPb2 = customer_feed_error_pb2
CustomerFeedErrorEnum = customer_feed_error_pb2.CustomerFeedErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    customer_manager_link_error_pb2 as customer_manager_link_error_pb2,
)

CustomerManagerLinkErrorPb2 = customer_manager_link_error_pb2
CustomerManagerLinkErrorEnum = (
    customer_manager_link_error_pb2.CustomerManagerLinkErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    customer_negative_criterion_error_pb2 as customer_negative_criterion_error_pb2,
)

CustomerNegativeCriterionErrorPb2 = customer_negative_criterion_error_pb2

from google.ads.google_ads.v2.proto.errors import (
    database_error_pb2 as database_error_pb2,
)

DatabaseErrorPb2 = database_error_pb2
DatabaseErrorEnum = database_error_pb2.DatabaseErrorEnum

from google.ads.google_ads.v2.proto.errors import date_error_pb2 as date_error_pb2

DateErrorPb2 = date_error_pb2
DateErrorEnum = date_error_pb2.DateErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    date_range_error_pb2 as date_range_error_pb2,
)

DateRangeErrorPb2 = date_range_error_pb2
DateRangeErrorEnum = date_range_error_pb2.DateRangeErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    distinct_error_pb2 as distinct_error_pb2,
)

DistinctErrorPb2 = distinct_error_pb2
DistinctErrorEnum = distinct_error_pb2.DistinctErrorEnum

from google.ads.google_ads.v2.proto.errors import enum_error_pb2 as enum_error_pb2

EnumErrorPb2 = enum_error_pb2
EnumErrorEnum = enum_error_pb2.EnumErrorEnum

from google.ads.google_ads.v2.proto.errors import errors_pb2 as errors_pb2

ErrorsPb2 = errors_pb2
ErrorCode = errors_pb2.ErrorCode
ErrorDetails = errors_pb2.ErrorDetails
ErrorLocation = errors_pb2.ErrorLocation
GoogleAdsError = errors_pb2.GoogleAdsError
GoogleAdsFailure = errors_pb2.GoogleAdsFailure
PolicyFindingDetails = errors_pb2.PolicyFindingDetails
PolicyViolationDetails = errors_pb2.PolicyViolationDetails

from google.ads.google_ads.v2.proto.errors import (
    experiment_error_pb2 as experiment_error_pb2,
)

ExperimentErrorPb2 = experiment_error_pb2

from google.ads.google_ads.v2.proto.errors import (
    extension_feed_item_error_pb2 as extension_feed_item_error_pb2,
)

ExtensionFeedItemErrorPb2 = extension_feed_item_error_pb2
ExtensionFeedItemErrorEnum = extension_feed_item_error_pb2.ExtensionFeedItemErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    extension_setting_error_pb2 as extension_setting_error_pb2,
)

ExtensionSettingErrorPb2 = extension_setting_error_pb2
ExtensionSettingErrorEnum = extension_setting_error_pb2.ExtensionSettingErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    feed_attribute_reference_error_pb2 as feed_attribute_reference_error_pb2,
)

FeedAttributeReferenceErrorPb2 = feed_attribute_reference_error_pb2
FeedAttributeReferenceErrorEnum = (
    feed_attribute_reference_error_pb2.FeedAttributeReferenceErrorEnum
)

from google.ads.google_ads.v2.proto.errors import feed_error_pb2 as feed_error_pb2

FeedErrorPb2 = feed_error_pb2
FeedErrorEnum = feed_error_pb2.FeedErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    feed_item_error_pb2 as feed_item_error_pb2,
)

FeedItemErrorPb2 = feed_item_error_pb2
FeedItemErrorEnum = feed_item_error_pb2.FeedItemErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    feed_item_target_error_pb2 as feed_item_target_error_pb2,
)

FeedItemTargetErrorPb2 = feed_item_target_error_pb2
FeedItemTargetErrorEnum = feed_item_target_error_pb2.FeedItemTargetErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    feed_item_validation_error_pb2 as feed_item_validation_error_pb2,
)

FeedItemValidationErrorPb2 = feed_item_validation_error_pb2
FeedItemValidationErrorEnum = feed_item_validation_error_pb2.FeedItemValidationErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    feed_mapping_error_pb2 as feed_mapping_error_pb2,
)

FeedMappingErrorPb2 = feed_mapping_error_pb2
FeedMappingErrorEnum = feed_mapping_error_pb2.FeedMappingErrorEnum

from google.ads.google_ads.v2.proto.errors import field_error_pb2 as field_error_pb2

FieldErrorPb2 = field_error_pb2
FieldErrorEnum = field_error_pb2.FieldErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    field_mask_error_pb2 as field_mask_error_pb2,
)

FieldMaskErrorPb2 = field_mask_error_pb2
FieldMaskErrorEnum = field_mask_error_pb2.FieldMaskErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    function_error_pb2 as function_error_pb2,
)

FunctionErrorPb2 = function_error_pb2
FunctionErrorEnum = function_error_pb2.FunctionErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    function_parsing_error_pb2 as function_parsing_error_pb2,
)

FunctionParsingErrorPb2 = function_parsing_error_pb2
FunctionParsingErrorEnum = function_parsing_error_pb2.FunctionParsingErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    geo_target_constant_suggestion_error_pb2 as geo_target_constant_suggestion_error_pb2,
)

GeoTargetConstantSuggestionErrorPb2 = geo_target_constant_suggestion_error_pb2
GeoTargetConstantSuggestionErrorEnum = (
    geo_target_constant_suggestion_error_pb2.GeoTargetConstantSuggestionErrorEnum
)

from google.ads.google_ads.v2.proto.errors import header_error_pb2 as header_error_pb2

HeaderErrorPb2 = header_error_pb2
HeaderErrorEnum = header_error_pb2.HeaderErrorEnum

from google.ads.google_ads.v2.proto.errors import id_error_pb2 as id_error_pb2

IdErrorPb2 = id_error_pb2
IdErrorEnum = id_error_pb2.IdErrorEnum

from google.ads.google_ads.v2.proto.errors import image_error_pb2 as image_error_pb2

ImageErrorPb2 = image_error_pb2
ImageErrorEnum = image_error_pb2.ImageErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    internal_error_pb2 as internal_error_pb2,
)

InternalErrorPb2 = internal_error_pb2
InternalErrorEnum = internal_error_pb2.InternalErrorEnum

from google.ads.google_ads.v2.proto.errors import invoice_error_pb2 as invoice_error_pb2

InvoiceErrorPb2 = invoice_error_pb2
InvoiceErrorEnum = invoice_error_pb2.InvoiceErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    keyword_plan_ad_group_error_pb2 as keyword_plan_ad_group_error_pb2,
)

KeywordPlanAdGroupErrorPb2 = keyword_plan_ad_group_error_pb2
KeywordPlanAdGroupErrorEnum = (
    keyword_plan_ad_group_error_pb2.KeywordPlanAdGroupErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    keyword_plan_campaign_error_pb2 as keyword_plan_campaign_error_pb2,
)

KeywordPlanCampaignErrorPb2 = keyword_plan_campaign_error_pb2
KeywordPlanCampaignErrorEnum = (
    keyword_plan_campaign_error_pb2.KeywordPlanCampaignErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    keyword_plan_error_pb2 as keyword_plan_error_pb2,
)

KeywordPlanErrorPb2 = keyword_plan_error_pb2
KeywordPlanErrorEnum = keyword_plan_error_pb2.KeywordPlanErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    keyword_plan_idea_error_pb2 as keyword_plan_idea_error_pb2,
)

KeywordPlanIdeaErrorPb2 = keyword_plan_idea_error_pb2
KeywordPlanIdeaErrorEnum = keyword_plan_idea_error_pb2.KeywordPlanIdeaErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    keyword_plan_keyword_error_pb2 as keyword_plan_keyword_error_pb2,
)

KeywordPlanKeywordErrorPb2 = keyword_plan_keyword_error_pb2
KeywordPlanKeywordErrorEnum = keyword_plan_keyword_error_pb2.KeywordPlanKeywordErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    keyword_plan_negative_keyword_error_pb2 as keyword_plan_negative_keyword_error_pb2,
)

KeywordPlanNegativeKeywordErrorPb2 = keyword_plan_negative_keyword_error_pb2
KeywordPlanNegativeKeywordErrorEnum = (
    keyword_plan_negative_keyword_error_pb2.KeywordPlanNegativeKeywordErrorEnum
)

from google.ads.google_ads.v2.proto.errors import label_error_pb2 as label_error_pb2

LabelErrorPb2 = label_error_pb2
LabelErrorEnum = label_error_pb2.LabelErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    language_code_error_pb2 as language_code_error_pb2,
)

LanguageCodeErrorPb2 = language_code_error_pb2
LanguageCodeErrorEnum = language_code_error_pb2.LanguageCodeErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    list_operation_error_pb2 as list_operation_error_pb2,
)

ListOperationErrorPb2 = list_operation_error_pb2
ListOperationErrorEnum = list_operation_error_pb2.ListOperationErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    manager_link_error_pb2 as manager_link_error_pb2,
)

ManagerLinkErrorPb2 = manager_link_error_pb2
ManagerLinkErrorEnum = manager_link_error_pb2.ManagerLinkErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    media_bundle_error_pb2 as media_bundle_error_pb2,
)

MediaBundleErrorPb2 = media_bundle_error_pb2
MediaBundleErrorEnum = media_bundle_error_pb2.MediaBundleErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    media_file_error_pb2 as media_file_error_pb2,
)

MediaFileErrorPb2 = media_file_error_pb2
MediaFileErrorEnum = media_file_error_pb2.MediaFileErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    media_upload_error_pb2 as media_upload_error_pb2,
)

MediaUploadErrorPb2 = media_upload_error_pb2
MediaUploadErrorEnum = media_upload_error_pb2.MediaUploadErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    merchant_center_link_error_pb2 as merchant_center_link_error_pb2,
)

MerchantCenterLinkErrorPb2 = merchant_center_link_error_pb2

from google.ads.google_ads.v2.proto.errors import (
    multiplier_error_pb2 as multiplier_error_pb2,
)

MultiplierErrorPb2 = multiplier_error_pb2
MultiplierErrorEnum = multiplier_error_pb2.MultiplierErrorEnum

from google.ads.google_ads.v2.proto.errors import mutate_error_pb2 as mutate_error_pb2

MutateErrorPb2 = mutate_error_pb2
MutateErrorEnum = mutate_error_pb2.MutateErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    mutate_job_error_pb2 as mutate_job_error_pb2,
)

MutateJobErrorPb2 = mutate_job_error_pb2
MutateJobErrorEnum = mutate_job_error_pb2.MutateJobErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    new_resource_creation_error_pb2 as new_resource_creation_error_pb2,
)

NewResourceCreationErrorPb2 = new_resource_creation_error_pb2
NewResourceCreationErrorEnum = (
    new_resource_creation_error_pb2.NewResourceCreationErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    not_empty_error_pb2 as not_empty_error_pb2,
)

NotEmptyErrorPb2 = not_empty_error_pb2
NotEmptyErrorEnum = not_empty_error_pb2.NotEmptyErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    not_whitelisted_error_pb2 as not_whitelisted_error_pb2,
)

NotWhitelistedErrorPb2 = not_whitelisted_error_pb2
NotWhitelistedErrorEnum = not_whitelisted_error_pb2.NotWhitelistedErrorEnum

from google.ads.google_ads.v2.proto.errors import null_error_pb2 as null_error_pb2

NullErrorPb2 = null_error_pb2
NullErrorEnum = null_error_pb2.NullErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    offline_user_data_job_error_pb2 as offline_user_data_job_error_pb2,
)

OfflineUserDataJobErrorPb2 = offline_user_data_job_error_pb2

from google.ads.google_ads.v2.proto.errors import (
    operation_access_denied_error_pb2 as operation_access_denied_error_pb2,
)

OperationAccessDeniedErrorPb2 = operation_access_denied_error_pb2
OperationAccessDeniedErrorEnum = (
    operation_access_denied_error_pb2.OperationAccessDeniedErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    operator_error_pb2 as operator_error_pb2,
)

OperatorErrorPb2 = operator_error_pb2
OperatorErrorEnum = operator_error_pb2.OperatorErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    partial_failure_error_pb2 as partial_failure_error_pb2,
)

PartialFailureErrorPb2 = partial_failure_error_pb2
PartialFailureErrorEnum = partial_failure_error_pb2.PartialFailureErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    policy_finding_error_pb2 as policy_finding_error_pb2,
)

PolicyFindingErrorPb2 = policy_finding_error_pb2
PolicyFindingErrorEnum = policy_finding_error_pb2.PolicyFindingErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    policy_validation_parameter_error_pb2 as policy_validation_parameter_error_pb2,
)

PolicyValidationParameterErrorPb2 = policy_validation_parameter_error_pb2
PolicyValidationParameterErrorEnum = (
    policy_validation_parameter_error_pb2.PolicyValidationParameterErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    policy_violation_error_pb2 as policy_violation_error_pb2,
)

PolicyViolationErrorPb2 = policy_violation_error_pb2
PolicyViolationErrorEnum = policy_violation_error_pb2.PolicyViolationErrorEnum

from google.ads.google_ads.v2.proto.errors import query_error_pb2 as query_error_pb2

QueryErrorPb2 = query_error_pb2
QueryErrorEnum = query_error_pb2.QueryErrorEnum

from google.ads.google_ads.v2.proto.errors import quota_error_pb2 as quota_error_pb2

QuotaErrorPb2 = quota_error_pb2
QuotaErrorEnum = quota_error_pb2.QuotaErrorEnum

from google.ads.google_ads.v2.proto.errors import range_error_pb2 as range_error_pb2

RangeErrorPb2 = range_error_pb2
RangeErrorEnum = range_error_pb2.RangeErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    reach_plan_error_pb2 as reach_plan_error_pb2,
)

ReachPlanErrorPb2 = reach_plan_error_pb2
ReachPlanErrorEnum = reach_plan_error_pb2.ReachPlanErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    recommendation_error_pb2 as recommendation_error_pb2,
)

RecommendationErrorPb2 = recommendation_error_pb2
RecommendationErrorEnum = recommendation_error_pb2.RecommendationErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    region_code_error_pb2 as region_code_error_pb2,
)

RegionCodeErrorPb2 = region_code_error_pb2
RegionCodeErrorEnum = region_code_error_pb2.RegionCodeErrorEnum

from google.ads.google_ads.v2.proto.errors import request_error_pb2 as request_error_pb2

RequestErrorPb2 = request_error_pb2
RequestErrorEnum = request_error_pb2.RequestErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    resource_access_denied_error_pb2 as resource_access_denied_error_pb2,
)

ResourceAccessDeniedErrorPb2 = resource_access_denied_error_pb2
ResourceAccessDeniedErrorEnum = (
    resource_access_denied_error_pb2.ResourceAccessDeniedErrorEnum
)

from google.ads.google_ads.v2.proto.errors import (
    resource_count_limit_exceeded_error_pb2 as resource_count_limit_exceeded_error_pb2,
)

ResourceCountLimitExceededErrorPb2 = resource_count_limit_exceeded_error_pb2
ResourceCountLimitExceededErrorEnum = (
    resource_count_limit_exceeded_error_pb2.ResourceCountLimitExceededErrorEnum
)

from google.ads.google_ads.v2.proto.errors import setting_error_pb2 as setting_error_pb2

SettingErrorPb2 = setting_error_pb2
SettingErrorEnum = setting_error_pb2.SettingErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    shared_criterion_error_pb2 as shared_criterion_error_pb2,
)

SharedCriterionErrorPb2 = shared_criterion_error_pb2
SharedCriterionErrorEnum = shared_criterion_error_pb2.SharedCriterionErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    shared_set_error_pb2 as shared_set_error_pb2,
)

SharedSetErrorPb2 = shared_set_error_pb2
SharedSetErrorEnum = shared_set_error_pb2.SharedSetErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    size_limit_error_pb2 as size_limit_error_pb2,
)

SizeLimitErrorPb2 = size_limit_error_pb2
SizeLimitErrorEnum = size_limit_error_pb2.SizeLimitErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    string_format_error_pb2 as string_format_error_pb2,
)

StringFormatErrorPb2 = string_format_error_pb2
StringFormatErrorEnum = string_format_error_pb2.StringFormatErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    string_length_error_pb2 as string_length_error_pb2,
)

StringLengthErrorPb2 = string_length_error_pb2
StringLengthErrorEnum = string_length_error_pb2.StringLengthErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    url_field_error_pb2 as url_field_error_pb2,
)

UrlFieldErrorPb2 = url_field_error_pb2
UrlFieldErrorEnum = url_field_error_pb2.UrlFieldErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    user_list_error_pb2 as user_list_error_pb2,
)

UserListErrorPb2 = user_list_error_pb2
UserListErrorEnum = user_list_error_pb2.UserListErrorEnum

from google.ads.google_ads.v2.proto.errors import (
    youtube_video_registration_error_pb2 as youtube_video_registration_error_pb2,
)

YoutubeVideoRegistrationErrorPb2 = youtube_video_registration_error_pb2
YoutubeVideoRegistrationErrorEnum = (
    youtube_video_registration_error_pb2.YoutubeVideoRegistrationErrorEnum
)

from google.ads.google_ads.v2.proto.resources import (
    account_budget_pb2 as account_budget_pb2,
)

AccountBudgetPb2 = account_budget_pb2
AccountBudget = account_budget_pb2.AccountBudget

from google.ads.google_ads.v2.proto.resources import (
    account_budget_proposal_pb2 as account_budget_proposal_pb2,
)

AccountBudgetProposalPb2 = account_budget_proposal_pb2
AccountBudgetProposal = account_budget_proposal_pb2.AccountBudgetProposal

from google.ads.google_ads.v2.proto.resources import (
    ad_group_ad_asset_view_pb2 as ad_group_ad_asset_view_pb2,
)

AdGroupAdAssetViewPb2 = ad_group_ad_asset_view_pb2
AdGroupAdAssetPolicySummary = ad_group_ad_asset_view_pb2.AdGroupAdAssetPolicySummary
AdGroupAdAssetView = ad_group_ad_asset_view_pb2.AdGroupAdAssetView

from google.ads.google_ads.v2.proto.resources import (
    ad_group_ad_label_pb2 as ad_group_ad_label_pb2,
)

AdGroupAdLabelPb2 = ad_group_ad_label_pb2
AdGroupAdLabel = ad_group_ad_label_pb2.AdGroupAdLabel

from google.ads.google_ads.v2.proto.resources import ad_group_ad_pb2 as ad_group_ad_pb2

AdGroupAdPb2 = ad_group_ad_pb2
AdGroupAd = ad_group_ad_pb2.AdGroupAd
AdGroupAdPolicySummary = ad_group_ad_pb2.AdGroupAdPolicySummary

from google.ads.google_ads.v2.proto.resources import (
    ad_group_audience_view_pb2 as ad_group_audience_view_pb2,
)

AdGroupAudienceViewPb2 = ad_group_audience_view_pb2
AdGroupAudienceView = ad_group_audience_view_pb2.AdGroupAudienceView

from google.ads.google_ads.v2.proto.resources import (
    ad_group_bid_modifier_pb2 as ad_group_bid_modifier_pb2,
)

AdGroupBidModifierPb2 = ad_group_bid_modifier_pb2
AdGroupBidModifier = ad_group_bid_modifier_pb2.AdGroupBidModifier

from google.ads.google_ads.v2.proto.resources import (
    ad_group_criterion_label_pb2 as ad_group_criterion_label_pb2,
)

AdGroupCriterionLabelPb2 = ad_group_criterion_label_pb2
AdGroupCriterionLabel = ad_group_criterion_label_pb2.AdGroupCriterionLabel

from google.ads.google_ads.v2.proto.resources import (
    ad_group_criterion_pb2 as ad_group_criterion_pb2,
)

AdGroupCriterionPb2 = ad_group_criterion_pb2
AdGroupCriterion = ad_group_criterion_pb2.AdGroupCriterion

from google.ads.google_ads.v2.proto.resources import (
    ad_group_criterion_simulation_pb2 as ad_group_criterion_simulation_pb2,
)

AdGroupCriterionSimulationPb2 = ad_group_criterion_simulation_pb2
AdGroupCriterionSimulation = (
    ad_group_criterion_simulation_pb2.AdGroupCriterionSimulation
)

from google.ads.google_ads.v2.proto.resources import (
    ad_group_extension_setting_pb2 as ad_group_extension_setting_pb2,
)

AdGroupExtensionSettingPb2 = ad_group_extension_setting_pb2
AdGroupExtensionSetting = ad_group_extension_setting_pb2.AdGroupExtensionSetting

from google.ads.google_ads.v2.proto.resources import (
    ad_group_feed_pb2 as ad_group_feed_pb2,
)

AdGroupFeedPb2 = ad_group_feed_pb2
AdGroupFeed = ad_group_feed_pb2.AdGroupFeed

from google.ads.google_ads.v2.proto.resources import (
    ad_group_label_pb2 as ad_group_label_pb2,
)

AdGroupLabelPb2 = ad_group_label_pb2
AdGroupLabel = ad_group_label_pb2.AdGroupLabel

from google.ads.google_ads.v2.proto.resources import ad_group_pb2 as ad_group_pb2

AdGroupPb2 = ad_group_pb2
AdGroup = ad_group_pb2.AdGroup

from google.ads.google_ads.v2.proto.resources import (
    ad_group_simulation_pb2 as ad_group_simulation_pb2,
)

AdGroupSimulationPb2 = ad_group_simulation_pb2
AdGroupSimulation = ad_group_simulation_pb2.AdGroupSimulation

from google.ads.google_ads.v2.proto.resources import (
    ad_parameter_pb2 as ad_parameter_pb2,
)

AdParameterPb2 = ad_parameter_pb2
AdParameter = ad_parameter_pb2.AdParameter

from google.ads.google_ads.v2.proto.resources import ad_pb2 as ad_pb2

AdPb2 = ad_pb2
Ad = ad_pb2.Ad

from google.ads.google_ads.v2.proto.resources import (
    ad_schedule_view_pb2 as ad_schedule_view_pb2,
)

AdScheduleViewPb2 = ad_schedule_view_pb2
AdScheduleView = ad_schedule_view_pb2.AdScheduleView

from google.ads.google_ads.v2.proto.resources import (
    ad_variation_ad_view_pb2 as ad_variation_ad_view_pb2,
)

AdVariationAdViewPb2 = ad_variation_ad_view_pb2

from google.ads.google_ads.v2.proto.resources import (
    age_range_view_pb2 as age_range_view_pb2,
)

AgeRangeViewPb2 = age_range_view_pb2
AgeRangeView = age_range_view_pb2.AgeRangeView

from google.ads.google_ads.v2.proto.resources import asset_pb2 as asset_pb2

AssetPb2 = asset_pb2
Asset = asset_pb2.Asset

from google.ads.google_ads.v2.proto.resources import (
    bidding_strategy_pb2 as bidding_strategy_pb2,
)

BiddingStrategyPb2 = bidding_strategy_pb2
BiddingStrategy = bidding_strategy_pb2.BiddingStrategy

from google.ads.google_ads.v2.proto.resources import (
    billing_setup_pb2 as billing_setup_pb2,
)

BillingSetupPb2 = billing_setup_pb2
BillingSetup = billing_setup_pb2.BillingSetup

from google.ads.google_ads.v2.proto.resources import (
    campaign_audience_view_pb2 as campaign_audience_view_pb2,
)

CampaignAudienceViewPb2 = campaign_audience_view_pb2
CampaignAudienceView = campaign_audience_view_pb2.CampaignAudienceView

from google.ads.google_ads.v2.proto.resources import (
    campaign_bid_modifier_pb2 as campaign_bid_modifier_pb2,
)

CampaignBidModifierPb2 = campaign_bid_modifier_pb2
CampaignBidModifier = campaign_bid_modifier_pb2.CampaignBidModifier

from google.ads.google_ads.v2.proto.resources import (
    campaign_budget_pb2 as campaign_budget_pb2,
)

CampaignBudgetPb2 = campaign_budget_pb2
CampaignBudget = campaign_budget_pb2.CampaignBudget

from google.ads.google_ads.v2.proto.resources import (
    campaign_criterion_pb2 as campaign_criterion_pb2,
)

CampaignCriterionPb2 = campaign_criterion_pb2
CampaignCriterion = campaign_criterion_pb2.CampaignCriterion

from google.ads.google_ads.v2.proto.resources import (
    campaign_criterion_simulation_pb2 as campaign_criterion_simulation_pb2,
)

CampaignCriterionSimulationPb2 = campaign_criterion_simulation_pb2
CampaignCriterionSimulation = (
    campaign_criterion_simulation_pb2.CampaignCriterionSimulation
)

from google.ads.google_ads.v2.proto.resources import (
    campaign_draft_pb2 as campaign_draft_pb2,
)

CampaignDraftPb2 = campaign_draft_pb2
CampaignDraft = campaign_draft_pb2.CampaignDraft

from google.ads.google_ads.v2.proto.resources import (
    campaign_experiment_pb2 as campaign_experiment_pb2,
)

CampaignExperimentPb2 = campaign_experiment_pb2
CampaignExperiment = campaign_experiment_pb2.CampaignExperiment

from google.ads.google_ads.v2.proto.resources import (
    campaign_extension_setting_pb2 as campaign_extension_setting_pb2,
)

CampaignExtensionSettingPb2 = campaign_extension_setting_pb2
CampaignExtensionSetting = campaign_extension_setting_pb2.CampaignExtensionSetting

from google.ads.google_ads.v2.proto.resources import (
    campaign_feed_pb2 as campaign_feed_pb2,
)

CampaignFeedPb2 = campaign_feed_pb2
CampaignFeed = campaign_feed_pb2.CampaignFeed

from google.ads.google_ads.v2.proto.resources import (
    campaign_label_pb2 as campaign_label_pb2,
)

CampaignLabelPb2 = campaign_label_pb2
CampaignLabel = campaign_label_pb2.CampaignLabel

from google.ads.google_ads.v2.proto.resources import campaign_pb2 as campaign_pb2

CampaignPb2 = campaign_pb2
Campaign = campaign_pb2.Campaign

from google.ads.google_ads.v2.proto.resources import (
    campaign_shared_set_pb2 as campaign_shared_set_pb2,
)

CampaignSharedSetPb2 = campaign_shared_set_pb2
CampaignSharedSet = campaign_shared_set_pb2.CampaignSharedSet

from google.ads.google_ads.v2.proto.resources import (
    carrier_constant_pb2 as carrier_constant_pb2,
)

CarrierConstantPb2 = carrier_constant_pb2
CarrierConstant = carrier_constant_pb2.CarrierConstant

from google.ads.google_ads.v2.proto.resources import (
    change_status_pb2 as change_status_pb2,
)

ChangeStatusPb2 = change_status_pb2
ChangeStatus = change_status_pb2.ChangeStatus

from google.ads.google_ads.v2.proto.resources import click_view_pb2 as click_view_pb2

ClickViewPb2 = click_view_pb2
ClickView = click_view_pb2.ClickView

from google.ads.google_ads.v2.proto.resources import (
    conversion_action_pb2 as conversion_action_pb2,
)

ConversionActionPb2 = conversion_action_pb2
ConversionAction = conversion_action_pb2.ConversionAction

from google.ads.google_ads.v2.proto.resources import (
    currency_constant_pb2 as currency_constant_pb2,
)

CurrencyConstantPb2 = currency_constant_pb2

from google.ads.google_ads.v2.proto.resources import (
    custom_interest_pb2 as custom_interest_pb2,
)

CustomInterestPb2 = custom_interest_pb2
CustomInterest = custom_interest_pb2.CustomInterest
CustomInterestMember = custom_interest_pb2.CustomInterestMember

from google.ads.google_ads.v2.proto.resources import (
    customer_client_link_pb2 as customer_client_link_pb2,
)

CustomerClientLinkPb2 = customer_client_link_pb2
CustomerClientLink = customer_client_link_pb2.CustomerClientLink

from google.ads.google_ads.v2.proto.resources import (
    customer_client_pb2 as customer_client_pb2,
)

CustomerClientPb2 = customer_client_pb2
CustomerClient = customer_client_pb2.CustomerClient

from google.ads.google_ads.v2.proto.resources import (
    customer_extension_setting_pb2 as customer_extension_setting_pb2,
)

CustomerExtensionSettingPb2 = customer_extension_setting_pb2
CustomerExtensionSetting = customer_extension_setting_pb2.CustomerExtensionSetting

from google.ads.google_ads.v2.proto.resources import (
    customer_feed_pb2 as customer_feed_pb2,
)

CustomerFeedPb2 = customer_feed_pb2
CustomerFeed = customer_feed_pb2.CustomerFeed

from google.ads.google_ads.v2.proto.resources import (
    customer_label_pb2 as customer_label_pb2,
)

CustomerLabelPb2 = customer_label_pb2
CustomerLabel = customer_label_pb2.CustomerLabel

from google.ads.google_ads.v2.proto.resources import (
    customer_manager_link_pb2 as customer_manager_link_pb2,
)

CustomerManagerLinkPb2 = customer_manager_link_pb2
CustomerManagerLink = customer_manager_link_pb2.CustomerManagerLink

from google.ads.google_ads.v2.proto.resources import (
    customer_negative_criterion_pb2 as customer_negative_criterion_pb2,
)

CustomerNegativeCriterionPb2 = customer_negative_criterion_pb2
CustomerNegativeCriterion = customer_negative_criterion_pb2.CustomerNegativeCriterion

from google.ads.google_ads.v2.proto.resources import customer_pb2 as customer_pb2

CustomerPb2 = customer_pb2
CallReportingSetting = customer_pb2.CallReportingSetting
ConversionTrackingSetting = customer_pb2.ConversionTrackingSetting
Customer = customer_pb2.Customer
RemarketingSetting = customer_pb2.RemarketingSetting

from google.ads.google_ads.v2.proto.resources import (
    detail_placement_view_pb2 as detail_placement_view_pb2,
)

DetailPlacementViewPb2 = detail_placement_view_pb2
DetailPlacementView = detail_placement_view_pb2.DetailPlacementView

from google.ads.google_ads.v2.proto.resources import (
    display_keyword_view_pb2 as display_keyword_view_pb2,
)

DisplayKeywordViewPb2 = display_keyword_view_pb2
DisplayKeywordView = display_keyword_view_pb2.DisplayKeywordView

from google.ads.google_ads.v2.proto.resources import (
    distance_view_pb2 as distance_view_pb2,
)

DistanceViewPb2 = distance_view_pb2
DistanceView = distance_view_pb2.DistanceView

from google.ads.google_ads.v2.proto.resources import (
    domain_category_pb2 as domain_category_pb2,
)

DomainCategoryPb2 = domain_category_pb2
DomainCategory = domain_category_pb2.DomainCategory

from google.ads.google_ads.v2.proto.resources import (
    dynamic_search_ads_search_term_view_pb2 as dynamic_search_ads_search_term_view_pb2,
)

DynamicSearchAdsSearchTermViewPb2 = dynamic_search_ads_search_term_view_pb2
DynamicSearchAdsSearchTermView = (
    dynamic_search_ads_search_term_view_pb2.DynamicSearchAdsSearchTermView
)

from google.ads.google_ads.v2.proto.resources import (
    expanded_landing_page_view_pb2 as expanded_landing_page_view_pb2,
)

ExpandedLandingPageViewPb2 = expanded_landing_page_view_pb2
ExpandedLandingPageView = expanded_landing_page_view_pb2.ExpandedLandingPageView

from google.ads.google_ads.v2.proto.resources import experiment_pb2 as experiment_pb2

ExperimentPb2 = experiment_pb2

from google.ads.google_ads.v2.proto.resources import (
    extension_feed_item_pb2 as extension_feed_item_pb2,
)

ExtensionFeedItemPb2 = extension_feed_item_pb2
ExtensionFeedItem = extension_feed_item_pb2.ExtensionFeedItem

from google.ads.google_ads.v2.proto.resources import feed_item_pb2 as feed_item_pb2

FeedItemPb2 = feed_item_pb2
FeedItemAttributeValue = feed_item_pb2.FeedItemAttributeValue
FeedItem = feed_item_pb2.FeedItem
FeedItemPlaceholderPolicyInfo = feed_item_pb2.FeedItemPlaceholderPolicyInfo
FeedItemValidationError = feed_item_pb2.FeedItemValidationError

from google.ads.google_ads.v2.proto.resources import (
    feed_item_target_pb2 as feed_item_target_pb2,
)

FeedItemTargetPb2 = feed_item_target_pb2
FeedItemTarget = feed_item_target_pb2.FeedItemTarget

from google.ads.google_ads.v2.proto.resources import (
    feed_mapping_pb2 as feed_mapping_pb2,
)

FeedMappingPb2 = feed_mapping_pb2
AttributeFieldMapping = feed_mapping_pb2.AttributeFieldMapping
FeedMapping = feed_mapping_pb2.FeedMapping

from google.ads.google_ads.v2.proto.resources import feed_pb2 as feed_pb2

FeedPb2 = feed_pb2
FeedAttribute = feed_pb2.FeedAttribute
FeedAttributeOperation = feed_pb2.FeedAttributeOperation
Feed = feed_pb2.Feed

from google.ads.google_ads.v2.proto.resources import (
    feed_placeholder_view_pb2 as feed_placeholder_view_pb2,
)

FeedPlaceholderViewPb2 = feed_placeholder_view_pb2
FeedPlaceholderView = feed_placeholder_view_pb2.FeedPlaceholderView

from google.ads.google_ads.v2.proto.resources import gender_view_pb2 as gender_view_pb2

GenderViewPb2 = gender_view_pb2
GenderView = gender_view_pb2.GenderView

from google.ads.google_ads.v2.proto.resources import (
    geo_target_constant_pb2 as geo_target_constant_pb2,
)

GeoTargetConstantPb2 = geo_target_constant_pb2
GeoTargetConstant = geo_target_constant_pb2.GeoTargetConstant

from google.ads.google_ads.v2.proto.resources import (
    geographic_view_pb2 as geographic_view_pb2,
)

GeographicViewPb2 = geographic_view_pb2
GeographicView = geographic_view_pb2.GeographicView

from google.ads.google_ads.v2.proto.resources import (
    google_ads_field_pb2 as google_ads_field_pb2,
)

GoogleAdsFieldPb2 = google_ads_field_pb2
GoogleAdsField = google_ads_field_pb2.GoogleAdsField

from google.ads.google_ads.v2.proto.resources import (
    group_placement_view_pb2 as group_placement_view_pb2,
)

GroupPlacementViewPb2 = group_placement_view_pb2
GroupPlacementView = group_placement_view_pb2.GroupPlacementView

from google.ads.google_ads.v2.proto.resources import (
    hotel_group_view_pb2 as hotel_group_view_pb2,
)

HotelGroupViewPb2 = hotel_group_view_pb2
HotelGroupView = hotel_group_view_pb2.HotelGroupView

from google.ads.google_ads.v2.proto.resources import (
    hotel_performance_view_pb2 as hotel_performance_view_pb2,
)

HotelPerformanceViewPb2 = hotel_performance_view_pb2
HotelPerformanceView = hotel_performance_view_pb2.HotelPerformanceView

from google.ads.google_ads.v2.proto.resources import invoice_pb2 as invoice_pb2

InvoicePb2 = invoice_pb2
Invoice = invoice_pb2.Invoice

from google.ads.google_ads.v2.proto.resources import (
    keyword_plan_ad_group_pb2 as keyword_plan_ad_group_pb2,
)

KeywordPlanAdGroupPb2 = keyword_plan_ad_group_pb2
KeywordPlanAdGroup = keyword_plan_ad_group_pb2.KeywordPlanAdGroup

from google.ads.google_ads.v2.proto.resources import (
    keyword_plan_campaign_pb2 as keyword_plan_campaign_pb2,
)

KeywordPlanCampaignPb2 = keyword_plan_campaign_pb2
KeywordPlanCampaign = keyword_plan_campaign_pb2.KeywordPlanCampaign
KeywordPlanGeoTarget = keyword_plan_campaign_pb2.KeywordPlanGeoTarget

from google.ads.google_ads.v2.proto.resources import (
    keyword_plan_keyword_pb2 as keyword_plan_keyword_pb2,
)

KeywordPlanKeywordPb2 = keyword_plan_keyword_pb2
KeywordPlanKeyword = keyword_plan_keyword_pb2.KeywordPlanKeyword

from google.ads.google_ads.v2.proto.resources import (
    keyword_plan_negative_keyword_pb2 as keyword_plan_negative_keyword_pb2,
)

KeywordPlanNegativeKeywordPb2 = keyword_plan_negative_keyword_pb2
KeywordPlanNegativeKeyword = (
    keyword_plan_negative_keyword_pb2.KeywordPlanNegativeKeyword
)

from google.ads.google_ads.v2.proto.resources import (
    keyword_plan_pb2 as keyword_plan_pb2,
)

KeywordPlanPb2 = keyword_plan_pb2
KeywordPlanForecastPeriod = keyword_plan_pb2.KeywordPlanForecastPeriod
KeywordPlan = keyword_plan_pb2.KeywordPlan

from google.ads.google_ads.v2.proto.resources import (
    keyword_view_pb2 as keyword_view_pb2,
)

KeywordViewPb2 = keyword_view_pb2
KeywordView = keyword_view_pb2.KeywordView

from google.ads.google_ads.v2.proto.resources import label_pb2 as label_pb2

LabelPb2 = label_pb2
Label = label_pb2.Label

from google.ads.google_ads.v2.proto.resources import (
    landing_page_view_pb2 as landing_page_view_pb2,
)

LandingPageViewPb2 = landing_page_view_pb2
LandingPageView = landing_page_view_pb2.LandingPageView

from google.ads.google_ads.v2.proto.resources import (
    language_constant_pb2 as language_constant_pb2,
)

LanguageConstantPb2 = language_constant_pb2
LanguageConstant = language_constant_pb2.LanguageConstant

from google.ads.google_ads.v2.proto.resources import (
    location_view_pb2 as location_view_pb2,
)

LocationViewPb2 = location_view_pb2
LocationView = location_view_pb2.LocationView

from google.ads.google_ads.v2.proto.resources import (
    managed_placement_view_pb2 as managed_placement_view_pb2,
)

ManagedPlacementViewPb2 = managed_placement_view_pb2
ManagedPlacementView = managed_placement_view_pb2.ManagedPlacementView

from google.ads.google_ads.v2.proto.resources import media_file_pb2 as media_file_pb2

MediaFilePb2 = media_file_pb2
MediaAudio = media_file_pb2.MediaAudio
MediaBundle = media_file_pb2.MediaBundle
MediaFile = media_file_pb2.MediaFile
MediaImage = media_file_pb2.MediaImage
MediaVideo = media_file_pb2.MediaVideo

from google.ads.google_ads.v2.proto.resources import (
    merchant_center_link_pb2 as merchant_center_link_pb2,
)

MerchantCenterLinkPb2 = merchant_center_link_pb2
MerchantCenterLink = merchant_center_link_pb2.MerchantCenterLink

from google.ads.google_ads.v2.proto.resources import (
    mobile_app_category_constant_pb2 as mobile_app_category_constant_pb2,
)

MobileAppCategoryConstantPb2 = mobile_app_category_constant_pb2
MobileAppCategoryConstant = mobile_app_category_constant_pb2.MobileAppCategoryConstant

from google.ads.google_ads.v2.proto.resources import (
    mobile_device_constant_pb2 as mobile_device_constant_pb2,
)

MobileDeviceConstantPb2 = mobile_device_constant_pb2
MobileDeviceConstant = mobile_device_constant_pb2.MobileDeviceConstant

from google.ads.google_ads.v2.proto.resources import mutate_job_pb2 as mutate_job_pb2

MutateJobPb2 = mutate_job_pb2
MutateJob = mutate_job_pb2.MutateJob

from google.ads.google_ads.v2.proto.resources import (
    offline_user_data_job_pb2 as offline_user_data_job_pb2,
)

OfflineUserDataJobPb2 = offline_user_data_job_pb2

from google.ads.google_ads.v2.proto.resources import (
    operating_system_version_constant_pb2 as operating_system_version_constant_pb2,
)

OperatingSystemVersionConstantPb2 = operating_system_version_constant_pb2
OperatingSystemVersionConstant = (
    operating_system_version_constant_pb2.OperatingSystemVersionConstant
)

from google.ads.google_ads.v2.proto.resources import (
    paid_organic_search_term_view_pb2 as paid_organic_search_term_view_pb2,
)

PaidOrganicSearchTermViewPb2 = paid_organic_search_term_view_pb2
PaidOrganicSearchTermView = paid_organic_search_term_view_pb2.PaidOrganicSearchTermView

from google.ads.google_ads.v2.proto.resources import (
    parental_status_view_pb2 as parental_status_view_pb2,
)

ParentalStatusViewPb2 = parental_status_view_pb2
ParentalStatusView = parental_status_view_pb2.ParentalStatusView

from google.ads.google_ads.v2.proto.resources import (
    payments_account_pb2 as payments_account_pb2,
)

PaymentsAccountPb2 = payments_account_pb2
PaymentsAccount = payments_account_pb2.PaymentsAccount

from google.ads.google_ads.v2.proto.resources import (
    product_bidding_category_constant_pb2 as product_bidding_category_constant_pb2,
)

ProductBiddingCategoryConstantPb2 = product_bidding_category_constant_pb2
ProductBiddingCategoryConstant = (
    product_bidding_category_constant_pb2.ProductBiddingCategoryConstant
)

from google.ads.google_ads.v2.proto.resources import (
    product_group_view_pb2 as product_group_view_pb2,
)

ProductGroupViewPb2 = product_group_view_pb2
ProductGroupView = product_group_view_pb2.ProductGroupView

from google.ads.google_ads.v2.proto.resources import (
    recommendation_pb2 as recommendation_pb2,
)

RecommendationPb2 = recommendation_pb2
Recommendation = recommendation_pb2.Recommendation

from google.ads.google_ads.v2.proto.resources import (
    remarketing_action_pb2 as remarketing_action_pb2,
)

RemarketingActionPb2 = remarketing_action_pb2
RemarketingAction = remarketing_action_pb2.RemarketingAction

from google.ads.google_ads.v2.proto.resources import (
    search_term_view_pb2 as search_term_view_pb2,
)

SearchTermViewPb2 = search_term_view_pb2
SearchTermView = search_term_view_pb2.SearchTermView

from google.ads.google_ads.v2.proto.resources import (
    shared_criterion_pb2 as shared_criterion_pb2,
)

SharedCriterionPb2 = shared_criterion_pb2
SharedCriterion = shared_criterion_pb2.SharedCriterion

from google.ads.google_ads.v2.proto.resources import shared_set_pb2 as shared_set_pb2

SharedSetPb2 = shared_set_pb2
SharedSet = shared_set_pb2.SharedSet

from google.ads.google_ads.v2.proto.resources import (
    shopping_performance_view_pb2 as shopping_performance_view_pb2,
)

ShoppingPerformanceViewPb2 = shopping_performance_view_pb2
ShoppingPerformanceView = shopping_performance_view_pb2.ShoppingPerformanceView

from google.ads.google_ads.v2.proto.resources import (
    topic_constant_pb2 as topic_constant_pb2,
)

TopicConstantPb2 = topic_constant_pb2
TopicConstant = topic_constant_pb2.TopicConstant

from google.ads.google_ads.v2.proto.resources import topic_view_pb2 as topic_view_pb2

TopicViewPb2 = topic_view_pb2
TopicView = topic_view_pb2.TopicView

from google.ads.google_ads.v2.proto.resources import (
    user_interest_pb2 as user_interest_pb2,
)

UserInterestPb2 = user_interest_pb2
UserInterest = user_interest_pb2.UserInterest

from google.ads.google_ads.v2.proto.resources import user_list_pb2 as user_list_pb2

UserListPb2 = user_list_pb2
UserList = user_list_pb2.UserList

from google.ads.google_ads.v2.proto.resources import (
    user_location_view_pb2 as user_location_view_pb2,
)

UserLocationViewPb2 = user_location_view_pb2
UserLocationView = user_location_view_pb2.UserLocationView

from google.ads.google_ads.v2.proto.resources import video_pb2 as video_pb2

VideoPb2 = video_pb2
Video = video_pb2.Video

from google.ads.google_ads.v2.proto.services import (
    account_budget_proposal_service_pb2 as account_budget_proposal_service_pb2,
)

AccountBudgetProposalServicePb2 = account_budget_proposal_service_pb2
AccountBudgetProposalOperation = (
    account_budget_proposal_service_pb2.AccountBudgetProposalOperation
)
GetAccountBudgetProposalRequest = (
    account_budget_proposal_service_pb2.GetAccountBudgetProposalRequest
)
MutateAccountBudgetProposalRequest = (
    account_budget_proposal_service_pb2.MutateAccountBudgetProposalRequest
)
MutateAccountBudgetProposalResponse = (
    account_budget_proposal_service_pb2.MutateAccountBudgetProposalResponse
)
MutateAccountBudgetProposalResult = (
    account_budget_proposal_service_pb2.MutateAccountBudgetProposalResult
)

from google.ads.google_ads.v2.proto.services import (
    account_budget_service_pb2 as account_budget_service_pb2,
)

AccountBudgetServicePb2 = account_budget_service_pb2
GetAccountBudgetRequest = account_budget_service_pb2.GetAccountBudgetRequest

from google.ads.google_ads.v2.proto.services import (
    ad_group_ad_asset_view_service_pb2 as ad_group_ad_asset_view_service_pb2,
)

AdGroupAdAssetViewServicePb2 = ad_group_ad_asset_view_service_pb2
GetAdGroupAdAssetViewRequest = (
    ad_group_ad_asset_view_service_pb2.GetAdGroupAdAssetViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_ad_label_service_pb2 as ad_group_ad_label_service_pb2,
)

AdGroupAdLabelServicePb2 = ad_group_ad_label_service_pb2
AdGroupAdLabelOperation = ad_group_ad_label_service_pb2.AdGroupAdLabelOperation
GetAdGroupAdLabelRequest = ad_group_ad_label_service_pb2.GetAdGroupAdLabelRequest
MutateAdGroupAdLabelResult = ad_group_ad_label_service_pb2.MutateAdGroupAdLabelResult
MutateAdGroupAdLabelsRequest = (
    ad_group_ad_label_service_pb2.MutateAdGroupAdLabelsRequest
)
MutateAdGroupAdLabelsResponse = (
    ad_group_ad_label_service_pb2.MutateAdGroupAdLabelsResponse
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_ad_service_pb2 as ad_group_ad_service_pb2,
)

AdGroupAdServicePb2 = ad_group_ad_service_pb2
AdGroupAdOperation = ad_group_ad_service_pb2.AdGroupAdOperation
GetAdGroupAdRequest = ad_group_ad_service_pb2.GetAdGroupAdRequest
MutateAdGroupAdResult = ad_group_ad_service_pb2.MutateAdGroupAdResult
MutateAdGroupAdsRequest = ad_group_ad_service_pb2.MutateAdGroupAdsRequest
MutateAdGroupAdsResponse = ad_group_ad_service_pb2.MutateAdGroupAdsResponse

from google.ads.google_ads.v2.proto.services import (
    ad_group_audience_view_service_pb2 as ad_group_audience_view_service_pb2,
)

AdGroupAudienceViewServicePb2 = ad_group_audience_view_service_pb2
GetAdGroupAudienceViewRequest = (
    ad_group_audience_view_service_pb2.GetAdGroupAudienceViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_bid_modifier_service_pb2 as ad_group_bid_modifier_service_pb2,
)

AdGroupBidModifierServicePb2 = ad_group_bid_modifier_service_pb2
AdGroupBidModifierOperation = (
    ad_group_bid_modifier_service_pb2.AdGroupBidModifierOperation
)
GetAdGroupBidModifierRequest = (
    ad_group_bid_modifier_service_pb2.GetAdGroupBidModifierRequest
)
MutateAdGroupBidModifierResult = (
    ad_group_bid_modifier_service_pb2.MutateAdGroupBidModifierResult
)
MutateAdGroupBidModifiersRequest = (
    ad_group_bid_modifier_service_pb2.MutateAdGroupBidModifiersRequest
)
MutateAdGroupBidModifiersResponse = (
    ad_group_bid_modifier_service_pb2.MutateAdGroupBidModifiersResponse
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_criterion_label_service_pb2 as ad_group_criterion_label_service_pb2,
)

AdGroupCriterionLabelServicePb2 = ad_group_criterion_label_service_pb2
AdGroupCriterionLabelOperation = (
    ad_group_criterion_label_service_pb2.AdGroupCriterionLabelOperation
)
GetAdGroupCriterionLabelRequest = (
    ad_group_criterion_label_service_pb2.GetAdGroupCriterionLabelRequest
)
MutateAdGroupCriterionLabelResult = (
    ad_group_criterion_label_service_pb2.MutateAdGroupCriterionLabelResult
)
MutateAdGroupCriterionLabelsRequest = (
    ad_group_criterion_label_service_pb2.MutateAdGroupCriterionLabelsRequest
)
MutateAdGroupCriterionLabelsResponse = (
    ad_group_criterion_label_service_pb2.MutateAdGroupCriterionLabelsResponse
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_criterion_service_pb2 as ad_group_criterion_service_pb2,
)

AdGroupCriterionServicePb2 = ad_group_criterion_service_pb2
AdGroupCriterionOperation = ad_group_criterion_service_pb2.AdGroupCriterionOperation
GetAdGroupCriterionRequest = ad_group_criterion_service_pb2.GetAdGroupCriterionRequest
MutateAdGroupCriteriaRequest = (
    ad_group_criterion_service_pb2.MutateAdGroupCriteriaRequest
)
MutateAdGroupCriteriaResponse = (
    ad_group_criterion_service_pb2.MutateAdGroupCriteriaResponse
)
MutateAdGroupCriterionResult = (
    ad_group_criterion_service_pb2.MutateAdGroupCriterionResult
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_criterion_simulation_service_pb2 as ad_group_criterion_simulation_service_pb2,
)

AdGroupCriterionSimulationServicePb2 = ad_group_criterion_simulation_service_pb2
GetAdGroupCriterionSimulationRequest = (
    ad_group_criterion_simulation_service_pb2.GetAdGroupCriterionSimulationRequest
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_extension_setting_service_pb2 as ad_group_extension_setting_service_pb2,
)

AdGroupExtensionSettingServicePb2 = ad_group_extension_setting_service_pb2
AdGroupExtensionSettingOperation = (
    ad_group_extension_setting_service_pb2.AdGroupExtensionSettingOperation
)
GetAdGroupExtensionSettingRequest = (
    ad_group_extension_setting_service_pb2.GetAdGroupExtensionSettingRequest
)
MutateAdGroupExtensionSettingResult = (
    ad_group_extension_setting_service_pb2.MutateAdGroupExtensionSettingResult
)
MutateAdGroupExtensionSettingsRequest = (
    ad_group_extension_setting_service_pb2.MutateAdGroupExtensionSettingsRequest
)
MutateAdGroupExtensionSettingsResponse = (
    ad_group_extension_setting_service_pb2.MutateAdGroupExtensionSettingsResponse
)

from google.ads.google_ads.v2.proto.services import (
    ad_group_feed_service_pb2 as ad_group_feed_service_pb2,
)

AdGroupFeedServicePb2 = ad_group_feed_service_pb2
AdGroupFeedOperation = ad_group_feed_service_pb2.AdGroupFeedOperation
GetAdGroupFeedRequest = ad_group_feed_service_pb2.GetAdGroupFeedRequest
MutateAdGroupFeedResult = ad_group_feed_service_pb2.MutateAdGroupFeedResult
MutateAdGroupFeedsRequest = ad_group_feed_service_pb2.MutateAdGroupFeedsRequest
MutateAdGroupFeedsResponse = ad_group_feed_service_pb2.MutateAdGroupFeedsResponse

from google.ads.google_ads.v2.proto.services import (
    ad_group_label_service_pb2 as ad_group_label_service_pb2,
)

AdGroupLabelServicePb2 = ad_group_label_service_pb2
AdGroupLabelOperation = ad_group_label_service_pb2.AdGroupLabelOperation
GetAdGroupLabelRequest = ad_group_label_service_pb2.GetAdGroupLabelRequest
MutateAdGroupLabelResult = ad_group_label_service_pb2.MutateAdGroupLabelResult
MutateAdGroupLabelsRequest = ad_group_label_service_pb2.MutateAdGroupLabelsRequest
MutateAdGroupLabelsResponse = ad_group_label_service_pb2.MutateAdGroupLabelsResponse

from google.ads.google_ads.v2.proto.services import (
    ad_group_service_pb2 as ad_group_service_pb2,
)

AdGroupServicePb2 = ad_group_service_pb2
AdGroupOperation = ad_group_service_pb2.AdGroupOperation
GetAdGroupRequest = ad_group_service_pb2.GetAdGroupRequest
MutateAdGroupResult = ad_group_service_pb2.MutateAdGroupResult
MutateAdGroupsRequest = ad_group_service_pb2.MutateAdGroupsRequest
MutateAdGroupsResponse = ad_group_service_pb2.MutateAdGroupsResponse

from google.ads.google_ads.v2.proto.services import (
    ad_group_simulation_service_pb2 as ad_group_simulation_service_pb2,
)

AdGroupSimulationServicePb2 = ad_group_simulation_service_pb2
GetAdGroupSimulationRequest = (
    ad_group_simulation_service_pb2.GetAdGroupSimulationRequest
)

from google.ads.google_ads.v2.proto.services import (
    ad_parameter_service_pb2 as ad_parameter_service_pb2,
)

AdParameterServicePb2 = ad_parameter_service_pb2
AdParameterOperation = ad_parameter_service_pb2.AdParameterOperation
GetAdParameterRequest = ad_parameter_service_pb2.GetAdParameterRequest
MutateAdParameterResult = ad_parameter_service_pb2.MutateAdParameterResult
MutateAdParametersRequest = ad_parameter_service_pb2.MutateAdParametersRequest
MutateAdParametersResponse = ad_parameter_service_pb2.MutateAdParametersResponse

from google.ads.google_ads.v2.proto.services import (
    ad_schedule_view_service_pb2 as ad_schedule_view_service_pb2,
)

AdScheduleViewServicePb2 = ad_schedule_view_service_pb2
GetAdScheduleViewRequest = ad_schedule_view_service_pb2.GetAdScheduleViewRequest

from google.ads.google_ads.v2.proto.services import ad_service_pb2 as ad_service_pb2

AdServicePb2 = ad_service_pb2
AdOperation = ad_service_pb2.AdOperation
GetAdRequest = ad_service_pb2.GetAdRequest
MutateAdResult = ad_service_pb2.MutateAdResult
MutateAdsRequest = ad_service_pb2.MutateAdsRequest
MutateAdsResponse = ad_service_pb2.MutateAdsResponse

from google.ads.google_ads.v2.proto.services import (
    ad_variation_ad_view_service_pb2 as ad_variation_ad_view_service_pb2,
)

AdVariationAdViewServicePb2 = ad_variation_ad_view_service_pb2

from google.ads.google_ads.v2.proto.services import (
    age_range_view_service_pb2 as age_range_view_service_pb2,
)

AgeRangeViewServicePb2 = age_range_view_service_pb2
GetAgeRangeViewRequest = age_range_view_service_pb2.GetAgeRangeViewRequest

from google.ads.google_ads.v2.proto.services import (
    asset_service_pb2 as asset_service_pb2,
)

AssetServicePb2 = asset_service_pb2
AssetOperation = asset_service_pb2.AssetOperation
GetAssetRequest = asset_service_pb2.GetAssetRequest
MutateAssetResult = asset_service_pb2.MutateAssetResult
MutateAssetsRequest = asset_service_pb2.MutateAssetsRequest
MutateAssetsResponse = asset_service_pb2.MutateAssetsResponse

from google.ads.google_ads.v2.proto.services import (
    bidding_strategy_service_pb2 as bidding_strategy_service_pb2,
)

BiddingStrategyServicePb2 = bidding_strategy_service_pb2
BiddingStrategyOperation = bidding_strategy_service_pb2.BiddingStrategyOperation
GetBiddingStrategyRequest = bidding_strategy_service_pb2.GetBiddingStrategyRequest
MutateBiddingStrategiesRequest = (
    bidding_strategy_service_pb2.MutateBiddingStrategiesRequest
)
MutateBiddingStrategiesResponse = (
    bidding_strategy_service_pb2.MutateBiddingStrategiesResponse
)
MutateBiddingStrategyResult = bidding_strategy_service_pb2.MutateBiddingStrategyResult

from google.ads.google_ads.v2.proto.services import (
    billing_setup_service_pb2 as billing_setup_service_pb2,
)

BillingSetupServicePb2 = billing_setup_service_pb2
BillingSetupOperation = billing_setup_service_pb2.BillingSetupOperation
GetBillingSetupRequest = billing_setup_service_pb2.GetBillingSetupRequest
MutateBillingSetupRequest = billing_setup_service_pb2.MutateBillingSetupRequest
MutateBillingSetupResponse = billing_setup_service_pb2.MutateBillingSetupResponse
MutateBillingSetupResult = billing_setup_service_pb2.MutateBillingSetupResult

from google.ads.google_ads.v2.proto.services import (
    campaign_audience_view_service_pb2 as campaign_audience_view_service_pb2,
)

CampaignAudienceViewServicePb2 = campaign_audience_view_service_pb2
GetCampaignAudienceViewRequest = (
    campaign_audience_view_service_pb2.GetCampaignAudienceViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    campaign_bid_modifier_service_pb2 as campaign_bid_modifier_service_pb2,
)

CampaignBidModifierServicePb2 = campaign_bid_modifier_service_pb2
CampaignBidModifierOperation = (
    campaign_bid_modifier_service_pb2.CampaignBidModifierOperation
)
GetCampaignBidModifierRequest = (
    campaign_bid_modifier_service_pb2.GetCampaignBidModifierRequest
)
MutateCampaignBidModifierResult = (
    campaign_bid_modifier_service_pb2.MutateCampaignBidModifierResult
)
MutateCampaignBidModifiersRequest = (
    campaign_bid_modifier_service_pb2.MutateCampaignBidModifiersRequest
)
MutateCampaignBidModifiersResponse = (
    campaign_bid_modifier_service_pb2.MutateCampaignBidModifiersResponse
)

from google.ads.google_ads.v2.proto.services import (
    campaign_budget_service_pb2 as campaign_budget_service_pb2,
)

CampaignBudgetServicePb2 = campaign_budget_service_pb2
CampaignBudgetOperation = campaign_budget_service_pb2.CampaignBudgetOperation
GetCampaignBudgetRequest = campaign_budget_service_pb2.GetCampaignBudgetRequest
MutateCampaignBudgetResult = campaign_budget_service_pb2.MutateCampaignBudgetResult
MutateCampaignBudgetsRequest = campaign_budget_service_pb2.MutateCampaignBudgetsRequest
MutateCampaignBudgetsResponse = (
    campaign_budget_service_pb2.MutateCampaignBudgetsResponse
)

from google.ads.google_ads.v2.proto.services import (
    campaign_criterion_service_pb2 as campaign_criterion_service_pb2,
)

CampaignCriterionServicePb2 = campaign_criterion_service_pb2
CampaignCriterionOperation = campaign_criterion_service_pb2.CampaignCriterionOperation
GetCampaignCriterionRequest = campaign_criterion_service_pb2.GetCampaignCriterionRequest
MutateCampaignCriteriaRequest = (
    campaign_criterion_service_pb2.MutateCampaignCriteriaRequest
)
MutateCampaignCriteriaResponse = (
    campaign_criterion_service_pb2.MutateCampaignCriteriaResponse
)
MutateCampaignCriterionResult = (
    campaign_criterion_service_pb2.MutateCampaignCriterionResult
)

from google.ads.google_ads.v2.proto.services import (
    campaign_criterion_simulation_service_pb2 as campaign_criterion_simulation_service_pb2,
)

CampaignCriterionSimulationServicePb2 = campaign_criterion_simulation_service_pb2
GetCampaignCriterionSimulationRequest = (
    campaign_criterion_simulation_service_pb2.GetCampaignCriterionSimulationRequest
)

from google.ads.google_ads.v2.proto.services import (
    campaign_draft_service_pb2 as campaign_draft_service_pb2,
)

CampaignDraftServicePb2 = campaign_draft_service_pb2
CampaignDraftOperation = campaign_draft_service_pb2.CampaignDraftOperation
GetCampaignDraftRequest = campaign_draft_service_pb2.GetCampaignDraftRequest
ListCampaignDraftAsyncErrorsRequest = (
    campaign_draft_service_pb2.ListCampaignDraftAsyncErrorsRequest
)
ListCampaignDraftAsyncErrorsResponse = (
    campaign_draft_service_pb2.ListCampaignDraftAsyncErrorsResponse
)
MutateCampaignDraftResult = campaign_draft_service_pb2.MutateCampaignDraftResult
MutateCampaignDraftsRequest = campaign_draft_service_pb2.MutateCampaignDraftsRequest
MutateCampaignDraftsResponse = campaign_draft_service_pb2.MutateCampaignDraftsResponse
PromoteCampaignDraftRequest = campaign_draft_service_pb2.PromoteCampaignDraftRequest

from google.ads.google_ads.v2.proto.services import (
    campaign_experiment_service_pb2 as campaign_experiment_service_pb2,
)

CampaignExperimentServicePb2 = campaign_experiment_service_pb2
CampaignExperimentOperation = (
    campaign_experiment_service_pb2.CampaignExperimentOperation
)
CreateCampaignExperimentMetadata = (
    campaign_experiment_service_pb2.CreateCampaignExperimentMetadata
)
CreateCampaignExperimentRequest = (
    campaign_experiment_service_pb2.CreateCampaignExperimentRequest
)
EndCampaignExperimentRequest = (
    campaign_experiment_service_pb2.EndCampaignExperimentRequest
)
GetCampaignExperimentRequest = (
    campaign_experiment_service_pb2.GetCampaignExperimentRequest
)
GraduateCampaignExperimentRequest = (
    campaign_experiment_service_pb2.GraduateCampaignExperimentRequest
)
GraduateCampaignExperimentResponse = (
    campaign_experiment_service_pb2.GraduateCampaignExperimentResponse
)
ListCampaignExperimentAsyncErrorsRequest = (
    campaign_experiment_service_pb2.ListCampaignExperimentAsyncErrorsRequest
)
ListCampaignExperimentAsyncErrorsResponse = (
    campaign_experiment_service_pb2.ListCampaignExperimentAsyncErrorsResponse
)
MutateCampaignExperimentResult = (
    campaign_experiment_service_pb2.MutateCampaignExperimentResult
)
MutateCampaignExperimentsRequest = (
    campaign_experiment_service_pb2.MutateCampaignExperimentsRequest
)
MutateCampaignExperimentsResponse = (
    campaign_experiment_service_pb2.MutateCampaignExperimentsResponse
)
PromoteCampaignExperimentRequest = (
    campaign_experiment_service_pb2.PromoteCampaignExperimentRequest
)

from google.ads.google_ads.v2.proto.services import (
    campaign_extension_setting_service_pb2 as campaign_extension_setting_service_pb2,
)

CampaignExtensionSettingServicePb2 = campaign_extension_setting_service_pb2
CampaignExtensionSettingOperation = (
    campaign_extension_setting_service_pb2.CampaignExtensionSettingOperation
)
GetCampaignExtensionSettingRequest = (
    campaign_extension_setting_service_pb2.GetCampaignExtensionSettingRequest
)
MutateCampaignExtensionSettingResult = (
    campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingResult
)
MutateCampaignExtensionSettingsRequest = (
    campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsRequest
)
MutateCampaignExtensionSettingsResponse = (
    campaign_extension_setting_service_pb2.MutateCampaignExtensionSettingsResponse
)

from google.ads.google_ads.v2.proto.services import (
    campaign_feed_service_pb2 as campaign_feed_service_pb2,
)

CampaignFeedServicePb2 = campaign_feed_service_pb2
CampaignFeedOperation = campaign_feed_service_pb2.CampaignFeedOperation
GetCampaignFeedRequest = campaign_feed_service_pb2.GetCampaignFeedRequest
MutateCampaignFeedResult = campaign_feed_service_pb2.MutateCampaignFeedResult
MutateCampaignFeedsRequest = campaign_feed_service_pb2.MutateCampaignFeedsRequest
MutateCampaignFeedsResponse = campaign_feed_service_pb2.MutateCampaignFeedsResponse

from google.ads.google_ads.v2.proto.services import (
    campaign_label_service_pb2 as campaign_label_service_pb2,
)

CampaignLabelServicePb2 = campaign_label_service_pb2
CampaignLabelOperation = campaign_label_service_pb2.CampaignLabelOperation
GetCampaignLabelRequest = campaign_label_service_pb2.GetCampaignLabelRequest
MutateCampaignLabelResult = campaign_label_service_pb2.MutateCampaignLabelResult
MutateCampaignLabelsRequest = campaign_label_service_pb2.MutateCampaignLabelsRequest
MutateCampaignLabelsResponse = campaign_label_service_pb2.MutateCampaignLabelsResponse

from google.ads.google_ads.v2.proto.services import (
    campaign_service_pb2 as campaign_service_pb2,
)

CampaignServicePb2 = campaign_service_pb2
CampaignOperation = campaign_service_pb2.CampaignOperation
GetCampaignRequest = campaign_service_pb2.GetCampaignRequest
MutateCampaignResult = campaign_service_pb2.MutateCampaignResult
MutateCampaignsRequest = campaign_service_pb2.MutateCampaignsRequest
MutateCampaignsResponse = campaign_service_pb2.MutateCampaignsResponse

from google.ads.google_ads.v2.proto.services import (
    campaign_shared_set_service_pb2 as campaign_shared_set_service_pb2,
)

CampaignSharedSetServicePb2 = campaign_shared_set_service_pb2
CampaignSharedSetOperation = campaign_shared_set_service_pb2.CampaignSharedSetOperation
GetCampaignSharedSetRequest = (
    campaign_shared_set_service_pb2.GetCampaignSharedSetRequest
)
MutateCampaignSharedSetResult = (
    campaign_shared_set_service_pb2.MutateCampaignSharedSetResult
)
MutateCampaignSharedSetsRequest = (
    campaign_shared_set_service_pb2.MutateCampaignSharedSetsRequest
)
MutateCampaignSharedSetsResponse = (
    campaign_shared_set_service_pb2.MutateCampaignSharedSetsResponse
)

from google.ads.google_ads.v2.proto.services import (
    carrier_constant_service_pb2 as carrier_constant_service_pb2,
)

CarrierConstantServicePb2 = carrier_constant_service_pb2
GetCarrierConstantRequest = carrier_constant_service_pb2.GetCarrierConstantRequest

from google.ads.google_ads.v2.proto.services import (
    change_status_service_pb2 as change_status_service_pb2,
)

ChangeStatusServicePb2 = change_status_service_pb2
GetChangeStatusRequest = change_status_service_pb2.GetChangeStatusRequest

from google.ads.google_ads.v2.proto.services import (
    click_view_service_pb2 as click_view_service_pb2,
)

ClickViewServicePb2 = click_view_service_pb2
GetClickViewRequest = click_view_service_pb2.GetClickViewRequest

from google.ads.google_ads.v2.proto.services import (
    conversion_action_service_pb2 as conversion_action_service_pb2,
)

ConversionActionServicePb2 = conversion_action_service_pb2
ConversionActionOperation = conversion_action_service_pb2.ConversionActionOperation
GetConversionActionRequest = conversion_action_service_pb2.GetConversionActionRequest
MutateConversionActionResult = (
    conversion_action_service_pb2.MutateConversionActionResult
)
MutateConversionActionsRequest = (
    conversion_action_service_pb2.MutateConversionActionsRequest
)
MutateConversionActionsResponse = (
    conversion_action_service_pb2.MutateConversionActionsResponse
)

from google.ads.google_ads.v2.proto.services import (
    conversion_adjustment_upload_service_pb2 as conversion_adjustment_upload_service_pb2,
)

ConversionAdjustmentUploadServicePb2 = conversion_adjustment_upload_service_pb2
ConversionAdjustment = conversion_adjustment_upload_service_pb2.ConversionAdjustment
ConversionAdjustmentResult = (
    conversion_adjustment_upload_service_pb2.ConversionAdjustmentResult
)
GclidDateTimePair = conversion_adjustment_upload_service_pb2.GclidDateTimePair
RestatementValue = conversion_adjustment_upload_service_pb2.RestatementValue
UploadConversionAdjustmentsRequest = (
    conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsRequest
)
UploadConversionAdjustmentsResponse = (
    conversion_adjustment_upload_service_pb2.UploadConversionAdjustmentsResponse
)

from google.ads.google_ads.v2.proto.services import (
    conversion_upload_service_pb2 as conversion_upload_service_pb2,
)

ConversionUploadServicePb2 = conversion_upload_service_pb2
CallConversion = conversion_upload_service_pb2.CallConversion
CallConversionResult = conversion_upload_service_pb2.CallConversionResult
ClickConversion = conversion_upload_service_pb2.ClickConversion
ClickConversionResult = conversion_upload_service_pb2.ClickConversionResult
ExternalAttributionData = conversion_upload_service_pb2.ExternalAttributionData
UploadCallConversionsRequest = (
    conversion_upload_service_pb2.UploadCallConversionsRequest
)
UploadCallConversionsResponse = (
    conversion_upload_service_pb2.UploadCallConversionsResponse
)
UploadClickConversionsRequest = (
    conversion_upload_service_pb2.UploadClickConversionsRequest
)
UploadClickConversionsResponse = (
    conversion_upload_service_pb2.UploadClickConversionsResponse
)

from google.ads.google_ads.v2.proto.services import (
    currency_constant_service_pb2 as currency_constant_service_pb2,
)

CurrencyConstantServicePb2 = currency_constant_service_pb2

from google.ads.google_ads.v2.proto.services import (
    custom_interest_service_pb2 as custom_interest_service_pb2,
)

CustomInterestServicePb2 = custom_interest_service_pb2
CustomInterestOperation = custom_interest_service_pb2.CustomInterestOperation
GetCustomInterestRequest = custom_interest_service_pb2.GetCustomInterestRequest
MutateCustomInterestResult = custom_interest_service_pb2.MutateCustomInterestResult
MutateCustomInterestsRequest = custom_interest_service_pb2.MutateCustomInterestsRequest
MutateCustomInterestsResponse = (
    custom_interest_service_pb2.MutateCustomInterestsResponse
)

from google.ads.google_ads.v2.proto.services import (
    customer_client_link_service_pb2 as customer_client_link_service_pb2,
)

CustomerClientLinkServicePb2 = customer_client_link_service_pb2
CustomerClientLinkOperation = (
    customer_client_link_service_pb2.CustomerClientLinkOperation
)
GetCustomerClientLinkRequest = (
    customer_client_link_service_pb2.GetCustomerClientLinkRequest
)
MutateCustomerClientLinkRequest = (
    customer_client_link_service_pb2.MutateCustomerClientLinkRequest
)
MutateCustomerClientLinkResponse = (
    customer_client_link_service_pb2.MutateCustomerClientLinkResponse
)
MutateCustomerClientLinkResult = (
    customer_client_link_service_pb2.MutateCustomerClientLinkResult
)

from google.ads.google_ads.v2.proto.services import (
    customer_client_service_pb2 as customer_client_service_pb2,
)

CustomerClientServicePb2 = customer_client_service_pb2
GetCustomerClientRequest = customer_client_service_pb2.GetCustomerClientRequest

from google.ads.google_ads.v2.proto.services import (
    customer_extension_setting_service_pb2 as customer_extension_setting_service_pb2,
)

CustomerExtensionSettingServicePb2 = customer_extension_setting_service_pb2
CustomerExtensionSettingOperation = (
    customer_extension_setting_service_pb2.CustomerExtensionSettingOperation
)
GetCustomerExtensionSettingRequest = (
    customer_extension_setting_service_pb2.GetCustomerExtensionSettingRequest
)
MutateCustomerExtensionSettingResult = (
    customer_extension_setting_service_pb2.MutateCustomerExtensionSettingResult
)
MutateCustomerExtensionSettingsRequest = (
    customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsRequest
)
MutateCustomerExtensionSettingsResponse = (
    customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsResponse
)

from google.ads.google_ads.v2.proto.services import (
    customer_feed_service_pb2 as customer_feed_service_pb2,
)

CustomerFeedServicePb2 = customer_feed_service_pb2
CustomerFeedOperation = customer_feed_service_pb2.CustomerFeedOperation
GetCustomerFeedRequest = customer_feed_service_pb2.GetCustomerFeedRequest
MutateCustomerFeedResult = customer_feed_service_pb2.MutateCustomerFeedResult
MutateCustomerFeedsRequest = customer_feed_service_pb2.MutateCustomerFeedsRequest
MutateCustomerFeedsResponse = customer_feed_service_pb2.MutateCustomerFeedsResponse

from google.ads.google_ads.v2.proto.services import (
    customer_label_service_pb2 as customer_label_service_pb2,
)

CustomerLabelServicePb2 = customer_label_service_pb2
CustomerLabelOperation = customer_label_service_pb2.CustomerLabelOperation
GetCustomerLabelRequest = customer_label_service_pb2.GetCustomerLabelRequest
MutateCustomerLabelResult = customer_label_service_pb2.MutateCustomerLabelResult
MutateCustomerLabelsRequest = customer_label_service_pb2.MutateCustomerLabelsRequest
MutateCustomerLabelsResponse = customer_label_service_pb2.MutateCustomerLabelsResponse

from google.ads.google_ads.v2.proto.services import (
    customer_manager_link_service_pb2 as customer_manager_link_service_pb2,
)

CustomerManagerLinkServicePb2 = customer_manager_link_service_pb2
CustomerManagerLinkOperation = (
    customer_manager_link_service_pb2.CustomerManagerLinkOperation
)
GetCustomerManagerLinkRequest = (
    customer_manager_link_service_pb2.GetCustomerManagerLinkRequest
)
MutateCustomerManagerLinkRequest = (
    customer_manager_link_service_pb2.MutateCustomerManagerLinkRequest
)
MutateCustomerManagerLinkResponse = (
    customer_manager_link_service_pb2.MutateCustomerManagerLinkResponse
)
MutateCustomerManagerLinkResult = (
    customer_manager_link_service_pb2.MutateCustomerManagerLinkResult
)

from google.ads.google_ads.v2.proto.services import (
    customer_negative_criterion_service_pb2 as customer_negative_criterion_service_pb2,
)

CustomerNegativeCriterionServicePb2 = customer_negative_criterion_service_pb2
CustomerNegativeCriterionOperation = (
    customer_negative_criterion_service_pb2.CustomerNegativeCriterionOperation
)
GetCustomerNegativeCriterionRequest = (
    customer_negative_criterion_service_pb2.GetCustomerNegativeCriterionRequest
)
MutateCustomerNegativeCriteriaRequest = (
    customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaRequest
)
MutateCustomerNegativeCriteriaResponse = (
    customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaResponse
)
MutateCustomerNegativeCriteriaResult = (
    customer_negative_criterion_service_pb2.MutateCustomerNegativeCriteriaResult
)

from google.ads.google_ads.v2.proto.services import (
    customer_service_pb2 as customer_service_pb2,
)

CustomerServicePb2 = customer_service_pb2
CreateCustomerClientRequest = customer_service_pb2.CreateCustomerClientRequest
CreateCustomerClientResponse = customer_service_pb2.CreateCustomerClientResponse
CustomerOperation = customer_service_pb2.CustomerOperation
GetCustomerRequest = customer_service_pb2.GetCustomerRequest
ListAccessibleCustomersRequest = customer_service_pb2.ListAccessibleCustomersRequest
ListAccessibleCustomersResponse = customer_service_pb2.ListAccessibleCustomersResponse
MutateCustomerRequest = customer_service_pb2.MutateCustomerRequest
MutateCustomerResponse = customer_service_pb2.MutateCustomerResponse
MutateCustomerResult = customer_service_pb2.MutateCustomerResult

from google.ads.google_ads.v2.proto.services import (
    display_keyword_view_service_pb2 as display_keyword_view_service_pb2,
)

DisplayKeywordViewServicePb2 = display_keyword_view_service_pb2
GetDisplayKeywordViewRequest = (
    display_keyword_view_service_pb2.GetDisplayKeywordViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    distance_view_service_pb2 as distance_view_service_pb2,
)

DistanceViewServicePb2 = distance_view_service_pb2
GetDistanceViewRequest = distance_view_service_pb2.GetDistanceViewRequest

from google.ads.google_ads.v2.proto.services import (
    domain_category_service_pb2 as domain_category_service_pb2,
)

DomainCategoryServicePb2 = domain_category_service_pb2
GetDomainCategoryRequest = domain_category_service_pb2.GetDomainCategoryRequest

from google.ads.google_ads.v2.proto.services import (
    dynamic_search_ads_search_term_view_service_pb2 as dynamic_search_ads_search_term_view_service_pb2,
)

DynamicSearchAdsSearchTermViewServicePb2 = (
    dynamic_search_ads_search_term_view_service_pb2
)
GetDynamicSearchAdsSearchTermViewRequest = (
    dynamic_search_ads_search_term_view_service_pb2.GetDynamicSearchAdsSearchTermViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    expanded_landing_page_view_service_pb2 as expanded_landing_page_view_service_pb2,
)

ExpandedLandingPageViewServicePb2 = expanded_landing_page_view_service_pb2
GetExpandedLandingPageViewRequest = (
    expanded_landing_page_view_service_pb2.GetExpandedLandingPageViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    experiment_service_pb2 as experiment_service_pb2,
)

ExperimentServicePb2 = experiment_service_pb2

from google.ads.google_ads.v2.proto.services import (
    extension_feed_item_service_pb2 as extension_feed_item_service_pb2,
)

ExtensionFeedItemServicePb2 = extension_feed_item_service_pb2
ExtensionFeedItemOperation = extension_feed_item_service_pb2.ExtensionFeedItemOperation
GetExtensionFeedItemRequest = (
    extension_feed_item_service_pb2.GetExtensionFeedItemRequest
)
MutateExtensionFeedItemResult = (
    extension_feed_item_service_pb2.MutateExtensionFeedItemResult
)
MutateExtensionFeedItemsRequest = (
    extension_feed_item_service_pb2.MutateExtensionFeedItemsRequest
)
MutateExtensionFeedItemsResponse = (
    extension_feed_item_service_pb2.MutateExtensionFeedItemsResponse
)

from google.ads.google_ads.v2.proto.services import (
    feed_item_service_pb2 as feed_item_service_pb2,
)

FeedItemServicePb2 = feed_item_service_pb2
FeedItemOperation = feed_item_service_pb2.FeedItemOperation
GetFeedItemRequest = feed_item_service_pb2.GetFeedItemRequest
MutateFeedItemResult = feed_item_service_pb2.MutateFeedItemResult
MutateFeedItemsRequest = feed_item_service_pb2.MutateFeedItemsRequest
MutateFeedItemsResponse = feed_item_service_pb2.MutateFeedItemsResponse

from google.ads.google_ads.v2.proto.services import (
    feed_item_target_service_pb2 as feed_item_target_service_pb2,
)

FeedItemTargetServicePb2 = feed_item_target_service_pb2
FeedItemTargetOperation = feed_item_target_service_pb2.FeedItemTargetOperation
GetFeedItemTargetRequest = feed_item_target_service_pb2.GetFeedItemTargetRequest
MutateFeedItemTargetResult = feed_item_target_service_pb2.MutateFeedItemTargetResult
MutateFeedItemTargetsRequest = feed_item_target_service_pb2.MutateFeedItemTargetsRequest
MutateFeedItemTargetsResponse = (
    feed_item_target_service_pb2.MutateFeedItemTargetsResponse
)

from google.ads.google_ads.v2.proto.services import (
    feed_mapping_service_pb2 as feed_mapping_service_pb2,
)

FeedMappingServicePb2 = feed_mapping_service_pb2
FeedMappingOperation = feed_mapping_service_pb2.FeedMappingOperation
GetFeedMappingRequest = feed_mapping_service_pb2.GetFeedMappingRequest
MutateFeedMappingResult = feed_mapping_service_pb2.MutateFeedMappingResult
MutateFeedMappingsRequest = feed_mapping_service_pb2.MutateFeedMappingsRequest
MutateFeedMappingsResponse = feed_mapping_service_pb2.MutateFeedMappingsResponse

from google.ads.google_ads.v2.proto.services import (
    feed_placeholder_view_service_pb2 as feed_placeholder_view_service_pb2,
)

FeedPlaceholderViewServicePb2 = feed_placeholder_view_service_pb2
GetFeedPlaceholderViewRequest = (
    feed_placeholder_view_service_pb2.GetFeedPlaceholderViewRequest
)

from google.ads.google_ads.v2.proto.services import feed_service_pb2 as feed_service_pb2

FeedServicePb2 = feed_service_pb2
FeedOperation = feed_service_pb2.FeedOperation
GetFeedRequest = feed_service_pb2.GetFeedRequest
MutateFeedResult = feed_service_pb2.MutateFeedResult
MutateFeedsRequest = feed_service_pb2.MutateFeedsRequest
MutateFeedsResponse = feed_service_pb2.MutateFeedsResponse

from google.ads.google_ads.v2.proto.services import (
    gender_view_service_pb2 as gender_view_service_pb2,
)

GenderViewServicePb2 = gender_view_service_pb2
GetGenderViewRequest = gender_view_service_pb2.GetGenderViewRequest

from google.ads.google_ads.v2.proto.services import (
    geo_target_constant_service_pb2 as geo_target_constant_service_pb2,
)

GeoTargetConstantServicePb2 = geo_target_constant_service_pb2
GeoTargetConstantSuggestion = (
    geo_target_constant_service_pb2.GeoTargetConstantSuggestion
)
GetGeoTargetConstantRequest = (
    geo_target_constant_service_pb2.GetGeoTargetConstantRequest
)
SuggestGeoTargetConstantsRequest = (
    geo_target_constant_service_pb2.SuggestGeoTargetConstantsRequest
)
SuggestGeoTargetConstantsResponse = (
    geo_target_constant_service_pb2.SuggestGeoTargetConstantsResponse
)

from google.ads.google_ads.v2.proto.services import (
    geographic_view_service_pb2 as geographic_view_service_pb2,
)

GeographicViewServicePb2 = geographic_view_service_pb2
GetGeographicViewRequest = geographic_view_service_pb2.GetGeographicViewRequest

from google.ads.google_ads.v2.proto.services import (
    google_ads_field_service_pb2 as google_ads_field_service_pb2,
)

GoogleAdsFieldServicePb2 = google_ads_field_service_pb2
GetGoogleAdsFieldRequest = google_ads_field_service_pb2.GetGoogleAdsFieldRequest
SearchGoogleAdsFieldsRequest = google_ads_field_service_pb2.SearchGoogleAdsFieldsRequest
SearchGoogleAdsFieldsResponse = (
    google_ads_field_service_pb2.SearchGoogleAdsFieldsResponse
)

from google.ads.google_ads.v2.proto.services import (
    google_ads_service_pb2 as google_ads_service_pb2,
)

GoogleAdsServicePb2 = google_ads_service_pb2
GoogleAdsRow = google_ads_service_pb2.GoogleAdsRow
MutateGoogleAdsRequest = google_ads_service_pb2.MutateGoogleAdsRequest
MutateGoogleAdsResponse = google_ads_service_pb2.MutateGoogleAdsResponse
MutateOperation = google_ads_service_pb2.MutateOperation
MutateOperationResponse = google_ads_service_pb2.MutateOperationResponse
SearchGoogleAdsRequest = google_ads_service_pb2.SearchGoogleAdsRequest
SearchGoogleAdsResponse = google_ads_service_pb2.SearchGoogleAdsResponse

from google.ads.google_ads.v2.proto.services import (
    hotel_group_view_service_pb2 as hotel_group_view_service_pb2,
)

HotelGroupViewServicePb2 = hotel_group_view_service_pb2
GetHotelGroupViewRequest = hotel_group_view_service_pb2.GetHotelGroupViewRequest

from google.ads.google_ads.v2.proto.services import (
    hotel_performance_view_service_pb2 as hotel_performance_view_service_pb2,
)

HotelPerformanceViewServicePb2 = hotel_performance_view_service_pb2
GetHotelPerformanceViewRequest = (
    hotel_performance_view_service_pb2.GetHotelPerformanceViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    invoice_service_pb2 as invoice_service_pb2,
)

InvoiceServicePb2 = invoice_service_pb2
ListInvoicesRequest = invoice_service_pb2.ListInvoicesRequest
ListInvoicesResponse = invoice_service_pb2.ListInvoicesResponse

from google.ads.google_ads.v2.proto.services import (
    keyword_plan_ad_group_service_pb2 as keyword_plan_ad_group_service_pb2,
)

KeywordPlanAdGroupServicePb2 = keyword_plan_ad_group_service_pb2
GetKeywordPlanAdGroupRequest = (
    keyword_plan_ad_group_service_pb2.GetKeywordPlanAdGroupRequest
)
KeywordPlanAdGroupOperation = (
    keyword_plan_ad_group_service_pb2.KeywordPlanAdGroupOperation
)
MutateKeywordPlanAdGroupResult = (
    keyword_plan_ad_group_service_pb2.MutateKeywordPlanAdGroupResult
)
MutateKeywordPlanAdGroupsRequest = (
    keyword_plan_ad_group_service_pb2.MutateKeywordPlanAdGroupsRequest
)
MutateKeywordPlanAdGroupsResponse = (
    keyword_plan_ad_group_service_pb2.MutateKeywordPlanAdGroupsResponse
)

from google.ads.google_ads.v2.proto.services import (
    keyword_plan_campaign_service_pb2 as keyword_plan_campaign_service_pb2,
)

KeywordPlanCampaignServicePb2 = keyword_plan_campaign_service_pb2
GetKeywordPlanCampaignRequest = (
    keyword_plan_campaign_service_pb2.GetKeywordPlanCampaignRequest
)
KeywordPlanCampaignOperation = (
    keyword_plan_campaign_service_pb2.KeywordPlanCampaignOperation
)
MutateKeywordPlanCampaignResult = (
    keyword_plan_campaign_service_pb2.MutateKeywordPlanCampaignResult
)
MutateKeywordPlanCampaignsRequest = (
    keyword_plan_campaign_service_pb2.MutateKeywordPlanCampaignsRequest
)
MutateKeywordPlanCampaignsResponse = (
    keyword_plan_campaign_service_pb2.MutateKeywordPlanCampaignsResponse
)

from google.ads.google_ads.v2.proto.services import (
    keyword_plan_idea_service_pb2 as keyword_plan_idea_service_pb2,
)

KeywordPlanIdeaServicePb2 = keyword_plan_idea_service_pb2
GenerateKeywordIdeaResponse = keyword_plan_idea_service_pb2.GenerateKeywordIdeaResponse
GenerateKeywordIdeaResult = keyword_plan_idea_service_pb2.GenerateKeywordIdeaResult
GenerateKeywordIdeasRequest = keyword_plan_idea_service_pb2.GenerateKeywordIdeasRequest
KeywordAndUrlSeed = keyword_plan_idea_service_pb2.KeywordAndUrlSeed
KeywordSeed = keyword_plan_idea_service_pb2.KeywordSeed
UrlSeed = keyword_plan_idea_service_pb2.UrlSeed

from google.ads.google_ads.v2.proto.services import (
    keyword_plan_keyword_service_pb2 as keyword_plan_keyword_service_pb2,
)

KeywordPlanKeywordServicePb2 = keyword_plan_keyword_service_pb2
GetKeywordPlanKeywordRequest = (
    keyword_plan_keyword_service_pb2.GetKeywordPlanKeywordRequest
)
KeywordPlanKeywordOperation = (
    keyword_plan_keyword_service_pb2.KeywordPlanKeywordOperation
)
MutateKeywordPlanKeywordResult = (
    keyword_plan_keyword_service_pb2.MutateKeywordPlanKeywordResult
)
MutateKeywordPlanKeywordsRequest = (
    keyword_plan_keyword_service_pb2.MutateKeywordPlanKeywordsRequest
)
MutateKeywordPlanKeywordsResponse = (
    keyword_plan_keyword_service_pb2.MutateKeywordPlanKeywordsResponse
)

from google.ads.google_ads.v2.proto.services import (
    keyword_plan_negative_keyword_service_pb2 as keyword_plan_negative_keyword_service_pb2,
)

KeywordPlanNegativeKeywordServicePb2 = keyword_plan_negative_keyword_service_pb2
GetKeywordPlanNegativeKeywordRequest = (
    keyword_plan_negative_keyword_service_pb2.GetKeywordPlanNegativeKeywordRequest
)
KeywordPlanNegativeKeywordOperation = (
    keyword_plan_negative_keyword_service_pb2.KeywordPlanNegativeKeywordOperation
)
MutateKeywordPlanNegativeKeywordResult = (
    keyword_plan_negative_keyword_service_pb2.MutateKeywordPlanNegativeKeywordResult
)
MutateKeywordPlanNegativeKeywordsRequest = (
    keyword_plan_negative_keyword_service_pb2.MutateKeywordPlanNegativeKeywordsRequest
)
MutateKeywordPlanNegativeKeywordsResponse = (
    keyword_plan_negative_keyword_service_pb2.MutateKeywordPlanNegativeKeywordsResponse
)

from google.ads.google_ads.v2.proto.services import (
    keyword_plan_service_pb2 as keyword_plan_service_pb2,
)

KeywordPlanServicePb2 = keyword_plan_service_pb2
ForecastMetrics = keyword_plan_service_pb2.ForecastMetrics
GenerateForecastMetricsRequest = keyword_plan_service_pb2.GenerateForecastMetricsRequest
GenerateForecastMetricsResponse = (
    keyword_plan_service_pb2.GenerateForecastMetricsResponse
)
GenerateHistoricalMetricsRequest = (
    keyword_plan_service_pb2.GenerateHistoricalMetricsRequest
)
GenerateHistoricalMetricsResponse = (
    keyword_plan_service_pb2.GenerateHistoricalMetricsResponse
)
GetKeywordPlanRequest = keyword_plan_service_pb2.GetKeywordPlanRequest
KeywordPlanAdGroupForecast = keyword_plan_service_pb2.KeywordPlanAdGroupForecast
KeywordPlanCampaignForecast = keyword_plan_service_pb2.KeywordPlanCampaignForecast
KeywordPlanKeywordForecast = keyword_plan_service_pb2.KeywordPlanKeywordForecast
KeywordPlanKeywordHistoricalMetrics = (
    keyword_plan_service_pb2.KeywordPlanKeywordHistoricalMetrics
)
KeywordPlanOperation = keyword_plan_service_pb2.KeywordPlanOperation
MutateKeywordPlansRequest = keyword_plan_service_pb2.MutateKeywordPlansRequest
MutateKeywordPlansResponse = keyword_plan_service_pb2.MutateKeywordPlansResponse
MutateKeywordPlansResult = keyword_plan_service_pb2.MutateKeywordPlansResult

from google.ads.google_ads.v2.proto.services import (
    keyword_view_service_pb2 as keyword_view_service_pb2,
)

KeywordViewServicePb2 = keyword_view_service_pb2
GetKeywordViewRequest = keyword_view_service_pb2.GetKeywordViewRequest

from google.ads.google_ads.v2.proto.services import (
    label_service_pb2 as label_service_pb2,
)

LabelServicePb2 = label_service_pb2
GetLabelRequest = label_service_pb2.GetLabelRequest
LabelOperation = label_service_pb2.LabelOperation
MutateLabelResult = label_service_pb2.MutateLabelResult
MutateLabelsRequest = label_service_pb2.MutateLabelsRequest
MutateLabelsResponse = label_service_pb2.MutateLabelsResponse

from google.ads.google_ads.v2.proto.services import (
    landing_page_view_service_pb2 as landing_page_view_service_pb2,
)

LandingPageViewServicePb2 = landing_page_view_service_pb2
GetLandingPageViewRequest = landing_page_view_service_pb2.GetLandingPageViewRequest

from google.ads.google_ads.v2.proto.services import (
    language_constant_service_pb2 as language_constant_service_pb2,
)

LanguageConstantServicePb2 = language_constant_service_pb2
GetLanguageConstantRequest = language_constant_service_pb2.GetLanguageConstantRequest

from google.ads.google_ads.v2.proto.services import (
    location_view_service_pb2 as location_view_service_pb2,
)

LocationViewServicePb2 = location_view_service_pb2
GetLocationViewRequest = location_view_service_pb2.GetLocationViewRequest

from google.ads.google_ads.v2.proto.services import (
    managed_placement_view_service_pb2 as managed_placement_view_service_pb2,
)

ManagedPlacementViewServicePb2 = managed_placement_view_service_pb2
GetManagedPlacementViewRequest = (
    managed_placement_view_service_pb2.GetManagedPlacementViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    media_file_service_pb2 as media_file_service_pb2,
)

MediaFileServicePb2 = media_file_service_pb2
GetMediaFileRequest = media_file_service_pb2.GetMediaFileRequest
MediaFileOperation = media_file_service_pb2.MediaFileOperation
MutateMediaFileResult = media_file_service_pb2.MutateMediaFileResult
MutateMediaFilesRequest = media_file_service_pb2.MutateMediaFilesRequest
MutateMediaFilesResponse = media_file_service_pb2.MutateMediaFilesResponse

from google.ads.google_ads.v2.proto.services import (
    merchant_center_link_service_pb2 as merchant_center_link_service_pb2,
)

MerchantCenterLinkServicePb2 = merchant_center_link_service_pb2
GetMerchantCenterLinkRequest = (
    merchant_center_link_service_pb2.GetMerchantCenterLinkRequest
)
ListMerchantCenterLinksRequest = (
    merchant_center_link_service_pb2.ListMerchantCenterLinksRequest
)
ListMerchantCenterLinksResponse = (
    merchant_center_link_service_pb2.ListMerchantCenterLinksResponse
)
MerchantCenterLinkOperation = (
    merchant_center_link_service_pb2.MerchantCenterLinkOperation
)
MutateMerchantCenterLinkRequest = (
    merchant_center_link_service_pb2.MutateMerchantCenterLinkRequest
)
MutateMerchantCenterLinkResponse = (
    merchant_center_link_service_pb2.MutateMerchantCenterLinkResponse
)
MutateMerchantCenterLinkResult = (
    merchant_center_link_service_pb2.MutateMerchantCenterLinkResult
)

from google.ads.google_ads.v2.proto.services import (
    mobile_app_category_constant_service_pb2 as mobile_app_category_constant_service_pb2,
)

MobileAppCategoryConstantServicePb2 = mobile_app_category_constant_service_pb2
GetMobileAppCategoryConstantRequest = (
    mobile_app_category_constant_service_pb2.GetMobileAppCategoryConstantRequest
)

from google.ads.google_ads.v2.proto.services import (
    mobile_device_constant_service_pb2 as mobile_device_constant_service_pb2,
)

MobileDeviceConstantServicePb2 = mobile_device_constant_service_pb2
GetMobileDeviceConstantRequest = (
    mobile_device_constant_service_pb2.GetMobileDeviceConstantRequest
)

from google.ads.google_ads.v2.proto.services import (
    mutate_job_service_pb2 as mutate_job_service_pb2,
)

MutateJobServicePb2 = mutate_job_service_pb2
AddMutateJobOperationsRequest = mutate_job_service_pb2.AddMutateJobOperationsRequest
AddMutateJobOperationsResponse = mutate_job_service_pb2.AddMutateJobOperationsResponse
CreateMutateJobRequest = mutate_job_service_pb2.CreateMutateJobRequest
CreateMutateJobResponse = mutate_job_service_pb2.CreateMutateJobResponse
GetMutateJobRequest = mutate_job_service_pb2.GetMutateJobRequest
ListMutateJobResultsRequest = mutate_job_service_pb2.ListMutateJobResultsRequest
ListMutateJobResultsResponse = mutate_job_service_pb2.ListMutateJobResultsResponse
MutateJobResult = mutate_job_service_pb2.MutateJobResult
RunMutateJobRequest = mutate_job_service_pb2.RunMutateJobRequest

from google.ads.google_ads.v2.proto.services import (
    offline_user_data_job_service_pb2 as offline_user_data_job_service_pb2,
)

OfflineUserDataJobServicePb2 = offline_user_data_job_service_pb2

from google.ads.google_ads.v2.proto.services import (
    operating_system_version_constant_service_pb2 as operating_system_version_constant_service_pb2,
)

OperatingSystemVersionConstantServicePb2 = operating_system_version_constant_service_pb2
GetOperatingSystemVersionConstantRequest = (
    operating_system_version_constant_service_pb2.GetOperatingSystemVersionConstantRequest
)

from google.ads.google_ads.v2.proto.services import (
    paid_organic_search_term_view_service_pb2 as paid_organic_search_term_view_service_pb2,
)

PaidOrganicSearchTermViewServicePb2 = paid_organic_search_term_view_service_pb2
GetPaidOrganicSearchTermViewRequest = (
    paid_organic_search_term_view_service_pb2.GetPaidOrganicSearchTermViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    parental_status_view_service_pb2 as parental_status_view_service_pb2,
)

ParentalStatusViewServicePb2 = parental_status_view_service_pb2
GetParentalStatusViewRequest = (
    parental_status_view_service_pb2.GetParentalStatusViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    payments_account_service_pb2 as payments_account_service_pb2,
)

PaymentsAccountServicePb2 = payments_account_service_pb2
ListPaymentsAccountsRequest = payments_account_service_pb2.ListPaymentsAccountsRequest
ListPaymentsAccountsResponse = payments_account_service_pb2.ListPaymentsAccountsResponse

from google.ads.google_ads.v2.proto.services import (
    product_bidding_category_constant_service_pb2 as product_bidding_category_constant_service_pb2,
)

ProductBiddingCategoryConstantServicePb2 = product_bidding_category_constant_service_pb2
GetProductBiddingCategoryConstantRequest = (
    product_bidding_category_constant_service_pb2.GetProductBiddingCategoryConstantRequest
)

from google.ads.google_ads.v2.proto.services import (
    product_group_view_service_pb2 as product_group_view_service_pb2,
)

ProductGroupViewServicePb2 = product_group_view_service_pb2
GetProductGroupViewRequest = product_group_view_service_pb2.GetProductGroupViewRequest

from google.ads.google_ads.v2.proto.services import (
    reach_plan_service_pb2 as reach_plan_service_pb2,
)

ReachPlanServicePb2 = reach_plan_service_pb2
CampaignDuration = reach_plan_service_pb2.CampaignDuration
Forecast = reach_plan_service_pb2.Forecast
GenerateProductMixIdeasRequest = reach_plan_service_pb2.GenerateProductMixIdeasRequest
GenerateProductMixIdeasResponse = reach_plan_service_pb2.GenerateProductMixIdeasResponse
GenerateReachForecastRequest = reach_plan_service_pb2.GenerateReachForecastRequest
GenerateReachForecastResponse = reach_plan_service_pb2.GenerateReachForecastResponse
ListPlannableLocationsRequest = reach_plan_service_pb2.ListPlannableLocationsRequest
ListPlannableLocationsResponse = reach_plan_service_pb2.ListPlannableLocationsResponse
ListPlannableProductsRequest = reach_plan_service_pb2.ListPlannableProductsRequest
ListPlannableProductsResponse = reach_plan_service_pb2.ListPlannableProductsResponse
OnTargetAudienceMetrics = reach_plan_service_pb2.OnTargetAudienceMetrics
PlannableLocation = reach_plan_service_pb2.PlannableLocation
PlannableTargeting = reach_plan_service_pb2.PlannableTargeting
PlannedProduct = reach_plan_service_pb2.PlannedProduct
Preferences = reach_plan_service_pb2.Preferences
ProductAllocation = reach_plan_service_pb2.ProductAllocation
ProductMetadata = reach_plan_service_pb2.ProductMetadata
ReachCurve = reach_plan_service_pb2.ReachCurve
ReachForecast = reach_plan_service_pb2.ReachForecast
Targeting = reach_plan_service_pb2.Targeting

from google.ads.google_ads.v2.proto.services import (
    recommendation_service_pb2 as recommendation_service_pb2,
)

RecommendationServicePb2 = recommendation_service_pb2
ApplyRecommendationOperation = recommendation_service_pb2.ApplyRecommendationOperation
ApplyRecommendationRequest = recommendation_service_pb2.ApplyRecommendationRequest
ApplyRecommendationResponse = recommendation_service_pb2.ApplyRecommendationResponse
ApplyRecommendationResult = recommendation_service_pb2.ApplyRecommendationResult
DismissRecommendationRequest = recommendation_service_pb2.DismissRecommendationRequest
DismissRecommendationResponse = recommendation_service_pb2.DismissRecommendationResponse
GetRecommendationRequest = recommendation_service_pb2.GetRecommendationRequest

from google.ads.google_ads.v2.proto.services import (
    remarketing_action_service_pb2 as remarketing_action_service_pb2,
)

RemarketingActionServicePb2 = remarketing_action_service_pb2
GetRemarketingActionRequest = remarketing_action_service_pb2.GetRemarketingActionRequest
MutateRemarketingActionResult = (
    remarketing_action_service_pb2.MutateRemarketingActionResult
)
MutateRemarketingActionsRequest = (
    remarketing_action_service_pb2.MutateRemarketingActionsRequest
)
MutateRemarketingActionsResponse = (
    remarketing_action_service_pb2.MutateRemarketingActionsResponse
)
RemarketingActionOperation = remarketing_action_service_pb2.RemarketingActionOperation

from google.ads.google_ads.v2.proto.services import (
    search_term_view_service_pb2 as search_term_view_service_pb2,
)

SearchTermViewServicePb2 = search_term_view_service_pb2
GetSearchTermViewRequest = search_term_view_service_pb2.GetSearchTermViewRequest

from google.ads.google_ads.v2.proto.services import (
    shared_criterion_service_pb2 as shared_criterion_service_pb2,
)

SharedCriterionServicePb2 = shared_criterion_service_pb2
GetSharedCriterionRequest = shared_criterion_service_pb2.GetSharedCriterionRequest
MutateSharedCriteriaRequest = shared_criterion_service_pb2.MutateSharedCriteriaRequest
MutateSharedCriteriaResponse = shared_criterion_service_pb2.MutateSharedCriteriaResponse
MutateSharedCriterionResult = shared_criterion_service_pb2.MutateSharedCriterionResult
SharedCriterionOperation = shared_criterion_service_pb2.SharedCriterionOperation

from google.ads.google_ads.v2.proto.services import (
    shared_set_service_pb2 as shared_set_service_pb2,
)

SharedSetServicePb2 = shared_set_service_pb2
GetSharedSetRequest = shared_set_service_pb2.GetSharedSetRequest
MutateSharedSetResult = shared_set_service_pb2.MutateSharedSetResult
MutateSharedSetsRequest = shared_set_service_pb2.MutateSharedSetsRequest
MutateSharedSetsResponse = shared_set_service_pb2.MutateSharedSetsResponse
SharedSetOperation = shared_set_service_pb2.SharedSetOperation

from google.ads.google_ads.v2.proto.services import (
    shopping_performance_view_service_pb2 as shopping_performance_view_service_pb2,
)

ShoppingPerformanceViewServicePb2 = shopping_performance_view_service_pb2
GetShoppingPerformanceViewRequest = (
    shopping_performance_view_service_pb2.GetShoppingPerformanceViewRequest
)

from google.ads.google_ads.v2.proto.services import (
    topic_constant_service_pb2 as topic_constant_service_pb2,
)

TopicConstantServicePb2 = topic_constant_service_pb2
GetTopicConstantRequest = topic_constant_service_pb2.GetTopicConstantRequest

from google.ads.google_ads.v2.proto.services import (
    topic_view_service_pb2 as topic_view_service_pb2,
)

TopicViewServicePb2 = topic_view_service_pb2
GetTopicViewRequest = topic_view_service_pb2.GetTopicViewRequest

from google.ads.google_ads.v2.proto.services import (
    user_interest_service_pb2 as user_interest_service_pb2,
)

UserInterestServicePb2 = user_interest_service_pb2
GetUserInterestRequest = user_interest_service_pb2.GetUserInterestRequest

from google.ads.google_ads.v2.proto.services import (
    user_list_service_pb2 as user_list_service_pb2,
)

UserListServicePb2 = user_list_service_pb2
GetUserListRequest = user_list_service_pb2.GetUserListRequest
MutateUserListResult = user_list_service_pb2.MutateUserListResult
MutateUserListsRequest = user_list_service_pb2.MutateUserListsRequest
MutateUserListsResponse = user_list_service_pb2.MutateUserListsResponse
UserListOperation = user_list_service_pb2.UserListOperation

from google.ads.google_ads.v2.proto.services import (
    user_location_view_service_pb2 as user_location_view_service_pb2,
)

UserLocationViewServicePb2 = user_location_view_service_pb2
GetUserLocationViewRequest = user_location_view_service_pb2.GetUserLocationViewRequest

from google.ads.google_ads.v2.proto.services import (
    video_service_pb2 as video_service_pb2,
)

VideoServicePb2 = video_service_pb2
GetVideoRequest = video_service_pb2.GetVideoRequest

from google.longrunning import operations_pb2 as operations_pb2

OperationsPb2 = operations_pb2
CancelOperationRequest = operations_pb2.CancelOperationRequest
DeleteOperationRequest = operations_pb2.DeleteOperationRequest
GetOperationRequest = operations_pb2.GetOperationRequest
ListOperationsRequest = operations_pb2.ListOperationsRequest
ListOperationsResponse = operations_pb2.ListOperationsResponse
Operation = operations_pb2.Operation
OperationInfo = operations_pb2.OperationInfo
OperationsStub = operations_pb2.OperationsStub

from google.protobuf import any_pb2 as any_pb2

AnyPb2 = any_pb2
Any = any_pb2.Any

from google.protobuf import empty_pb2 as empty_pb2

EmptyPb2 = empty_pb2
Empty = empty_pb2.Empty

from google.protobuf import field_mask_pb2 as field_mask_pb2

FieldMaskPb2 = field_mask_pb2
FieldMask = field_mask_pb2.FieldMask

from google.protobuf import wrappers_pb2 as wrappers_pb2

WrappersPb2 = wrappers_pb2
BoolValue = wrappers_pb2.BoolValue
BytesValue = wrappers_pb2.BytesValue
DoubleValue = wrappers_pb2.DoubleValue
FloatValue = wrappers_pb2.FloatValue
Int32Value = wrappers_pb2.Int32Value
Int64Value = wrappers_pb2.Int64Value
StringValue = wrappers_pb2.StringValue
UInt32Value = wrappers_pb2.UInt32Value
UInt64Value = wrappers_pb2.UInt64Value

from google.rpc import status_pb2 as status_pb2

StatusPb2 = status_pb2

__all__ = [
    "AdAssetPb2",
    "AdTypeInfosPb2",
    "AssetTypesPb2",
    "BiddingPb2",
    "ClickLocationPb2",
    "CriteriaPb2",
    "CriterionCategoryAvailabilityPb2",
    "CustomParameterPb2",
    "DatesPb2",
    "ExplorerAutoOptimizerSettingPb2",
    "ExtensionsPb2",
    "FeedCommonPb2",
    "FinalAppUrlPb2",
    "FinalUrlPb2",
    "FrequencyCapPb2",
    "KeywordPlanCommonPb2",
    "MatchingFunctionPb2",
    "MetricsPb2",
    "MutatePb2",
    "OfflineUserDataPb2",
    "PolicyPb2",
    "RealTimeBiddingSettingPb2",
    "SegmentsPb2",
    "SimulationPb2",
    "TagSnippetPb2",
    "TargetingSettingPb2",
    "TextLabelPb2",
    "UrlCollectionPb2",
    "UserListsPb2",
    "ValuePb2",
    "AccessReasonPb2",
    "AccessRolePb2",
    "AccountBudgetProposalStatusPb2",
    "AccountBudgetProposalTypePb2",
    "AccountBudgetStatusPb2",
    "AdCustomizerPlaceholderFieldPb2",
    "AdGroupAdRotationModePb2",
    "AdGroupAdStatusPb2",
    "AdGroupCriterionApprovalStatusPb2",
    "AdGroupCriterionStatusPb2",
    "AdGroupStatusPb2",
    "AdGroupTypePb2",
    "AdNetworkTypePb2",
    "AdServingOptimizationStatusPb2",
    "AdStrengthPb2",
    "AdTypePb2",
    "AdvertisingChannelSubTypePb2",
    "AdvertisingChannelTypePb2",
    "AffiliateLocationFeedRelationshipTypePb2",
    "AffiliateLocationPlaceholderFieldPb2",
    "AgeRangeTypePb2",
    "AppCampaignAppStorePb2",
    "AppCampaignBiddingStrategyGoalTypePb2",
    "AppPaymentModelTypePb2",
    "AppPlaceholderFieldPb2",
    "AppStorePb2",
    "AppUrlOperatingSystemTypePb2",
    "AssetFieldTypePb2",
    "AssetPerformanceLabelPb2",
    "AssetTypePb2",
    "AttributionModelPb2",
    "BidModifierSourcePb2",
    "BiddingSourcePb2",
    "BiddingStrategyStatusPb2",
    "BiddingStrategyTypePb2",
    "BillingSetupStatusPb2",
    "BrandSafetySuitabilityPb2",
    "BudgetDeliveryMethodPb2",
    "BudgetPeriodPb2",
    "BudgetStatusPb2",
    "BudgetTypePb2",
    "CallConversionReportingStatePb2",
    "CallPlaceholderFieldPb2",
    "CalloutPlaceholderFieldPb2",
    "CampaignCriterionStatusPb2",
    "CampaignDraftStatusPb2",
    "CampaignExperimentStatusPb2",
    "CampaignExperimentTrafficSplitTypePb2",
    "CampaignExperimentTypePb2",
    "CampaignServingStatusPb2",
    "CampaignSharedSetStatusPb2",
    "CampaignStatusPb2",
    "ChangeStatusOperationPb2",
    "ChangeStatusResourceTypePb2",
    "ClickTypePb2",
    "ContentLabelTypePb2",
    "ConversionActionCategoryPb2",
    "ConversionActionCountingTypePb2",
    "ConversionActionStatusPb2",
    "ConversionActionTypePb2",
    "ConversionAdjustmentTypePb2",
    "ConversionAttributionEventTypePb2",
    "ConversionLagBucketPb2",
    "ConversionOrAdjustmentLagBucketPb2",
    "CriterionCategoryChannelAvailabilityModePb2",
    "CriterionCategoryLocaleAvailabilityModePb2",
    "CriterionSystemServingStatusPb2",
    "CriterionTypePb2",
    "CustomInterestMemberTypePb2",
    "CustomInterestStatusPb2",
    "CustomInterestTypePb2",
    "CustomPlaceholderFieldPb2",
    "CustomerMatchUploadKeyTypePb2",
    "CustomerPayPerConversionEligibilityFailureReasonPb2",
    "DataDrivenModelStatusPb2",
    "DayOfWeekPb2",
    "DevicePb2",
    "DisplayAdFormatSettingPb2",
    "DisplayUploadProductTypePb2",
    "DistanceBucketPb2",
    "DsaPageFeedCriterionFieldPb2",
    "EducationPlaceholderFieldPb2",
    "ExtensionSettingDevicePb2",
    "ExtensionTypePb2",
    "ExternalConversionSourcePb2",
    "FeedAttributeTypePb2",
    "FeedItemQualityApprovalStatusPb2",
    "FeedItemQualityDisapprovalReasonPb2",
    "FeedItemStatusPb2",
    "FeedItemTargetDevicePb2",
    "FeedItemTargetStatusPb2",
    "FeedItemTargetTypePb2",
    "FeedItemValidationStatusPb2",
    "FeedLinkStatusPb2",
    "FeedMappingCriterionTypePb2",
    "FeedMappingStatusPb2",
    "FeedOriginPb2",
    "FeedStatusPb2",
    "FlightPlaceholderFieldPb2",
    "FrequencyCapEventTypePb2",
    "FrequencyCapLevelPb2",
    "FrequencyCapTimeUnitPb2",
    "GenderTypePb2",
    "GeoTargetConstantStatusPb2",
    "GeoTargetingRestrictionPb2",
    "GeoTargetingTypePb2",
    "GoogleAdsFieldCategoryPb2",
    "GoogleAdsFieldDataTypePb2",
    "HotelDateSelectionTypePb2",
    "HotelPlaceholderFieldPb2",
    "HotelPriceBucketPb2",
    "HotelRateTypePb2",
    "IncomeRangeTypePb2",
    "InteractionEventTypePb2",
    "InteractionTypePb2",
    "InvoiceTypePb2",
    "JobPlaceholderFieldPb2",
    "KeywordMatchTypePb2",
    "KeywordPlanCompetitionLevelPb2",
    "KeywordPlanForecastIntervalPb2",
    "KeywordPlanNetworkPb2",
    "LabelStatusPb2",
    "LegacyAppInstallAdAppStorePb2",
    "ListingCustomAttributeIndexPb2",
    "ListingGroupTypePb2",
    "LocalPlaceholderFieldPb2",
    "LocationExtensionTargetingCriterionFieldPb2",
    "LocationGroupRadiusUnitsPb2",
    "LocationPlaceholderFieldPb2",
    "LocationSourceTypePb2",
    "ManagerLinkStatusPb2",
    "MatchingFunctionContextTypePb2",
    "MatchingFunctionOperatorPb2",
    "MediaTypePb2",
    "MerchantCenterLinkStatusPb2",
    "MessagePlaceholderFieldPb2",
    "MimeTypePb2",
    "MinuteOfHourPb2",
    "MobileDeviceTypePb2",
    "MonthOfYearPb2",
    "MutateJobStatusPb2",
    "NegativeGeoTargetTypePb2",
    "OfflineUserDataJobFailureReasonPb2",
    "OfflineUserDataJobStatusPb2",
    "OfflineUserDataJobTypePb2",
    "OperatingSystemVersionOperatorTypePb2",
    "PageOnePromotedStrategyGoalPb2",
    "ParentalStatusTypePb2",
    "PaymentModePb2",
    "PlaceholderTypePb2",
    "PlacementTypePb2",
    "PolicyApprovalStatusPb2",
    "PolicyReviewStatusPb2",
    "PolicyTopicEntryTypePb2",
    "PolicyTopicEvidenceDestinationMismatchUrlTypePb2",
    "PolicyTopicEvidenceDestinationNotWorkingDevicePb2",
    "PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypePb2",
    "PositiveGeoTargetTypePb2",
    "PreferredContentTypePb2",
    "PriceExtensionPriceQualifierPb2",
    "PriceExtensionPriceUnitPb2",
    "PriceExtensionTypePb2",
    "PricePlaceholderFieldPb2",
    "ProductBiddingCategoryLevelPb2",
    "ProductBiddingCategoryStatusPb2",
    "ProductChannelExclusivityPb2",
    "ProductChannelPb2",
    "ProductConditionPb2",
    "ProductTypeLevelPb2",
    "PromotionExtensionDiscountModifierPb2",
    "PromotionExtensionOccasionPb2",
    "PromotionPlaceholderFieldPb2",
    "ProximityRadiusUnitsPb2",
    "QualityScoreBucketPb2",
    "ReachPlanAdLengthPb2",
    "ReachPlanAgeRangePb2",
    "RealEstatePlaceholderFieldPb2",
    "RecommendationTypePb2",
    "SearchEngineResultsPageTypePb2",
    "SearchTermMatchTypePb2",
    "SearchTermTargetingStatusPb2",
    "ServedAssetFieldTypePb2",
    "SharedSetStatusPb2",
    "SharedSetTypePb2",
    "SimulationModificationMethodPb2",
    "SimulationTypePb2",
    "SitelinkPlaceholderFieldPb2",
    "SlotPb2",
    "SpendingLimitTypePb2",
    "StructuredSnippetPlaceholderFieldPb2",
    "SummaryRowSettingPb2",
    "SystemManagedEntitySourcePb2",
    "TargetCpaOptInRecommendationGoalPb2",
    "TargetImpressionShareLocationPb2",
    "TargetingDimensionPb2",
    "TimeTypePb2",
    "TrackingCodePageFormatPb2",
    "TrackingCodeTypePb2",
    "TravelPlaceholderFieldPb2",
    "UserInterestTaxonomyTypePb2",
    "UserListAccessStatusPb2",
    "UserListClosingReasonPb2",
    "UserListCombinedRuleOperatorPb2",
    "UserListCrmDataSourceTypePb2",
    "UserListDateRuleItemOperatorPb2",
    "UserListLogicalRuleOperatorPb2",
    "UserListMembershipStatusPb2",
    "UserListNumberRuleItemOperatorPb2",
    "UserListPrepopulationStatusPb2",
    "UserListRuleTypePb2",
    "UserListSizeRangePb2",
    "UserListStringRuleItemOperatorPb2",
    "UserListTypePb2",
    "VanityPharmaDisplayUrlModePb2",
    "VanityPharmaTextPb2",
    "WebpageConditionOperandPb2",
    "WebpageConditionOperatorPb2",
    "AccessInvitationErrorPb2",
    "AccountBudgetProposalErrorPb2",
    "AdCustomizerErrorPb2",
    "AdErrorPb2",
    "AdGroupAdErrorPb2",
    "AdGroupBidModifierErrorPb2",
    "AdGroupCriterionErrorPb2",
    "AdGroupErrorPb2",
    "AdGroupFeedErrorPb2",
    "AdParameterErrorPb2",
    "AdSharingErrorPb2",
    "AdxErrorPb2",
    "AssetErrorPb2",
    "AuthenticationErrorPb2",
    "AuthorizationErrorPb2",
    "BiddingErrorPb2",
    "BiddingStrategyErrorPb2",
    "BillingSetupErrorPb2",
    "CampaignBudgetErrorPb2",
    "CampaignCriterionErrorPb2",
    "CampaignDraftErrorPb2",
    "CampaignErrorPb2",
    "CampaignExperimentErrorPb2",
    "CampaignFeedErrorPb2",
    "CampaignSharedSetErrorPb2",
    "ChangeStatusErrorPb2",
    "ClickViewErrorPb2",
    "CollectionSizeErrorPb2",
    "ContextErrorPb2",
    "ConversionActionErrorPb2",
    "ConversionAdjustmentUploadErrorPb2",
    "ConversionUploadErrorPb2",
    "CountryCodeErrorPb2",
    "CriterionErrorPb2",
    "CurrencyCodeErrorPb2",
    "CustomInterestErrorPb2",
    "CustomerClientLinkErrorPb2",
    "CustomerErrorPb2",
    "CustomerFeedErrorPb2",
    "CustomerManagerLinkErrorPb2",
    "CustomerNegativeCriterionErrorPb2",
    "DatabaseErrorPb2",
    "DateErrorPb2",
    "DateRangeErrorPb2",
    "DistinctErrorPb2",
    "EnumErrorPb2",
    "ErrorsPb2",
    "ExperimentErrorPb2",
    "ExtensionFeedItemErrorPb2",
    "ExtensionSettingErrorPb2",
    "FeedAttributeReferenceErrorPb2",
    "FeedErrorPb2",
    "FeedItemErrorPb2",
    "FeedItemTargetErrorPb2",
    "FeedItemValidationErrorPb2",
    "FeedMappingErrorPb2",
    "FieldErrorPb2",
    "FieldMaskErrorPb2",
    "FunctionErrorPb2",
    "FunctionParsingErrorPb2",
    "GeoTargetConstantSuggestionErrorPb2",
    "HeaderErrorPb2",
    "IdErrorPb2",
    "ImageErrorPb2",
    "InternalErrorPb2",
    "InvoiceErrorPb2",
    "KeywordPlanAdGroupErrorPb2",
    "KeywordPlanCampaignErrorPb2",
    "KeywordPlanErrorPb2",
    "KeywordPlanIdeaErrorPb2",
    "KeywordPlanKeywordErrorPb2",
    "KeywordPlanNegativeKeywordErrorPb2",
    "LabelErrorPb2",
    "LanguageCodeErrorPb2",
    "ListOperationErrorPb2",
    "ManagerLinkErrorPb2",
    "MediaBundleErrorPb2",
    "MediaFileErrorPb2",
    "MediaUploadErrorPb2",
    "MerchantCenterLinkErrorPb2",
    "MultiplierErrorPb2",
    "MutateErrorPb2",
    "MutateJobErrorPb2",
    "NewResourceCreationErrorPb2",
    "NotEmptyErrorPb2",
    "NotWhitelistedErrorPb2",
    "NullErrorPb2",
    "OfflineUserDataJobErrorPb2",
    "OperationAccessDeniedErrorPb2",
    "OperatorErrorPb2",
    "PartialFailureErrorPb2",
    "PolicyFindingErrorPb2",
    "PolicyValidationParameterErrorPb2",
    "PolicyViolationErrorPb2",
    "QueryErrorPb2",
    "QuotaErrorPb2",
    "RangeErrorPb2",
    "ReachPlanErrorPb2",
    "RecommendationErrorPb2",
    "RegionCodeErrorPb2",
    "RequestErrorPb2",
    "ResourceAccessDeniedErrorPb2",
    "ResourceCountLimitExceededErrorPb2",
    "SettingErrorPb2",
    "SharedCriterionErrorPb2",
    "SharedSetErrorPb2",
    "SizeLimitErrorPb2",
    "StringFormatErrorPb2",
    "StringLengthErrorPb2",
    "UrlFieldErrorPb2",
    "UserListErrorPb2",
    "YoutubeVideoRegistrationErrorPb2",
    "AccountBudgetPb2",
    "AccountBudgetProposalPb2",
    "AdGroupAdAssetViewPb2",
    "AdGroupAdLabelPb2",
    "AdGroupAdPb2",
    "AdGroupAudienceViewPb2",
    "AdGroupBidModifierPb2",
    "AdGroupCriterionLabelPb2",
    "AdGroupCriterionPb2",
    "AdGroupCriterionSimulationPb2",
    "AdGroupExtensionSettingPb2",
    "AdGroupFeedPb2",
    "AdGroupLabelPb2",
    "AdGroupPb2",
    "AdGroupSimulationPb2",
    "AdParameterPb2",
    "AdPb2",
    "AdScheduleViewPb2",
    "AdVariationAdViewPb2",
    "AgeRangeViewPb2",
    "AssetPb2",
    "BiddingStrategyPb2",
    "BillingSetupPb2",
    "CampaignAudienceViewPb2",
    "CampaignBidModifierPb2",
    "CampaignBudgetPb2",
    "CampaignCriterionPb2",
    "CampaignCriterionSimulationPb2",
    "CampaignDraftPb2",
    "CampaignExperimentPb2",
    "CampaignExtensionSettingPb2",
    "CampaignFeedPb2",
    "CampaignLabelPb2",
    "CampaignPb2",
    "CampaignSharedSetPb2",
    "CarrierConstantPb2",
    "ChangeStatusPb2",
    "ClickViewPb2",
    "ConversionActionPb2",
    "CurrencyConstantPb2",
    "CustomInterestPb2",
    "CustomerClientLinkPb2",
    "CustomerClientPb2",
    "CustomerExtensionSettingPb2",
    "CustomerFeedPb2",
    "CustomerLabelPb2",
    "CustomerManagerLinkPb2",
    "CustomerNegativeCriterionPb2",
    "CustomerPb2",
    "DetailPlacementViewPb2",
    "DisplayKeywordViewPb2",
    "DistanceViewPb2",
    "DomainCategoryPb2",
    "DynamicSearchAdsSearchTermViewPb2",
    "ExpandedLandingPageViewPb2",
    "ExperimentPb2",
    "ExtensionFeedItemPb2",
    "FeedItemPb2",
    "FeedItemTargetPb2",
    "FeedMappingPb2",
    "FeedPb2",
    "FeedPlaceholderViewPb2",
    "GenderViewPb2",
    "GeoTargetConstantPb2",
    "GeographicViewPb2",
    "GoogleAdsFieldPb2",
    "GroupPlacementViewPb2",
    "HotelGroupViewPb2",
    "HotelPerformanceViewPb2",
    "InvoicePb2",
    "KeywordPlanAdGroupPb2",
    "KeywordPlanCampaignPb2",
    "KeywordPlanKeywordPb2",
    "KeywordPlanNegativeKeywordPb2",
    "KeywordPlanPb2",
    "KeywordViewPb2",
    "LabelPb2",
    "LandingPageViewPb2",
    "LanguageConstantPb2",
    "LocationViewPb2",
    "ManagedPlacementViewPb2",
    "MediaFilePb2",
    "MerchantCenterLinkPb2",
    "MobileAppCategoryConstantPb2",
    "MobileDeviceConstantPb2",
    "MutateJobPb2",
    "OfflineUserDataJobPb2",
    "OperatingSystemVersionConstantPb2",
    "PaidOrganicSearchTermViewPb2",
    "ParentalStatusViewPb2",
    "PaymentsAccountPb2",
    "ProductBiddingCategoryConstantPb2",
    "ProductGroupViewPb2",
    "RecommendationPb2",
    "RemarketingActionPb2",
    "SearchTermViewPb2",
    "SharedCriterionPb2",
    "SharedSetPb2",
    "ShoppingPerformanceViewPb2",
    "TopicConstantPb2",
    "TopicViewPb2",
    "UserInterestPb2",
    "UserListPb2",
    "UserLocationViewPb2",
    "VideoPb2",
    "AccountBudgetProposalServicePb2",
    "AccountBudgetServicePb2",
    "AdGroupAdAssetViewServicePb2",
    "AdGroupAdLabelServicePb2",
    "AdGroupAdServicePb2",
    "AdGroupAudienceViewServicePb2",
    "AdGroupBidModifierServicePb2",
    "AdGroupCriterionLabelServicePb2",
    "AdGroupCriterionServicePb2",
    "AdGroupCriterionSimulationServicePb2",
    "AdGroupExtensionSettingServicePb2",
    "AdGroupFeedServicePb2",
    "AdGroupLabelServicePb2",
    "AdGroupServicePb2",
    "AdGroupSimulationServicePb2",
    "AdParameterServicePb2",
    "AdScheduleViewServicePb2",
    "AdServicePb2",
    "AdVariationAdViewServicePb2",
    "AgeRangeViewServicePb2",
    "AssetServicePb2",
    "BiddingStrategyServicePb2",
    "BillingSetupServicePb2",
    "CampaignAudienceViewServicePb2",
    "CampaignBidModifierServicePb2",
    "CampaignBudgetServicePb2",
    "CampaignCriterionServicePb2",
    "CampaignCriterionSimulationServicePb2",
    "CampaignDraftServicePb2",
    "CampaignExperimentServicePb2",
    "CampaignExtensionSettingServicePb2",
    "CampaignFeedServicePb2",
    "CampaignLabelServicePb2",
    "CampaignServicePb2",
    "CampaignSharedSetServicePb2",
    "CarrierConstantServicePb2",
    "ChangeStatusServicePb2",
    "ClickViewServicePb2",
    "ConversionActionServicePb2",
    "ConversionAdjustmentUploadServicePb2",
    "ConversionUploadServicePb2",
    "CurrencyConstantServicePb2",
    "CustomInterestServicePb2",
    "CustomerClientLinkServicePb2",
    "CustomerClientServicePb2",
    "CustomerExtensionSettingServicePb2",
    "CustomerFeedServicePb2",
    "CustomerLabelServicePb2",
    "CustomerManagerLinkServicePb2",
    "CustomerNegativeCriterionServicePb2",
    "CustomerServicePb2",
    "DisplayKeywordViewServicePb2",
    "DistanceViewServicePb2",
    "DomainCategoryServicePb2",
    "DynamicSearchAdsSearchTermViewServicePb2",
    "ExpandedLandingPageViewServicePb2",
    "ExperimentServicePb2",
    "ExtensionFeedItemServicePb2",
    "FeedItemServicePb2",
    "FeedItemTargetServicePb2",
    "FeedMappingServicePb2",
    "FeedPlaceholderViewServicePb2",
    "FeedServicePb2",
    "GenderViewServicePb2",
    "GeoTargetConstantServicePb2",
    "GeographicViewServicePb2",
    "GoogleAdsFieldServicePb2",
    "GoogleAdsServicePb2",
    "HotelGroupViewServicePb2",
    "HotelPerformanceViewServicePb2",
    "InvoiceServicePb2",
    "KeywordPlanAdGroupServicePb2",
    "KeywordPlanCampaignServicePb2",
    "KeywordPlanIdeaServicePb2",
    "KeywordPlanKeywordServicePb2",
    "KeywordPlanNegativeKeywordServicePb2",
    "KeywordPlanServicePb2",
    "KeywordViewServicePb2",
    "LabelServicePb2",
    "LandingPageViewServicePb2",
    "LanguageConstantServicePb2",
    "LocationViewServicePb2",
    "ManagedPlacementViewServicePb2",
    "MediaFileServicePb2",
    "MerchantCenterLinkServicePb2",
    "MobileAppCategoryConstantServicePb2",
    "MobileDeviceConstantServicePb2",
    "MutateJobServicePb2",
    "OfflineUserDataJobServicePb2",
    "OperatingSystemVersionConstantServicePb2",
    "PaidOrganicSearchTermViewServicePb2",
    "ParentalStatusViewServicePb2",
    "PaymentsAccountServicePb2",
    "ProductBiddingCategoryConstantServicePb2",
    "ProductGroupViewServicePb2",
    "ReachPlanServicePb2",
    "RecommendationServicePb2",
    "RemarketingActionServicePb2",
    "SearchTermViewServicePb2",
    "SharedCriterionServicePb2",
    "SharedSetServicePb2",
    "ShoppingPerformanceViewServicePb2",
    "TopicConstantServicePb2",
    "TopicViewServicePb2",
    "UserInterestServicePb2",
    "UserListServicePb2",
    "UserLocationViewServicePb2",
    "VideoServicePb2",
    "OperationsPb2",
    "AnyPb2",
    "EmptyPb2",
    "FieldMaskPb2",
    "WrappersPb2",
    "StatusPb2",
    "AccessInvitationErrorEnum",
    "AccessReasonEnum",
    "AccessRoleEnum",
    "AccountBudget",
    "AccountBudgetProposalErrorEnum",
    "AccountBudgetProposal",
    "AccountBudgetProposalOperation",
    "AccountBudgetProposalStatusEnum",
    "AccountBudgetProposalTypeEnum",
    "AccountBudgetStatusEnum",
    "AdCustomizerErrorEnum",
    "AdCustomizerPlaceholderFieldEnum",
    "AddMutateJobOperationsRequest",
    "AddMutateJobOperationsResponse",
    "AddressInfo",
    "AdErrorEnum",
    "Ad",
    "AdGroupAdAssetPolicySummary",
    "AdGroupAdAssetView",
    "AdGroupAdErrorEnum",
    "AdGroupAd",
    "AdGroupAdLabel",
    "AdGroupAdLabelOperation",
    "AdGroupAdOperation",
    "AdGroupAdPolicySummary",
    "AdGroupAdRotationModeEnum",
    "AdGroupAdStatusEnum",
    "AdGroupAudienceView",
    "AdGroupBidModifierErrorEnum",
    "AdGroupBidModifier",
    "AdGroupBidModifierOperation",
    "AdGroupCriterionApprovalStatusEnum",
    "AdGroupCriterionErrorEnum",
    "AdGroupCriterion",
    "AdGroupCriterionLabel",
    "AdGroupCriterionLabelOperation",
    "AdGroupCriterionOperation",
    "AdGroupCriterionSimulation",
    "AdGroupCriterionStatusEnum",
    "AdGroupErrorEnum",
    "AdGroupExtensionSetting",
    "AdGroupExtensionSettingOperation",
    "AdGroupFeedErrorEnum",
    "AdGroupFeed",
    "AdGroupFeedOperation",
    "AdGroup",
    "AdGroupLabel",
    "AdGroupLabelOperation",
    "AdGroupOperation",
    "AdGroupSimulation",
    "AdGroupStatusEnum",
    "AdGroupTypeEnum",
    "AdImageAsset",
    "AdMediaBundleAsset",
    "AdNetworkTypeEnum",
    "AdOperation",
    "AdParameterErrorEnum",
    "AdParameter",
    "AdParameterOperation",
    "AdScheduleInfo",
    "AdScheduleView",
    "AdServingOptimizationStatusEnum",
    "AdSharingErrorEnum",
    "AdStrengthEnum",
    "AdTextAsset",
    "AdTypeEnum",
    "AdvertisingChannelSubTypeEnum",
    "AdvertisingChannelTypeEnum",
    "AdVideoAsset",
    "AdxErrorEnum",
    "AffiliateLocationFeedItem",
    "AffiliateLocationFeedRelationshipTypeEnum",
    "AffiliateLocationPlaceholderFieldEnum",
    "AgeRangeInfo",
    "AgeRangeTypeEnum",
    "AgeRangeView",
    "AppAdInfo",
    "AppCampaignAppStoreEnum",
    "AppCampaignBiddingStrategyGoalTypeEnum",
    "AppEngagementAdInfo",
    "AppFeedItem",
    "ApplyRecommendationOperation",
    "ApplyRecommendationRequest",
    "ApplyRecommendationResponse",
    "ApplyRecommendationResult",
    "AppPaymentModelInfo",
    "AppPaymentModelTypeEnum",
    "AppPlaceholderFieldEnum",
    "AppStoreEnum",
    "AppUrlOperatingSystemTypeEnum",
    "AssetErrorEnum",
    "AssetFieldTypeEnum",
    "Asset",
    "AssetOperation",
    "AssetPerformanceLabelEnum",
    "AssetTypeEnum",
    "AttributeFieldMapping",
    "AttributionModelEnum",
    "AuthenticationErrorEnum",
    "AuthorizationErrorEnum",
    "BasicUserListInfo",
    "BiddingErrorEnum",
    "BiddingSourceEnum",
    "BiddingStrategyErrorEnum",
    "BiddingStrategy",
    "BiddingStrategyOperation",
    "BiddingStrategyStatusEnum",
    "BiddingStrategyTypeEnum",
    "BidModifierSimulationPoint",
    "BidModifierSimulationPointList",
    "BidModifierSourceEnum",
    "BillingSetupErrorEnum",
    "BillingSetup",
    "BillingSetupOperation",
    "BillingSetupStatusEnum",
    "BrandSafetySuitabilityEnum",
    "BudgetDeliveryMethodEnum",
    "BudgetPeriodEnum",
    "BudgetStatusEnum",
    "BudgetTypeEnum",
    "CallConversion",
    "CallConversionReportingStateEnum",
    "CallConversionResult",
    "CallFeedItem",
    "CallOnlyAdInfo",
    "CalloutFeedItem",
    "CalloutPlaceholderFieldEnum",
    "CallPlaceholderFieldEnum",
    "CallReportingSetting",
    "CampaignAudienceView",
    "CampaignBidModifier",
    "CampaignBidModifierOperation",
    "CampaignBudgetErrorEnum",
    "CampaignBudget",
    "CampaignBudgetOperation",
    "CampaignCriterionErrorEnum",
    "CampaignCriterion",
    "CampaignCriterionOperation",
    "CampaignCriterionSimulation",
    "CampaignCriterionStatusEnum",
    "CampaignDraftErrorEnum",
    "CampaignDraft",
    "CampaignDraftOperation",
    "CampaignDraftStatusEnum",
    "CampaignDuration",
    "CampaignErrorEnum",
    "CampaignExperimentErrorEnum",
    "CampaignExperiment",
    "CampaignExperimentOperation",
    "CampaignExperimentStatusEnum",
    "CampaignExperimentTrafficSplitTypeEnum",
    "CampaignExperimentTypeEnum",
    "CampaignExtensionSetting",
    "CampaignExtensionSettingOperation",
    "CampaignFeedErrorEnum",
    "CampaignFeed",
    "CampaignFeedOperation",
    "Campaign",
    "CampaignLabel",
    "CampaignLabelOperation",
    "CampaignOperation",
    "CampaignServingStatusEnum",
    "CampaignSharedSetErrorEnum",
    "CampaignSharedSet",
    "CampaignSharedSetOperation",
    "CampaignSharedSetStatusEnum",
    "CampaignStatusEnum",
    "CarrierConstant",
    "CarrierInfo",
    "ChangeStatusErrorEnum",
    "ChangeStatus",
    "ChangeStatusOperationEnum",
    "ChangeStatusResourceTypeEnum",
    "ClickConversion",
    "ClickConversionResult",
    "ClickLocation",
    "ClickTypeEnum",
    "ClickView",
    "CollectionSizeErrorEnum",
    "CombinedRuleUserListInfo",
    "Commission",
    "ContentLabelInfo",
    "ContentLabelTypeEnum",
    "ContextErrorEnum",
    "ConversionActionCategoryEnum",
    "ConversionActionCountingTypeEnum",
    "ConversionActionErrorEnum",
    "ConversionAction",
    "ConversionActionOperation",
    "ConversionActionStatusEnum",
    "ConversionActionTypeEnum",
    "ConversionAdjustment",
    "ConversionAdjustmentResult",
    "ConversionAdjustmentTypeEnum",
    "ConversionAdjustmentUploadErrorEnum",
    "ConversionAttributionEventTypeEnum",
    "ConversionLagBucketEnum",
    "ConversionOrAdjustmentLagBucketEnum",
    "ConversionTrackingSetting",
    "ConversionUploadErrorEnum",
    "CountryCodeErrorEnum",
    "CpcBidSimulationPoint",
    "CpcBidSimulationPointList",
    "CpvBidSimulationPoint",
    "CpvBidSimulationPointList",
    "CreateCampaignExperimentMetadata",
    "CreateCampaignExperimentRequest",
    "CreateCustomerClientRequest",
    "CreateCustomerClientResponse",
    "CreateMutateJobRequest",
    "CreateMutateJobResponse",
    "CriterionCategoryAvailability",
    "CriterionCategoryChannelAvailability",
    "CriterionCategoryChannelAvailabilityModeEnum",
    "CriterionCategoryLocaleAvailability",
    "CriterionCategoryLocaleAvailabilityModeEnum",
    "CriterionErrorEnum",
    "CriterionSystemServingStatusEnum",
    "CriterionTypeEnum",
    "CrmBasedUserListInfo",
    "CurrencyCodeErrorEnum",
    "CustomAffinityInfo",
    "CustomerClient",
    "CustomerClientLinkErrorEnum",
    "CustomerClientLink",
    "CustomerClientLinkOperation",
    "CustomerErrorEnum",
    "CustomerExtensionSetting",
    "CustomerExtensionSettingOperation",
    "CustomerFeedErrorEnum",
    "CustomerFeed",
    "CustomerFeedOperation",
    "Customer",
    "CustomerLabel",
    "CustomerLabelOperation",
    "CustomerManagerLinkErrorEnum",
    "CustomerManagerLink",
    "CustomerManagerLinkOperation",
    "CustomerMatchUploadKeyTypeEnum",
    "CustomerNegativeCriterion",
    "CustomerNegativeCriterionOperation",
    "CustomerOperation",
    "CustomerPayPerConversionEligibilityFailureReasonEnum",
    "CustomIntentInfo",
    "CustomInterestErrorEnum",
    "CustomInterest",
    "CustomInterestMember",
    "CustomInterestMemberTypeEnum",
    "CustomInterestOperation",
    "CustomInterestStatusEnum",
    "CustomInterestTypeEnum",
    "CustomParameter",
    "CustomPlaceholderFieldEnum",
    "DatabaseErrorEnum",
    "DataDrivenModelStatusEnum",
    "DateErrorEnum",
    "DateRangeErrorEnum",
    "DateRange",
    "DateSpecificRuleUserListInfo",
    "DayOfWeekEnum",
    "DetailPlacementView",
    "DeviceEnum",
    "DeviceInfo",
    "DismissRecommendationRequest",
    "DismissRecommendationResponse",
    "DisplayAdFormatSettingEnum",
    "DisplayCallToAction",
    "DisplayKeywordView",
    "DisplayUploadAdInfo",
    "DisplayUploadProductTypeEnum",
    "DistanceBucketEnum",
    "DistanceView",
    "DistinctErrorEnum",
    "DomainCategory",
    "DsaPageFeedCriterionFieldEnum",
    "DynamicSearchAdsSearchTermView",
    "EducationPlaceholderFieldEnum",
    "EndCampaignExperimentRequest",
    "EnhancedCpc",
    "EnumErrorEnum",
    "ErrorCode",
    "ErrorDetails",
    "ErrorLocation",
    "ExpandedDynamicSearchAdInfo",
    "ExpandedLandingPageView",
    "ExpandedTextAdInfo",
    "ExplorerAutoOptimizerSetting",
    "ExpressionRuleUserListInfo",
    "ExtensionFeedItemErrorEnum",
    "ExtensionFeedItem",
    "ExtensionFeedItemOperation",
    "ExtensionSettingDeviceEnum",
    "ExtensionSettingErrorEnum",
    "ExtensionTypeEnum",
    "ExternalAttributionData",
    "ExternalConversionSourceEnum",
    "FeedAttribute",
    "FeedAttributeOperation",
    "FeedAttributeReferenceErrorEnum",
    "FeedAttributeTypeEnum",
    "FeedErrorEnum",
    "Feed",
    "FeedItemAttributeValue",
    "FeedItemErrorEnum",
    "FeedItem",
    "FeedItemOperation",
    "FeedItemPlaceholderPolicyInfo",
    "FeedItemQualityApprovalStatusEnum",
    "FeedItemQualityDisapprovalReasonEnum",
    "FeedItemStatusEnum",
    "FeedItemTargetDeviceEnum",
    "FeedItemTargetErrorEnum",
    "FeedItemTarget",
    "FeedItemTargetOperation",
    "FeedItemTargetTypeEnum",
    "FeedItemValidationErrorEnum",
    "FeedItemValidationError",
    "FeedItemValidationStatusEnum",
    "FeedLinkStatusEnum",
    "FeedMappingCriterionTypeEnum",
    "FeedMappingErrorEnum",
    "FeedMapping",
    "FeedMappingOperation",
    "FeedMappingStatusEnum",
    "FeedOperation",
    "FeedOriginEnum",
    "FeedPlaceholderView",
    "FeedStatusEnum",
    "FieldErrorEnum",
    "FieldMaskErrorEnum",
    "FinalAppUrl",
    "FlightPlaceholderFieldEnum",
    "Forecast",
    "ForecastMetrics",
    "FrequencyCapEntry",
    "FrequencyCapEventTypeEnum",
    "FrequencyCapKey",
    "FrequencyCapLevelEnum",
    "FrequencyCapTimeUnitEnum",
    "FunctionErrorEnum",
    "FunctionParsingErrorEnum",
    "GclidDateTimePair",
    "GenderInfo",
    "GenderTypeEnum",
    "GenderView",
    "GenerateForecastMetricsRequest",
    "GenerateForecastMetricsResponse",
    "GenerateHistoricalMetricsRequest",
    "GenerateHistoricalMetricsResponse",
    "GenerateKeywordIdeaResponse",
    "GenerateKeywordIdeaResult",
    "GenerateKeywordIdeasRequest",
    "GenerateProductMixIdeasRequest",
    "GenerateProductMixIdeasResponse",
    "GenerateReachForecastRequest",
    "GenerateReachForecastResponse",
    "GeographicView",
    "GeoPointInfo",
    "GeoTargetConstant",
    "GeoTargetConstantStatusEnum",
    "GeoTargetConstantSuggestionErrorEnum",
    "GeoTargetConstantSuggestion",
    "GeoTargetingRestrictionEnum",
    "GeoTargetingTypeEnum",
    "GetAccountBudgetProposalRequest",
    "GetAccountBudgetRequest",
    "GetAdGroupAdAssetViewRequest",
    "GetAdGroupAdLabelRequest",
    "GetAdGroupAdRequest",
    "GetAdGroupAudienceViewRequest",
    "GetAdGroupBidModifierRequest",
    "GetAdGroupCriterionLabelRequest",
    "GetAdGroupCriterionRequest",
    "GetAdGroupCriterionSimulationRequest",
    "GetAdGroupExtensionSettingRequest",
    "GetAdGroupFeedRequest",
    "GetAdGroupLabelRequest",
    "GetAdGroupRequest",
    "GetAdGroupSimulationRequest",
    "GetAdParameterRequest",
    "GetAdRequest",
    "GetAdScheduleViewRequest",
    "GetAgeRangeViewRequest",
    "GetAssetRequest",
    "GetBiddingStrategyRequest",
    "GetBillingSetupRequest",
    "GetCampaignAudienceViewRequest",
    "GetCampaignBidModifierRequest",
    "GetCampaignBudgetRequest",
    "GetCampaignCriterionRequest",
    "GetCampaignCriterionSimulationRequest",
    "GetCampaignDraftRequest",
    "GetCampaignExperimentRequest",
    "GetCampaignExtensionSettingRequest",
    "GetCampaignFeedRequest",
    "GetCampaignLabelRequest",
    "GetCampaignRequest",
    "GetCampaignSharedSetRequest",
    "GetCarrierConstantRequest",
    "GetChangeStatusRequest",
    "GetClickViewRequest",
    "GetConversionActionRequest",
    "GetCustomerClientLinkRequest",
    "GetCustomerClientRequest",
    "GetCustomerExtensionSettingRequest",
    "GetCustomerFeedRequest",
    "GetCustomerLabelRequest",
    "GetCustomerManagerLinkRequest",
    "GetCustomerNegativeCriterionRequest",
    "GetCustomerRequest",
    "GetCustomInterestRequest",
    "GetDetailPlacementViewRequest",
    "GetDisplayKeywordViewRequest",
    "GetDistanceViewRequest",
    "GetDomainCategoryRequest",
    "GetDynamicSearchAdsSearchTermViewRequest",
    "GetExpandedLandingPageViewRequest",
    "GetExtensionFeedItemRequest",
    "GetFeedItemRequest",
    "GetFeedItemTargetRequest",
    "GetFeedMappingRequest",
    "GetFeedPlaceholderViewRequest",
    "GetFeedRequest",
    "GetGenderViewRequest",
    "GetGeographicViewRequest",
    "GetGeoTargetConstantRequest",
    "GetGoogleAdsFieldRequest",
    "GetGroupPlacementViewRequest",
    "GetHotelGroupViewRequest",
    "GetHotelPerformanceViewRequest",
    "GetKeywordPlanAdGroupRequest",
    "GetKeywordPlanCampaignRequest",
    "GetKeywordPlanKeywordRequest",
    "GetKeywordPlanNegativeKeywordRequest",
    "GetKeywordPlanRequest",
    "GetKeywordViewRequest",
    "GetLabelRequest",
    "GetLandingPageViewRequest",
    "GetLanguageConstantRequest",
    "GetLocationViewRequest",
    "GetManagedPlacementViewRequest",
    "GetMediaFileRequest",
    "GetMerchantCenterLinkRequest",
    "GetMobileAppCategoryConstantRequest",
    "GetMobileDeviceConstantRequest",
    "GetMutateJobRequest",
    "GetOperatingSystemVersionConstantRequest",
    "GetPaidOrganicSearchTermViewRequest",
    "GetParentalStatusViewRequest",
    "GetProductBiddingCategoryConstantRequest",
    "GetProductGroupViewRequest",
    "GetRecommendationRequest",
    "GetRemarketingActionRequest",
    "GetSearchTermViewRequest",
    "GetSharedCriterionRequest",
    "GetSharedSetRequest",
    "GetShoppingPerformanceViewRequest",
    "GetTopicConstantRequest",
    "GetTopicViewRequest",
    "GetUserInterestRequest",
    "GetUserListRequest",
    "GetUserLocationViewRequest",
    "GetVideoRequest",
    "GmailAdInfo",
    "GmailTeaser",
    "GoogleAdsError",
    "GoogleAdsFailure",
    "GoogleAdsFieldCategoryEnum",
    "GoogleAdsFieldDataTypeEnum",
    "GoogleAdsField",
    "GoogleAdsRow",
    "GraduateCampaignExperimentRequest",
    "GraduateCampaignExperimentResponse",
    "GroupPlacementView",
    "HeaderErrorEnum",
    "HotelAdInfo",
    "HotelAdvanceBookingWindowInfo",
    "HotelCalloutFeedItem",
    "HotelCheckInDayInfo",
    "HotelCityInfo",
    "HotelClassInfo",
    "HotelCountryRegionInfo",
    "HotelDateSelectionTypeEnum",
    "HotelDateSelectionTypeInfo",
    "HotelGroupView",
    "HotelIdInfo",
    "HotelLengthOfStayInfo",
    "HotelPerformanceView",
    "HotelPlaceholderFieldEnum",
    "HotelPriceBucketEnum",
    "HotelRateTypeEnum",
    "HotelStateInfo",
    "IdErrorEnum",
    "ImageAdInfo",
    "ImageAsset",
    "ImageDimension",
    "ImageErrorEnum",
    "IncomeRangeInfo",
    "IncomeRangeTypeEnum",
    "InteractionEventTypeEnum",
    "InteractionTypeEnum",
    "InteractionTypeInfo",
    "InternalErrorEnum",
    "InvoiceErrorEnum",
    "Invoice",
    "InvoiceTypeEnum",
    "IpBlockInfo",
    "JobPlaceholderFieldEnum",
    "KeywordAndUrlSeed",
    "Keyword",
    "KeywordInfo",
    "KeywordMatchTypeEnum",
    "KeywordPlanAdGroupErrorEnum",
    "KeywordPlanAdGroupForecast",
    "KeywordPlanAdGroup",
    "KeywordPlanAdGroupOperation",
    "KeywordPlanCampaignErrorEnum",
    "KeywordPlanCampaignForecast",
    "KeywordPlanCampaign",
    "KeywordPlanCampaignOperation",
    "KeywordPlanCompetitionLevelEnum",
    "KeywordPlanErrorEnum",
    "KeywordPlanForecastIntervalEnum",
    "KeywordPlanForecastPeriod",
    "KeywordPlanGeoTarget",
    "KeywordPlan",
    "KeywordPlanHistoricalMetrics",
    "KeywordPlanIdeaErrorEnum",
    "KeywordPlanKeywordErrorEnum",
    "KeywordPlanKeywordForecast",
    "KeywordPlanKeyword",
    "KeywordPlanKeywordHistoricalMetrics",
    "KeywordPlanKeywordOperation",
    "KeywordPlanNegativeKeywordErrorEnum",
    "KeywordPlanNegativeKeyword",
    "KeywordPlanNegativeKeywordOperation",
    "KeywordPlanNetworkEnum",
    "KeywordPlanOperation",
    "KeywordSeed",
    "KeywordView",
    "LabelErrorEnum",
    "Label",
    "LabelOperation",
    "LabelStatusEnum",
    "LandingPageView",
    "LanguageCodeErrorEnum",
    "LanguageConstant",
    "LanguageInfo",
    "LegacyAppInstallAdAppStoreEnum",
    "LegacyAppInstallAdInfo",
    "LegacyResponsiveDisplayAdInfo",
    "ListAccessibleCustomersRequest",
    "ListAccessibleCustomersResponse",
    "ListCampaignDraftAsyncErrorsRequest",
    "ListCampaignDraftAsyncErrorsResponse",
    "ListCampaignExperimentAsyncErrorsRequest",
    "ListCampaignExperimentAsyncErrorsResponse",
    "ListingBrandInfo",
    "ListingCustomAttributeIndexEnum",
    "ListingCustomAttributeInfo",
    "ListingDimensionInfo",
    "ListingGroupInfo",
    "ListingGroupTypeEnum",
    "ListingScopeInfo",
    "ListInvoicesRequest",
    "ListInvoicesResponse",
    "ListMerchantCenterLinksRequest",
    "ListMerchantCenterLinksResponse",
    "ListMutateJobResultsRequest",
    "ListMutateJobResultsResponse",
    "ListOperationErrorEnum",
    "ListPaymentsAccountsRequest",
    "ListPaymentsAccountsResponse",
    "ListPlannableLocationsRequest",
    "ListPlannableLocationsResponse",
    "ListPlannableProductsRequest",
    "ListPlannableProductsResponse",
    "LocalPlaceholderFieldEnum",
    "LocationExtensionTargetingCriterionFieldEnum",
    "LocationFeedItem",
    "LocationGroupInfo",
    "LocationGroupRadiusUnitsEnum",
    "LocationInfo",
    "LocationPlaceholderFieldEnum",
    "LocationView",
    "LogicalUserListInfo",
    "LogicalUserListOperandInfo",
    "ManagedPlacementView",
    "ManagerLinkErrorEnum",
    "ManagerLinkStatusEnum",
    "ManualCpc",
    "ManualCpm",
    "ManualCpv",
    "MatchingFunctionContextTypeEnum",
    "MatchingFunction",
    "MatchingFunctionOperatorEnum",
    "MaximizeConversions",
    "MaximizeConversionValue",
    "MediaAudio",
    "MediaBundleAsset",
    "MediaBundleErrorEnum",
    "MediaBundle",
    "MediaFileErrorEnum",
    "MediaFile",
    "MediaFileOperation",
    "MediaImage",
    "MediaTypeEnum",
    "MediaUploadErrorEnum",
    "MediaVideo",
    "MerchantCenterLink",
    "MerchantCenterLinkOperation",
    "MerchantCenterLinkStatusEnum",
    "MessagePlaceholderFieldEnum",
    "Metrics",
    "MimeTypeEnum",
    "MinuteOfHourEnum",
    "MobileAppCategoryConstant",
    "MobileAppCategoryInfo",
    "MobileApplicationInfo",
    "MobileDeviceConstant",
    "MobileDeviceInfo",
    "MobileDeviceTypeEnum",
    "Money",
    "MonthOfYearEnum",
    "MultiplierErrorEnum",
    "MutateAccountBudgetProposalRequest",
    "MutateAccountBudgetProposalResponse",
    "MutateAccountBudgetProposalResult",
    "MutateAdGroupAdLabelResult",
    "MutateAdGroupAdLabelsRequest",
    "MutateAdGroupAdLabelsResponse",
    "MutateAdGroupAdResult",
    "MutateAdGroupAdsRequest",
    "MutateAdGroupAdsResponse",
    "MutateAdGroupBidModifierResult",
    "MutateAdGroupBidModifiersRequest",
    "MutateAdGroupBidModifiersResponse",
    "MutateAdGroupCriteriaRequest",
    "MutateAdGroupCriteriaResponse",
    "MutateAdGroupCriterionLabelResult",
    "MutateAdGroupCriterionLabelsRequest",
    "MutateAdGroupCriterionLabelsResponse",
    "MutateAdGroupCriterionResult",
    "MutateAdGroupExtensionSettingResult",
    "MutateAdGroupExtensionSettingsRequest",
    "MutateAdGroupExtensionSettingsResponse",
    "MutateAdGroupFeedResult",
    "MutateAdGroupFeedsRequest",
    "MutateAdGroupFeedsResponse",
    "MutateAdGroupLabelResult",
    "MutateAdGroupLabelsRequest",
    "MutateAdGroupLabelsResponse",
    "MutateAdGroupResult",
    "MutateAdGroupsRequest",
    "MutateAdGroupsResponse",
    "MutateAdParameterResult",
    "MutateAdParametersRequest",
    "MutateAdParametersResponse",
    "MutateAdResult",
    "MutateAdsRequest",
    "MutateAdsResponse",
    "MutateAssetResult",
    "MutateAssetsRequest",
    "MutateAssetsResponse",
    "MutateBiddingStrategiesRequest",
    "MutateBiddingStrategiesResponse",
    "MutateBiddingStrategyResult",
    "MutateBillingSetupRequest",
    "MutateBillingSetupResponse",
    "MutateBillingSetupResult",
    "MutateCampaignBidModifierResult",
    "MutateCampaignBidModifiersRequest",
    "MutateCampaignBidModifiersResponse",
    "MutateCampaignBudgetResult",
    "MutateCampaignBudgetsRequest",
    "MutateCampaignBudgetsResponse",
    "MutateCampaignCriteriaRequest",
    "MutateCampaignCriteriaResponse",
    "MutateCampaignCriterionResult",
    "MutateCampaignDraftResult",
    "MutateCampaignDraftsRequest",
    "MutateCampaignDraftsResponse",
    "MutateCampaignExperimentResult",
    "MutateCampaignExperimentsRequest",
    "MutateCampaignExperimentsResponse",
    "MutateCampaignExtensionSettingResult",
    "MutateCampaignExtensionSettingsRequest",
    "MutateCampaignExtensionSettingsResponse",
    "MutateCampaignFeedResult",
    "MutateCampaignFeedsRequest",
    "MutateCampaignFeedsResponse",
    "MutateCampaignLabelResult",
    "MutateCampaignLabelsRequest",
    "MutateCampaignLabelsResponse",
    "MutateCampaignResult",
    "MutateCampaignSharedSetResult",
    "MutateCampaignSharedSetsRequest",
    "MutateCampaignSharedSetsResponse",
    "MutateCampaignsRequest",
    "MutateCampaignsResponse",
    "MutateConversionActionResult",
    "MutateConversionActionsRequest",
    "MutateConversionActionsResponse",
    "MutateCustomerClientLinkRequest",
    "MutateCustomerClientLinkResponse",
    "MutateCustomerClientLinkResult",
    "MutateCustomerExtensionSettingResult",
    "MutateCustomerExtensionSettingsRequest",
    "MutateCustomerExtensionSettingsResponse",
    "MutateCustomerFeedResult",
    "MutateCustomerFeedsRequest",
    "MutateCustomerFeedsResponse",
    "MutateCustomerLabelResult",
    "MutateCustomerLabelsRequest",
    "MutateCustomerLabelsResponse",
    "MutateCustomerManagerLinkRequest",
    "MutateCustomerManagerLinkResponse",
    "MutateCustomerManagerLinkResult",
    "MutateCustomerNegativeCriteriaRequest",
    "MutateCustomerNegativeCriteriaResponse",
    "MutateCustomerNegativeCriteriaResult",
    "MutateCustomerRequest",
    "MutateCustomerResponse",
    "MutateCustomerResult",
    "MutateCustomInterestResult",
    "MutateCustomInterestsRequest",
    "MutateCustomInterestsResponse",
    "MutateErrorEnum",
    "MutateExtensionFeedItemResult",
    "MutateExtensionFeedItemsRequest",
    "MutateExtensionFeedItemsResponse",
    "MutateFeedItemResult",
    "MutateFeedItemsRequest",
    "MutateFeedItemsResponse",
    "MutateFeedItemTargetResult",
    "MutateFeedItemTargetsRequest",
    "MutateFeedItemTargetsResponse",
    "MutateFeedMappingResult",
    "MutateFeedMappingsRequest",
    "MutateFeedMappingsResponse",
    "MutateFeedResult",
    "MutateFeedsRequest",
    "MutateFeedsResponse",
    "MutateGoogleAdsRequest",
    "MutateGoogleAdsResponse",
    "MutateJobErrorEnum",
    "MutateJob",
    "MutateJobResult",
    "MutateJobStatusEnum",
    "MutateKeywordPlanAdGroupResult",
    "MutateKeywordPlanAdGroupsRequest",
    "MutateKeywordPlanAdGroupsResponse",
    "MutateKeywordPlanCampaignResult",
    "MutateKeywordPlanCampaignsRequest",
    "MutateKeywordPlanCampaignsResponse",
    "MutateKeywordPlanKeywordResult",
    "MutateKeywordPlanKeywordsRequest",
    "MutateKeywordPlanKeywordsResponse",
    "MutateKeywordPlanNegativeKeywordResult",
    "MutateKeywordPlanNegativeKeywordsRequest",
    "MutateKeywordPlanNegativeKeywordsResponse",
    "MutateKeywordPlansRequest",
    "MutateKeywordPlansResponse",
    "MutateKeywordPlansResult",
    "MutateLabelResult",
    "MutateLabelsRequest",
    "MutateLabelsResponse",
    "MutateMediaFileResult",
    "MutateMediaFilesRequest",
    "MutateMediaFilesResponse",
    "MutateMerchantCenterLinkRequest",
    "MutateMerchantCenterLinkResponse",
    "MutateMerchantCenterLinkResult",
    "MutateOperation",
    "MutateOperationResponse",
    "MutateRemarketingActionResult",
    "MutateRemarketingActionsRequest",
    "MutateRemarketingActionsResponse",
    "MutateSharedCriteriaRequest",
    "MutateSharedCriteriaResponse",
    "MutateSharedCriterionResult",
    "MutateSharedSetResult",
    "MutateSharedSetsRequest",
    "MutateSharedSetsResponse",
    "MutateUserListResult",
    "MutateUserListsRequest",
    "MutateUserListsResponse",
    "NegativeGeoTargetTypeEnum",
    "NewResourceCreationErrorEnum",
    "NotEmptyErrorEnum",
    "NotWhitelistedErrorEnum",
    "NullErrorEnum",
    "OnTargetAudienceMetrics",
    "Operand",
    "OperatingSystemVersionConstant",
    "OperatingSystemVersionInfo",
    "OperatingSystemVersionOperatorTypeEnum",
    "OperationAccessDeniedErrorEnum",
    "OperatorErrorEnum",
    "PageOnePromoted",
    "PageOnePromotedStrategyGoalEnum",
    "PaidOrganicSearchTermView",
    "ParentalStatusInfo",
    "ParentalStatusTypeEnum",
    "ParentalStatusView",
    "PartialFailureErrorEnum",
    "PaymentModeEnum",
    "PaymentsAccount",
    "PercentCpc",
    "PlaceholderTypeEnum",
    "PlacementInfo",
    "PlacementTypeEnum",
    "PlannableLocation",
    "PlannableTargeting",
    "PlannedProduct",
    "PolicyApprovalStatusEnum",
    "PolicyFindingDetails",
    "PolicyFindingErrorEnum",
    "PolicyReviewStatusEnum",
    "PolicyTopicConstraint",
    "PolicyTopicEntry",
    "PolicyTopicEntryTypeEnum",
    "PolicyTopicEvidenceDestinationMismatchUrlTypeEnum",
    "PolicyTopicEvidenceDestinationNotWorkingDeviceEnum",
    "PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum",
    "PolicyTopicEvidence",
    "PolicyValidationParameterErrorEnum",
    "PolicyValidationParameter",
    "PolicyViolationDetails",
    "PolicyViolationErrorEnum",
    "PolicyViolationKey",
    "PositiveGeoTargetTypeEnum",
    "Preferences",
    "PreferredContentInfo",
    "PreferredContentTypeEnum",
    "PriceExtensionPriceQualifierEnum",
    "PriceExtensionPriceUnitEnum",
    "PriceExtensionTypeEnum",
    "PriceFeedItem",
    "PriceOffer",
    "PricePlaceholderFieldEnum",
    "ProductAllocation",
    "ProductBiddingCategoryConstant",
    "ProductBiddingCategoryInfo",
    "ProductBiddingCategoryLevelEnum",
    "ProductBiddingCategoryStatusEnum",
    "ProductChannelEnum",
    "ProductChannelExclusivityEnum",
    "ProductChannelExclusivityInfo",
    "ProductChannelInfo",
    "ProductConditionEnum",
    "ProductConditionInfo",
    "ProductGroupView",
    "ProductImage",
    "ProductItemIdInfo",
    "ProductMetadata",
    "ProductTypeInfo",
    "ProductTypeLevelEnum",
    "ProductVideo",
    "PromoteCampaignDraftRequest",
    "PromoteCampaignExperimentRequest",
    "PromotionExtensionDiscountModifierEnum",
    "PromotionExtensionOccasionEnum",
    "PromotionFeedItem",
    "PromotionPlaceholderFieldEnum",
    "ProximityInfo",
    "ProximityRadiusUnitsEnum",
    "QualityScoreBucketEnum",
    "QueryErrorEnum",
    "QuotaErrorEnum",
    "RangeErrorEnum",
    "ReachCurve",
    "ReachForecast",
    "ReachPlanAdLengthEnum",
    "ReachPlanAgeRangeEnum",
    "ReachPlanErrorEnum",
    "RealEstatePlaceholderFieldEnum",
    "RealTimeBiddingSetting",
    "RecommendationErrorEnum",
    "Recommendation",
    "RecommendationTypeEnum",
    "RegionCodeErrorEnum",
    "RemarketingAction",
    "RemarketingActionOperation",
    "RemarketingSetting",
    "RequestErrorEnum",
    "ResourceAccessDeniedErrorEnum",
    "ResourceCountLimitExceededErrorEnum",
    "ResponsiveDisplayAdInfo",
    "ResponsiveSearchAdInfo",
    "RestatementValue",
    "RuleBasedUserListInfo",
    "RunMutateJobRequest",
    "SearchEngineResultsPageTypeEnum",
    "SearchGoogleAdsFieldsRequest",
    "SearchGoogleAdsFieldsResponse",
    "SearchGoogleAdsRequest",
    "SearchGoogleAdsResponse",
    "SearchTermMatchTypeEnum",
    "SearchTermTargetingStatusEnum",
    "SearchTermView",
    "Segments",
    "ServedAssetFieldTypeEnum",
    "SettingErrorEnum",
    "SharedCriterionErrorEnum",
    "SharedCriterion",
    "SharedCriterionOperation",
    "SharedSetErrorEnum",
    "SharedSet",
    "SharedSetOperation",
    "SharedSetStatusEnum",
    "SharedSetTypeEnum",
    "ShoppingComparisonListingAdInfo",
    "ShoppingPerformanceView",
    "ShoppingProductAdInfo",
    "ShoppingSmartAdInfo",
    "SimilarUserListInfo",
    "SimulationModificationMethodEnum",
    "SimulationTypeEnum",
    "SitelinkFeedItem",
    "SitelinkPlaceholderFieldEnum",
    "SizeLimitErrorEnum",
    "SlotEnum",
    "SpendingLimitTypeEnum",
    "StringFormatErrorEnum",
    "StringLengthErrorEnum",
    "StructuredSnippetFeedItem",
    "StructuredSnippetPlaceholderFieldEnum",
    "SuggestGeoTargetConstantsRequest",
    "SuggestGeoTargetConstantsResponse",
    "SystemManagedResourceSourceEnum",
    "TagSnippet",
    "TargetCpa",
    "TargetCpaOptInRecommendationGoalEnum",
    "TargetCpaSimulationPoint",
    "TargetCpaSimulationPointList",
    "TargetCpm",
    "TargetImpressionShare",
    "TargetImpressionShareLocationEnum",
    "TargetingDimensionEnum",
    "Targeting",
    "TargetingSetting",
    "TargetOutrankShare",
    "TargetRestriction",
    "TargetRoas",
    "TargetSpend",
    "TextAdInfo",
    "TextAsset",
    "TextLabel",
    "TextMessageFeedItem",
    "TimeTypeEnum",
    "TopicConstant",
    "TopicInfo",
    "TopicView",
    "TrackingCodePageFormatEnum",
    "TrackingCodeTypeEnum",
    "TravelPlaceholderFieldEnum",
    "UnknownListingDimensionInfo",
    "UploadCallConversionsRequest",
    "UploadCallConversionsResponse",
    "UploadClickConversionsRequest",
    "UploadClickConversionsResponse",
    "UploadConversionAdjustmentsRequest",
    "UploadConversionAdjustmentsResponse",
    "UrlCollection",
    "UrlFieldErrorEnum",
    "UrlSeed",
    "UserInterest",
    "UserInterestInfo",
    "UserInterestTaxonomyTypeEnum",
    "UserListAccessStatusEnum",
    "UserListActionInfo",
    "UserListClosingReasonEnum",
    "UserListCombinedRuleOperatorEnum",
    "UserListCrmDataSourceTypeEnum",
    "UserListDateRuleItemInfo",
    "UserListDateRuleItemOperatorEnum",
    "UserListErrorEnum",
    "UserList",
    "UserListInfo",
    "UserListLogicalRuleInfo",
    "UserListLogicalRuleOperatorEnum",
    "UserListMembershipStatusEnum",
    "UserListNumberRuleItemInfo",
    "UserListNumberRuleItemOperatorEnum",
    "UserListOperation",
    "UserListPrepopulationStatusEnum",
    "UserListRuleInfo",
    "UserListRuleItemGroupInfo",
    "UserListRuleItemInfo",
    "UserListRuleTypeEnum",
    "UserListSizeRangeEnum",
    "UserListStringRuleItemInfo",
    "UserListStringRuleItemOperatorEnum",
    "UserListTypeEnum",
    "UserLocationView",
    "Value",
    "VanityPharmaDisplayUrlModeEnum",
    "VanityPharmaTextEnum",
    "VideoAdInfo",
    "VideoBumperInStreamAdInfo",
    "Video",
    "VideoNonSkippableInStreamAdInfo",
    "VideoOutstreamAdInfo",
    "VideoTrueViewInStreamAdInfo",
    "WebpageConditionInfo",
    "WebpageConditionOperandEnum",
    "WebpageConditionOperatorEnum",
    "WebpageInfo",
    "YouTubeChannelInfo",
    "YoutubeVideoAsset",
    "YouTubeVideoInfo",
    "YoutubeVideoRegistrationErrorEnum",
    "CancelOperationRequest",
    "DeleteOperationRequest",
    "GetOperationRequest",
    "ListOperationsRequest",
    "ListOperationsResponse",
    "Operation",
    "OperationInfo",
    "OperationsStub",
    "Any",
    "Empty",
    "FieldMask",
    "BoolValue",
    "BytesValue",
    "DoubleValue",
    "FloatValue",
    "Int32Value",
    "Int64Value",
    "StringValue",
    "UInt32Value",
    "UInt64Value",
    "Status",
]
