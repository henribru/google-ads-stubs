from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.metrics import Metrics
from google.ads.googleads.v14.common.types.segments import Segments
from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.enums.types.summary_row_setting import (
    SummaryRowSettingEnum,
)
from google.ads.googleads.v14.resources.types.accessible_bidding_strategy import (
    AccessibleBiddingStrategy,
)
from google.ads.googleads.v14.resources.types.account_budget import AccountBudget
from google.ads.googleads.v14.resources.types.account_budget_proposal import (
    AccountBudgetProposal,
)
from google.ads.googleads.v14.resources.types.account_link import AccountLink
from google.ads.googleads.v14.resources.types.ad_group import AdGroup
from google.ads.googleads.v14.resources.types.ad_group_ad import AdGroupAd
from google.ads.googleads.v14.resources.types.ad_group_ad_asset_combination_view import (
    AdGroupAdAssetCombinationView,
)
from google.ads.googleads.v14.resources.types.ad_group_ad_asset_view import (
    AdGroupAdAssetView,
)
from google.ads.googleads.v14.resources.types.ad_group_ad_label import AdGroupAdLabel
from google.ads.googleads.v14.resources.types.ad_group_asset import AdGroupAsset
from google.ads.googleads.v14.resources.types.ad_group_asset_set import AdGroupAssetSet
from google.ads.googleads.v14.resources.types.ad_group_audience_view import (
    AdGroupAudienceView,
)
from google.ads.googleads.v14.resources.types.ad_group_bid_modifier import (
    AdGroupBidModifier,
)
from google.ads.googleads.v14.resources.types.ad_group_criterion import AdGroupCriterion
from google.ads.googleads.v14.resources.types.ad_group_criterion_customizer import (
    AdGroupCriterionCustomizer,
)
from google.ads.googleads.v14.resources.types.ad_group_criterion_label import (
    AdGroupCriterionLabel,
)
from google.ads.googleads.v14.resources.types.ad_group_criterion_simulation import (
    AdGroupCriterionSimulation,
)
from google.ads.googleads.v14.resources.types.ad_group_customizer import (
    AdGroupCustomizer,
)
from google.ads.googleads.v14.resources.types.ad_group_extension_setting import (
    AdGroupExtensionSetting,
)
from google.ads.googleads.v14.resources.types.ad_group_feed import AdGroupFeed
from google.ads.googleads.v14.resources.types.ad_group_label import AdGroupLabel
from google.ads.googleads.v14.resources.types.ad_group_simulation import (
    AdGroupSimulation,
)
from google.ads.googleads.v14.resources.types.ad_parameter import AdParameter
from google.ads.googleads.v14.resources.types.ad_schedule_view import AdScheduleView
from google.ads.googleads.v14.resources.types.age_range_view import AgeRangeView
from google.ads.googleads.v14.resources.types.asset import Asset
from google.ads.googleads.v14.resources.types.asset_field_type_view import (
    AssetFieldTypeView,
)
from google.ads.googleads.v14.resources.types.asset_group import AssetGroup
from google.ads.googleads.v14.resources.types.asset_group_asset import AssetGroupAsset
from google.ads.googleads.v14.resources.types.asset_group_listing_group_filter import (
    AssetGroupListingGroupFilter,
)
from google.ads.googleads.v14.resources.types.asset_group_product_group_view import (
    AssetGroupProductGroupView,
)
from google.ads.googleads.v14.resources.types.asset_group_signal import AssetGroupSignal
from google.ads.googleads.v14.resources.types.asset_set import AssetSet
from google.ads.googleads.v14.resources.types.asset_set_asset import AssetSetAsset
from google.ads.googleads.v14.resources.types.asset_set_type_view import (
    AssetSetTypeView,
)
from google.ads.googleads.v14.resources.types.audience import Audience
from google.ads.googleads.v14.resources.types.batch_job import BatchJob
from google.ads.googleads.v14.resources.types.bidding_data_exclusion import (
    BiddingDataExclusion,
)
from google.ads.googleads.v14.resources.types.bidding_seasonality_adjustment import (
    BiddingSeasonalityAdjustment,
)
from google.ads.googleads.v14.resources.types.bidding_strategy import BiddingStrategy
from google.ads.googleads.v14.resources.types.bidding_strategy_simulation import (
    BiddingStrategySimulation,
)
from google.ads.googleads.v14.resources.types.billing_setup import BillingSetup
from google.ads.googleads.v14.resources.types.call_view import CallView
from google.ads.googleads.v14.resources.types.campaign import Campaign
from google.ads.googleads.v14.resources.types.campaign_asset import CampaignAsset
from google.ads.googleads.v14.resources.types.campaign_asset_set import CampaignAssetSet
from google.ads.googleads.v14.resources.types.campaign_audience_view import (
    CampaignAudienceView,
)
from google.ads.googleads.v14.resources.types.campaign_bid_modifier import (
    CampaignBidModifier,
)
from google.ads.googleads.v14.resources.types.campaign_budget import CampaignBudget
from google.ads.googleads.v14.resources.types.campaign_conversion_goal import (
    CampaignConversionGoal,
)
from google.ads.googleads.v14.resources.types.campaign_criterion import (
    CampaignCriterion,
)
from google.ads.googleads.v14.resources.types.campaign_customizer import (
    CampaignCustomizer,
)
from google.ads.googleads.v14.resources.types.campaign_draft import CampaignDraft
from google.ads.googleads.v14.resources.types.campaign_extension_setting import (
    CampaignExtensionSetting,
)
from google.ads.googleads.v14.resources.types.campaign_feed import CampaignFeed
from google.ads.googleads.v14.resources.types.campaign_group import CampaignGroup
from google.ads.googleads.v14.resources.types.campaign_label import CampaignLabel
from google.ads.googleads.v14.resources.types.campaign_search_term_insight import (
    CampaignSearchTermInsight,
)
from google.ads.googleads.v14.resources.types.campaign_shared_set import (
    CampaignSharedSet,
)
from google.ads.googleads.v14.resources.types.campaign_simulation import (
    CampaignSimulation,
)
from google.ads.googleads.v14.resources.types.carrier_constant import CarrierConstant
from google.ads.googleads.v14.resources.types.change_event import ChangeEvent
from google.ads.googleads.v14.resources.types.change_status import ChangeStatus
from google.ads.googleads.v14.resources.types.click_view import ClickView
from google.ads.googleads.v14.resources.types.combined_audience import CombinedAudience
from google.ads.googleads.v14.resources.types.conversion_action import ConversionAction
from google.ads.googleads.v14.resources.types.conversion_custom_variable import (
    ConversionCustomVariable,
)
from google.ads.googleads.v14.resources.types.conversion_goal_campaign_config import (
    ConversionGoalCampaignConfig,
)
from google.ads.googleads.v14.resources.types.conversion_value_rule import (
    ConversionValueRule,
)
from google.ads.googleads.v14.resources.types.conversion_value_rule_set import (
    ConversionValueRuleSet,
)
from google.ads.googleads.v14.resources.types.currency_constant import CurrencyConstant
from google.ads.googleads.v14.resources.types.custom_audience import CustomAudience
from google.ads.googleads.v14.resources.types.custom_conversion_goal import (
    CustomConversionGoal,
)
from google.ads.googleads.v14.resources.types.custom_interest import CustomInterest
from google.ads.googleads.v14.resources.types.customer import Customer
from google.ads.googleads.v14.resources.types.customer_asset import CustomerAsset
from google.ads.googleads.v14.resources.types.customer_asset_set import CustomerAssetSet
from google.ads.googleads.v14.resources.types.customer_client import CustomerClient
from google.ads.googleads.v14.resources.types.customer_client_link import (
    CustomerClientLink,
)
from google.ads.googleads.v14.resources.types.customer_conversion_goal import (
    CustomerConversionGoal,
)
from google.ads.googleads.v14.resources.types.customer_customizer import (
    CustomerCustomizer,
)
from google.ads.googleads.v14.resources.types.customer_extension_setting import (
    CustomerExtensionSetting,
)
from google.ads.googleads.v14.resources.types.customer_feed import CustomerFeed
from google.ads.googleads.v14.resources.types.customer_label import CustomerLabel
from google.ads.googleads.v14.resources.types.customer_manager_link import (
    CustomerManagerLink,
)
from google.ads.googleads.v14.resources.types.customer_negative_criterion import (
    CustomerNegativeCriterion,
)
from google.ads.googleads.v14.resources.types.customer_search_term_insight import (
    CustomerSearchTermInsight,
)
from google.ads.googleads.v14.resources.types.customer_user_access import (
    CustomerUserAccess,
)
from google.ads.googleads.v14.resources.types.customer_user_access_invitation import (
    CustomerUserAccessInvitation,
)
from google.ads.googleads.v14.resources.types.customizer_attribute import (
    CustomizerAttribute,
)
from google.ads.googleads.v14.resources.types.detail_placement_view import (
    DetailPlacementView,
)
from google.ads.googleads.v14.resources.types.detailed_demographic import (
    DetailedDemographic,
)
from google.ads.googleads.v14.resources.types.display_keyword_view import (
    DisplayKeywordView,
)
from google.ads.googleads.v14.resources.types.distance_view import DistanceView
from google.ads.googleads.v14.resources.types.domain_category import DomainCategory
from google.ads.googleads.v14.resources.types.dynamic_search_ads_search_term_view import (
    DynamicSearchAdsSearchTermView,
)
from google.ads.googleads.v14.resources.types.expanded_landing_page_view import (
    ExpandedLandingPageView,
)
from google.ads.googleads.v14.resources.types.experiment import Experiment
from google.ads.googleads.v14.resources.types.experiment_arm import ExperimentArm
from google.ads.googleads.v14.resources.types.extension_feed_item import (
    ExtensionFeedItem,
)
from google.ads.googleads.v14.resources.types.feed import Feed
from google.ads.googleads.v14.resources.types.feed_item import FeedItem
from google.ads.googleads.v14.resources.types.feed_item_set import FeedItemSet
from google.ads.googleads.v14.resources.types.feed_item_set_link import FeedItemSetLink
from google.ads.googleads.v14.resources.types.feed_item_target import FeedItemTarget
from google.ads.googleads.v14.resources.types.feed_mapping import FeedMapping
from google.ads.googleads.v14.resources.types.feed_placeholder_view import (
    FeedPlaceholderView,
)
from google.ads.googleads.v14.resources.types.gender_view import GenderView
from google.ads.googleads.v14.resources.types.geo_target_constant import (
    GeoTargetConstant,
)
from google.ads.googleads.v14.resources.types.geographic_view import GeographicView
from google.ads.googleads.v14.resources.types.group_placement_view import (
    GroupPlacementView,
)
from google.ads.googleads.v14.resources.types.hotel_group_view import HotelGroupView
from google.ads.googleads.v14.resources.types.hotel_performance_view import (
    HotelPerformanceView,
)
from google.ads.googleads.v14.resources.types.hotel_reconciliation import (
    HotelReconciliation,
)
from google.ads.googleads.v14.resources.types.income_range_view import IncomeRangeView
from google.ads.googleads.v14.resources.types.keyword_plan import KeywordPlan
from google.ads.googleads.v14.resources.types.keyword_plan_ad_group import (
    KeywordPlanAdGroup,
)
from google.ads.googleads.v14.resources.types.keyword_plan_ad_group_keyword import (
    KeywordPlanAdGroupKeyword,
)
from google.ads.googleads.v14.resources.types.keyword_plan_campaign import (
    KeywordPlanCampaign,
)
from google.ads.googleads.v14.resources.types.keyword_plan_campaign_keyword import (
    KeywordPlanCampaignKeyword,
)
from google.ads.googleads.v14.resources.types.keyword_theme_constant import (
    KeywordThemeConstant,
)
from google.ads.googleads.v14.resources.types.keyword_view import KeywordView
from google.ads.googleads.v14.resources.types.label import Label
from google.ads.googleads.v14.resources.types.landing_page_view import LandingPageView
from google.ads.googleads.v14.resources.types.language_constant import LanguageConstant
from google.ads.googleads.v14.resources.types.lead_form_submission_data import (
    LeadFormSubmissionData,
)
from google.ads.googleads.v14.resources.types.life_event import LifeEvent
from google.ads.googleads.v14.resources.types.location_view import LocationView
from google.ads.googleads.v14.resources.types.managed_placement_view import (
    ManagedPlacementView,
)
from google.ads.googleads.v14.resources.types.media_file import MediaFile
from google.ads.googleads.v14.resources.types.mobile_app_category_constant import (
    MobileAppCategoryConstant,
)
from google.ads.googleads.v14.resources.types.mobile_device_constant import (
    MobileDeviceConstant,
)
from google.ads.googleads.v14.resources.types.offline_user_data_job import (
    OfflineUserDataJob,
)
from google.ads.googleads.v14.resources.types.operating_system_version_constant import (
    OperatingSystemVersionConstant,
)
from google.ads.googleads.v14.resources.types.paid_organic_search_term_view import (
    PaidOrganicSearchTermView,
)
from google.ads.googleads.v14.resources.types.parental_status_view import (
    ParentalStatusView,
)
from google.ads.googleads.v14.resources.types.per_store_view import PerStoreView
from google.ads.googleads.v14.resources.types.product_bidding_category_constant import (
    ProductBiddingCategoryConstant,
)
from google.ads.googleads.v14.resources.types.product_group_view import ProductGroupView
from google.ads.googleads.v14.resources.types.product_link import ProductLink
from google.ads.googleads.v14.resources.types.qualifying_question import (
    QualifyingQuestion,
)
from google.ads.googleads.v14.resources.types.recommendation import Recommendation
from google.ads.googleads.v14.resources.types.remarketing_action import (
    RemarketingAction,
)
from google.ads.googleads.v14.resources.types.search_term_view import SearchTermView
from google.ads.googleads.v14.resources.types.shared_criterion import SharedCriterion
from google.ads.googleads.v14.resources.types.shared_set import SharedSet
from google.ads.googleads.v14.resources.types.shopping_performance_view import (
    ShoppingPerformanceView,
)
from google.ads.googleads.v14.resources.types.smart_campaign_search_term_view import (
    SmartCampaignSearchTermView,
)
from google.ads.googleads.v14.resources.types.smart_campaign_setting import (
    SmartCampaignSetting,
)
from google.ads.googleads.v14.resources.types.third_party_app_analytics_link import (
    ThirdPartyAppAnalyticsLink,
)
from google.ads.googleads.v14.resources.types.topic_constant import TopicConstant
from google.ads.googleads.v14.resources.types.topic_view import TopicView
from google.ads.googleads.v14.resources.types.travel_activity_group_view import (
    TravelActivityGroupView,
)
from google.ads.googleads.v14.resources.types.travel_activity_performance_view import (
    TravelActivityPerformanceView,
)
from google.ads.googleads.v14.resources.types.user_interest import UserInterest
from google.ads.googleads.v14.resources.types.user_list import UserList
from google.ads.googleads.v14.resources.types.user_location_view import UserLocationView
from google.ads.googleads.v14.resources.types.video import Video
from google.ads.googleads.v14.resources.types.webpage_view import WebpageView
from google.ads.googleads.v14.services.types.ad_group_ad_label_service import (
    AdGroupAdLabelOperation,
    MutateAdGroupAdLabelResult,
)
from google.ads.googleads.v14.services.types.ad_group_ad_service import (
    AdGroupAdOperation,
    MutateAdGroupAdResult,
)
from google.ads.googleads.v14.services.types.ad_group_asset_service import (
    AdGroupAssetOperation,
    MutateAdGroupAssetResult,
)
from google.ads.googleads.v14.services.types.ad_group_bid_modifier_service import (
    AdGroupBidModifierOperation,
    MutateAdGroupBidModifierResult,
)
from google.ads.googleads.v14.services.types.ad_group_criterion_customizer_service import (
    AdGroupCriterionCustomizerOperation,
    MutateAdGroupCriterionCustomizerResult,
)
from google.ads.googleads.v14.services.types.ad_group_criterion_label_service import (
    AdGroupCriterionLabelOperation,
    MutateAdGroupCriterionLabelResult,
)
from google.ads.googleads.v14.services.types.ad_group_criterion_service import (
    AdGroupCriterionOperation,
    MutateAdGroupCriterionResult,
)
from google.ads.googleads.v14.services.types.ad_group_customizer_service import (
    AdGroupCustomizerOperation,
    MutateAdGroupCustomizerResult,
)
from google.ads.googleads.v14.services.types.ad_group_extension_setting_service import (
    AdGroupExtensionSettingOperation,
    MutateAdGroupExtensionSettingResult,
)
from google.ads.googleads.v14.services.types.ad_group_feed_service import (
    AdGroupFeedOperation,
    MutateAdGroupFeedResult,
)
from google.ads.googleads.v14.services.types.ad_group_label_service import (
    AdGroupLabelOperation,
    MutateAdGroupLabelResult,
)
from google.ads.googleads.v14.services.types.ad_group_service import (
    AdGroupOperation,
    MutateAdGroupResult,
)
from google.ads.googleads.v14.services.types.ad_parameter_service import (
    AdParameterOperation,
    MutateAdParameterResult,
)
from google.ads.googleads.v14.services.types.ad_service import (
    AdOperation,
    MutateAdResult,
)
from google.ads.googleads.v14.services.types.asset_group_asset_service import (
    AssetGroupAssetOperation,
    MutateAssetGroupAssetResult,
)
from google.ads.googleads.v14.services.types.asset_group_listing_group_filter_service import (
    AssetGroupListingGroupFilterOperation,
    MutateAssetGroupListingGroupFilterResult,
)
from google.ads.googleads.v14.services.types.asset_group_service import (
    AssetGroupOperation,
    MutateAssetGroupResult,
)
from google.ads.googleads.v14.services.types.asset_group_signal_service import (
    AssetGroupSignalOperation,
    MutateAssetGroupSignalResult,
)
from google.ads.googleads.v14.services.types.asset_service import (
    AssetOperation,
    MutateAssetResult,
)
from google.ads.googleads.v14.services.types.asset_set_asset_service import (
    AssetSetAssetOperation,
    MutateAssetSetAssetResult,
)
from google.ads.googleads.v14.services.types.asset_set_service import (
    AssetSetOperation,
    MutateAssetSetResult,
)
from google.ads.googleads.v14.services.types.audience_service import (
    AudienceOperation,
    MutateAudienceResult,
)
from google.ads.googleads.v14.services.types.bidding_data_exclusion_service import (
    BiddingDataExclusionOperation,
    MutateBiddingDataExclusionsResult,
)
from google.ads.googleads.v14.services.types.bidding_seasonality_adjustment_service import (
    BiddingSeasonalityAdjustmentOperation,
    MutateBiddingSeasonalityAdjustmentsResult,
)
from google.ads.googleads.v14.services.types.bidding_strategy_service import (
    BiddingStrategyOperation,
    MutateBiddingStrategyResult,
)
from google.ads.googleads.v14.services.types.campaign_asset_service import (
    CampaignAssetOperation,
    MutateCampaignAssetResult,
)
from google.ads.googleads.v14.services.types.campaign_asset_set_service import (
    CampaignAssetSetOperation,
    MutateCampaignAssetSetResult,
)
from google.ads.googleads.v14.services.types.campaign_bid_modifier_service import (
    CampaignBidModifierOperation,
    MutateCampaignBidModifierResult,
)
from google.ads.googleads.v14.services.types.campaign_budget_service import (
    CampaignBudgetOperation,
    MutateCampaignBudgetResult,
)
from google.ads.googleads.v14.services.types.campaign_conversion_goal_service import (
    CampaignConversionGoalOperation,
    MutateCampaignConversionGoalResult,
)
from google.ads.googleads.v14.services.types.campaign_criterion_service import (
    CampaignCriterionOperation,
    MutateCampaignCriterionResult,
)
from google.ads.googleads.v14.services.types.campaign_customizer_service import (
    CampaignCustomizerOperation,
    MutateCampaignCustomizerResult,
)
from google.ads.googleads.v14.services.types.campaign_draft_service import (
    CampaignDraftOperation,
    MutateCampaignDraftResult,
)
from google.ads.googleads.v14.services.types.campaign_extension_setting_service import (
    CampaignExtensionSettingOperation,
    MutateCampaignExtensionSettingResult,
)
from google.ads.googleads.v14.services.types.campaign_feed_service import (
    CampaignFeedOperation,
    MutateCampaignFeedResult,
)
from google.ads.googleads.v14.services.types.campaign_group_service import (
    CampaignGroupOperation,
    MutateCampaignGroupResult,
)
from google.ads.googleads.v14.services.types.campaign_label_service import (
    CampaignLabelOperation,
    MutateCampaignLabelResult,
)
from google.ads.googleads.v14.services.types.campaign_service import (
    CampaignOperation,
    MutateCampaignResult,
)
from google.ads.googleads.v14.services.types.campaign_shared_set_service import (
    CampaignSharedSetOperation,
    MutateCampaignSharedSetResult,
)
from google.ads.googleads.v14.services.types.conversion_action_service import (
    ConversionActionOperation,
    MutateConversionActionResult,
)
from google.ads.googleads.v14.services.types.conversion_custom_variable_service import (
    ConversionCustomVariableOperation,
    MutateConversionCustomVariableResult,
)
from google.ads.googleads.v14.services.types.conversion_goal_campaign_config_service import (
    ConversionGoalCampaignConfigOperation,
    MutateConversionGoalCampaignConfigResult,
)
from google.ads.googleads.v14.services.types.conversion_value_rule_service import (
    ConversionValueRuleOperation,
    MutateConversionValueRuleResult,
)
from google.ads.googleads.v14.services.types.conversion_value_rule_set_service import (
    ConversionValueRuleSetOperation,
    MutateConversionValueRuleSetResult,
)
from google.ads.googleads.v14.services.types.custom_conversion_goal_service import (
    CustomConversionGoalOperation,
    MutateCustomConversionGoalResult,
)
from google.ads.googleads.v14.services.types.customer_asset_service import (
    CustomerAssetOperation,
    MutateCustomerAssetResult,
)
from google.ads.googleads.v14.services.types.customer_conversion_goal_service import (
    CustomerConversionGoalOperation,
    MutateCustomerConversionGoalResult,
)
from google.ads.googleads.v14.services.types.customer_customizer_service import (
    CustomerCustomizerOperation,
    MutateCustomerCustomizerResult,
)
from google.ads.googleads.v14.services.types.customer_extension_setting_service import (
    CustomerExtensionSettingOperation,
    MutateCustomerExtensionSettingResult,
)
from google.ads.googleads.v14.services.types.customer_feed_service import (
    CustomerFeedOperation,
    MutateCustomerFeedResult,
)
from google.ads.googleads.v14.services.types.customer_label_service import (
    CustomerLabelOperation,
    MutateCustomerLabelResult,
)
from google.ads.googleads.v14.services.types.customer_negative_criterion_service import (
    CustomerNegativeCriterionOperation,
    MutateCustomerNegativeCriteriaResult,
)
from google.ads.googleads.v14.services.types.customer_service import (
    CustomerOperation,
    MutateCustomerResult,
)
from google.ads.googleads.v14.services.types.customizer_attribute_service import (
    CustomizerAttributeOperation,
    MutateCustomizerAttributeResult,
)
from google.ads.googleads.v14.services.types.experiment_arm_service import (
    ExperimentArmOperation,
    MutateExperimentArmResult,
)
from google.ads.googleads.v14.services.types.experiment_service import (
    ExperimentOperation,
    MutateExperimentResult,
)
from google.ads.googleads.v14.services.types.extension_feed_item_service import (
    ExtensionFeedItemOperation,
    MutateExtensionFeedItemResult,
)
from google.ads.googleads.v14.services.types.feed_item_service import (
    FeedItemOperation,
    MutateFeedItemResult,
)
from google.ads.googleads.v14.services.types.feed_item_set_link_service import (
    FeedItemSetLinkOperation,
    MutateFeedItemSetLinkResult,
)
from google.ads.googleads.v14.services.types.feed_item_set_service import (
    FeedItemSetOperation,
    MutateFeedItemSetResult,
)
from google.ads.googleads.v14.services.types.feed_item_target_service import (
    FeedItemTargetOperation,
    MutateFeedItemTargetResult,
)
from google.ads.googleads.v14.services.types.feed_mapping_service import (
    FeedMappingOperation,
    MutateFeedMappingResult,
)
from google.ads.googleads.v14.services.types.feed_service import (
    FeedOperation,
    MutateFeedResult,
)
from google.ads.googleads.v14.services.types.keyword_plan_ad_group_keyword_service import (
    KeywordPlanAdGroupKeywordOperation,
    MutateKeywordPlanAdGroupKeywordResult,
)
from google.ads.googleads.v14.services.types.keyword_plan_ad_group_service import (
    KeywordPlanAdGroupOperation,
    MutateKeywordPlanAdGroupResult,
)
from google.ads.googleads.v14.services.types.keyword_plan_campaign_keyword_service import (
    KeywordPlanCampaignKeywordOperation,
    MutateKeywordPlanCampaignKeywordResult,
)
from google.ads.googleads.v14.services.types.keyword_plan_campaign_service import (
    KeywordPlanCampaignOperation,
    MutateKeywordPlanCampaignResult,
)
from google.ads.googleads.v14.services.types.keyword_plan_service import (
    KeywordPlanOperation,
    MutateKeywordPlansResult,
)
from google.ads.googleads.v14.services.types.label_service import (
    LabelOperation,
    MutateLabelResult,
)
from google.ads.googleads.v14.services.types.media_file_service import (
    MediaFileOperation,
    MutateMediaFileResult,
)
from google.ads.googleads.v14.services.types.remarketing_action_service import (
    MutateRemarketingActionResult,
    RemarketingActionOperation,
)
from google.ads.googleads.v14.services.types.shared_criterion_service import (
    MutateSharedCriterionResult,
    SharedCriterionOperation,
)
from google.ads.googleads.v14.services.types.shared_set_service import (
    MutateSharedSetResult,
    SharedSetOperation,
)
from google.ads.googleads.v14.services.types.smart_campaign_setting_service import (
    MutateSmartCampaignSettingResult,
    SmartCampaignSettingOperation,
)
from google.ads.googleads.v14.services.types.user_list_service import (
    MutateUserListResult,
    UserListOperation,
)

_M = TypeVar("_M")

class GoogleAdsRow(proto.Message):
    account_budget: AccountBudget
    account_budget_proposal: AccountBudgetProposal
    account_link: AccountLink
    ad_group: AdGroup
    ad_group_ad: AdGroupAd
    ad_group_ad_asset_combination_view: AdGroupAdAssetCombinationView
    ad_group_ad_asset_view: AdGroupAdAssetView
    ad_group_ad_label: AdGroupAdLabel
    ad_group_asset: AdGroupAsset
    ad_group_asset_set: AdGroupAssetSet
    ad_group_audience_view: AdGroupAudienceView
    ad_group_bid_modifier: AdGroupBidModifier
    ad_group_criterion: AdGroupCriterion
    ad_group_criterion_customizer: AdGroupCriterionCustomizer
    ad_group_criterion_label: AdGroupCriterionLabel
    ad_group_criterion_simulation: AdGroupCriterionSimulation
    ad_group_customizer: AdGroupCustomizer
    ad_group_extension_setting: AdGroupExtensionSetting
    ad_group_feed: AdGroupFeed
    ad_group_label: AdGroupLabel
    ad_group_simulation: AdGroupSimulation
    ad_parameter: AdParameter
    age_range_view: AgeRangeView
    ad_schedule_view: AdScheduleView
    domain_category: DomainCategory
    asset: Asset
    asset_field_type_view: AssetFieldTypeView
    asset_group_asset: AssetGroupAsset
    asset_group_signal: AssetGroupSignal
    asset_group_listing_group_filter: AssetGroupListingGroupFilter
    asset_group_product_group_view: AssetGroupProductGroupView
    asset_group: AssetGroup
    asset_set_asset: AssetSetAsset
    asset_set: AssetSet
    asset_set_type_view: AssetSetTypeView
    batch_job: BatchJob
    bidding_data_exclusion: BiddingDataExclusion
    bidding_seasonality_adjustment: BiddingSeasonalityAdjustment
    bidding_strategy: BiddingStrategy
    bidding_strategy_simulation: BiddingStrategySimulation
    billing_setup: BillingSetup
    call_view: CallView
    campaign_budget: CampaignBudget
    campaign: Campaign
    campaign_asset: CampaignAsset
    campaign_asset_set: CampaignAssetSet
    campaign_audience_view: CampaignAudienceView
    campaign_bid_modifier: CampaignBidModifier
    campaign_conversion_goal: CampaignConversionGoal
    campaign_criterion: CampaignCriterion
    campaign_customizer: CampaignCustomizer
    campaign_draft: CampaignDraft
    campaign_extension_setting: CampaignExtensionSetting
    campaign_feed: CampaignFeed
    campaign_group: CampaignGroup
    campaign_label: CampaignLabel
    campaign_search_term_insight: CampaignSearchTermInsight
    campaign_shared_set: CampaignSharedSet
    campaign_simulation: CampaignSimulation
    carrier_constant: CarrierConstant
    change_event: ChangeEvent
    change_status: ChangeStatus
    combined_audience: CombinedAudience
    audience: Audience
    conversion_action: ConversionAction
    conversion_custom_variable: ConversionCustomVariable
    conversion_goal_campaign_config: ConversionGoalCampaignConfig
    conversion_value_rule: ConversionValueRule
    conversion_value_rule_set: ConversionValueRuleSet
    click_view: ClickView
    currency_constant: CurrencyConstant
    custom_audience: CustomAudience
    custom_conversion_goal: CustomConversionGoal
    custom_interest: CustomInterest
    customer: Customer
    customer_asset: CustomerAsset
    customer_asset_set: CustomerAssetSet
    accessible_bidding_strategy: AccessibleBiddingStrategy
    customer_customizer: CustomerCustomizer
    customer_manager_link: CustomerManagerLink
    customer_client_link: CustomerClientLink
    customer_client: CustomerClient
    customer_conversion_goal: CustomerConversionGoal
    customer_extension_setting: CustomerExtensionSetting
    customer_feed: CustomerFeed
    customer_label: CustomerLabel
    customer_negative_criterion: CustomerNegativeCriterion
    customer_search_term_insight: CustomerSearchTermInsight
    customer_user_access: CustomerUserAccess
    customer_user_access_invitation: CustomerUserAccessInvitation
    customizer_attribute: CustomizerAttribute
    detail_placement_view: DetailPlacementView
    detailed_demographic: DetailedDemographic
    display_keyword_view: DisplayKeywordView
    distance_view: DistanceView
    dynamic_search_ads_search_term_view: DynamicSearchAdsSearchTermView
    expanded_landing_page_view: ExpandedLandingPageView
    extension_feed_item: ExtensionFeedItem
    feed: Feed
    feed_item: FeedItem
    feed_item_set: FeedItemSet
    feed_item_set_link: FeedItemSetLink
    feed_item_target: FeedItemTarget
    feed_mapping: FeedMapping
    feed_placeholder_view: FeedPlaceholderView
    gender_view: GenderView
    geo_target_constant: GeoTargetConstant
    geographic_view: GeographicView
    group_placement_view: GroupPlacementView
    hotel_group_view: HotelGroupView
    hotel_performance_view: HotelPerformanceView
    hotel_reconciliation: HotelReconciliation
    income_range_view: IncomeRangeView
    keyword_view: KeywordView
    keyword_plan: KeywordPlan
    keyword_plan_campaign: KeywordPlanCampaign
    keyword_plan_campaign_keyword: KeywordPlanCampaignKeyword
    keyword_plan_ad_group: KeywordPlanAdGroup
    keyword_plan_ad_group_keyword: KeywordPlanAdGroupKeyword
    keyword_theme_constant: KeywordThemeConstant
    label: Label
    landing_page_view: LandingPageView
    language_constant: LanguageConstant
    location_view: LocationView
    managed_placement_view: ManagedPlacementView
    media_file: MediaFile
    mobile_app_category_constant: MobileAppCategoryConstant
    mobile_device_constant: MobileDeviceConstant
    offline_user_data_job: OfflineUserDataJob
    operating_system_version_constant: OperatingSystemVersionConstant
    paid_organic_search_term_view: PaidOrganicSearchTermView
    qualifying_question: QualifyingQuestion
    parental_status_view: ParentalStatusView
    per_store_view: PerStoreView
    product_bidding_category_constant: ProductBiddingCategoryConstant
    product_group_view: ProductGroupView
    product_link: ProductLink
    recommendation: Recommendation
    search_term_view: SearchTermView
    shared_criterion: SharedCriterion
    shared_set: SharedSet
    smart_campaign_setting: SmartCampaignSetting
    shopping_performance_view: ShoppingPerformanceView
    smart_campaign_search_term_view: SmartCampaignSearchTermView
    third_party_app_analytics_link: ThirdPartyAppAnalyticsLink
    topic_view: TopicView
    travel_activity_group_view: TravelActivityGroupView
    travel_activity_performance_view: TravelActivityPerformanceView
    experiment: Experiment
    experiment_arm: ExperimentArm
    user_interest: UserInterest
    life_event: LifeEvent
    user_list: UserList
    user_location_view: UserLocationView
    remarketing_action: RemarketingAction
    topic_constant: TopicConstant
    video: Video
    webpage_view: WebpageView
    lead_form_submission_data: LeadFormSubmissionData
    metrics: Metrics
    segments: Segments
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        account_budget: AccountBudget = ...,
        account_budget_proposal: AccountBudgetProposal = ...,
        account_link: AccountLink = ...,
        ad_group: AdGroup = ...,
        ad_group_ad: AdGroupAd = ...,
        ad_group_ad_asset_combination_view: AdGroupAdAssetCombinationView = ...,
        ad_group_ad_asset_view: AdGroupAdAssetView = ...,
        ad_group_ad_label: AdGroupAdLabel = ...,
        ad_group_asset: AdGroupAsset = ...,
        ad_group_asset_set: AdGroupAssetSet = ...,
        ad_group_audience_view: AdGroupAudienceView = ...,
        ad_group_bid_modifier: AdGroupBidModifier = ...,
        ad_group_criterion: AdGroupCriterion = ...,
        ad_group_criterion_customizer: AdGroupCriterionCustomizer = ...,
        ad_group_criterion_label: AdGroupCriterionLabel = ...,
        ad_group_criterion_simulation: AdGroupCriterionSimulation = ...,
        ad_group_customizer: AdGroupCustomizer = ...,
        ad_group_extension_setting: AdGroupExtensionSetting = ...,
        ad_group_feed: AdGroupFeed = ...,
        ad_group_label: AdGroupLabel = ...,
        ad_group_simulation: AdGroupSimulation = ...,
        ad_parameter: AdParameter = ...,
        age_range_view: AgeRangeView = ...,
        ad_schedule_view: AdScheduleView = ...,
        domain_category: DomainCategory = ...,
        asset: Asset = ...,
        asset_field_type_view: AssetFieldTypeView = ...,
        asset_group_asset: AssetGroupAsset = ...,
        asset_group_signal: AssetGroupSignal = ...,
        asset_group_listing_group_filter: AssetGroupListingGroupFilter = ...,
        asset_group_product_group_view: AssetGroupProductGroupView = ...,
        asset_group: AssetGroup = ...,
        asset_set_asset: AssetSetAsset = ...,
        asset_set: AssetSet = ...,
        asset_set_type_view: AssetSetTypeView = ...,
        batch_job: BatchJob = ...,
        bidding_data_exclusion: BiddingDataExclusion = ...,
        bidding_seasonality_adjustment: BiddingSeasonalityAdjustment = ...,
        bidding_strategy: BiddingStrategy = ...,
        bidding_strategy_simulation: BiddingStrategySimulation = ...,
        billing_setup: BillingSetup = ...,
        call_view: CallView = ...,
        campaign_budget: CampaignBudget = ...,
        campaign: Campaign = ...,
        campaign_asset: CampaignAsset = ...,
        campaign_asset_set: CampaignAssetSet = ...,
        campaign_audience_view: CampaignAudienceView = ...,
        campaign_bid_modifier: CampaignBidModifier = ...,
        campaign_conversion_goal: CampaignConversionGoal = ...,
        campaign_criterion: CampaignCriterion = ...,
        campaign_customizer: CampaignCustomizer = ...,
        campaign_draft: CampaignDraft = ...,
        campaign_extension_setting: CampaignExtensionSetting = ...,
        campaign_feed: CampaignFeed = ...,
        campaign_group: CampaignGroup = ...,
        campaign_label: CampaignLabel = ...,
        campaign_search_term_insight: CampaignSearchTermInsight = ...,
        campaign_shared_set: CampaignSharedSet = ...,
        campaign_simulation: CampaignSimulation = ...,
        carrier_constant: CarrierConstant = ...,
        change_event: ChangeEvent = ...,
        change_status: ChangeStatus = ...,
        combined_audience: CombinedAudience = ...,
        audience: Audience = ...,
        conversion_action: ConversionAction = ...,
        conversion_custom_variable: ConversionCustomVariable = ...,
        conversion_goal_campaign_config: ConversionGoalCampaignConfig = ...,
        conversion_value_rule: ConversionValueRule = ...,
        conversion_value_rule_set: ConversionValueRuleSet = ...,
        click_view: ClickView = ...,
        currency_constant: CurrencyConstant = ...,
        custom_audience: CustomAudience = ...,
        custom_conversion_goal: CustomConversionGoal = ...,
        custom_interest: CustomInterest = ...,
        customer: Customer = ...,
        customer_asset: CustomerAsset = ...,
        customer_asset_set: CustomerAssetSet = ...,
        accessible_bidding_strategy: AccessibleBiddingStrategy = ...,
        customer_customizer: CustomerCustomizer = ...,
        customer_manager_link: CustomerManagerLink = ...,
        customer_client_link: CustomerClientLink = ...,
        customer_client: CustomerClient = ...,
        customer_conversion_goal: CustomerConversionGoal = ...,
        customer_extension_setting: CustomerExtensionSetting = ...,
        customer_feed: CustomerFeed = ...,
        customer_label: CustomerLabel = ...,
        customer_negative_criterion: CustomerNegativeCriterion = ...,
        customer_search_term_insight: CustomerSearchTermInsight = ...,
        customer_user_access: CustomerUserAccess = ...,
        customer_user_access_invitation: CustomerUserAccessInvitation = ...,
        customizer_attribute: CustomizerAttribute = ...,
        detail_placement_view: DetailPlacementView = ...,
        detailed_demographic: DetailedDemographic = ...,
        display_keyword_view: DisplayKeywordView = ...,
        distance_view: DistanceView = ...,
        dynamic_search_ads_search_term_view: DynamicSearchAdsSearchTermView = ...,
        expanded_landing_page_view: ExpandedLandingPageView = ...,
        extension_feed_item: ExtensionFeedItem = ...,
        feed: Feed = ...,
        feed_item: FeedItem = ...,
        feed_item_set: FeedItemSet = ...,
        feed_item_set_link: FeedItemSetLink = ...,
        feed_item_target: FeedItemTarget = ...,
        feed_mapping: FeedMapping = ...,
        feed_placeholder_view: FeedPlaceholderView = ...,
        gender_view: GenderView = ...,
        geo_target_constant: GeoTargetConstant = ...,
        geographic_view: GeographicView = ...,
        group_placement_view: GroupPlacementView = ...,
        hotel_group_view: HotelGroupView = ...,
        hotel_performance_view: HotelPerformanceView = ...,
        hotel_reconciliation: HotelReconciliation = ...,
        income_range_view: IncomeRangeView = ...,
        keyword_view: KeywordView = ...,
        keyword_plan: KeywordPlan = ...,
        keyword_plan_campaign: KeywordPlanCampaign = ...,
        keyword_plan_campaign_keyword: KeywordPlanCampaignKeyword = ...,
        keyword_plan_ad_group: KeywordPlanAdGroup = ...,
        keyword_plan_ad_group_keyword: KeywordPlanAdGroupKeyword = ...,
        keyword_theme_constant: KeywordThemeConstant = ...,
        label: Label = ...,
        landing_page_view: LandingPageView = ...,
        language_constant: LanguageConstant = ...,
        location_view: LocationView = ...,
        managed_placement_view: ManagedPlacementView = ...,
        media_file: MediaFile = ...,
        mobile_app_category_constant: MobileAppCategoryConstant = ...,
        mobile_device_constant: MobileDeviceConstant = ...,
        offline_user_data_job: OfflineUserDataJob = ...,
        operating_system_version_constant: OperatingSystemVersionConstant = ...,
        paid_organic_search_term_view: PaidOrganicSearchTermView = ...,
        qualifying_question: QualifyingQuestion = ...,
        parental_status_view: ParentalStatusView = ...,
        per_store_view: PerStoreView = ...,
        product_bidding_category_constant: ProductBiddingCategoryConstant = ...,
        product_group_view: ProductGroupView = ...,
        product_link: ProductLink = ...,
        recommendation: Recommendation = ...,
        search_term_view: SearchTermView = ...,
        shared_criterion: SharedCriterion = ...,
        shared_set: SharedSet = ...,
        smart_campaign_setting: SmartCampaignSetting = ...,
        shopping_performance_view: ShoppingPerformanceView = ...,
        smart_campaign_search_term_view: SmartCampaignSearchTermView = ...,
        third_party_app_analytics_link: ThirdPartyAppAnalyticsLink = ...,
        topic_view: TopicView = ...,
        travel_activity_group_view: TravelActivityGroupView = ...,
        travel_activity_performance_view: TravelActivityPerformanceView = ...,
        experiment: Experiment = ...,
        experiment_arm: ExperimentArm = ...,
        user_interest: UserInterest = ...,
        life_event: LifeEvent = ...,
        user_list: UserList = ...,
        user_location_view: UserLocationView = ...,
        remarketing_action: RemarketingAction = ...,
        topic_constant: TopicConstant = ...,
        video: Video = ...,
        webpage_view: WebpageView = ...,
        lead_form_submission_data: LeadFormSubmissionData = ...,
        metrics: Metrics = ...,
        segments: Segments = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "account_budget",
            "account_budget_proposal",
            "account_link",
            "ad_group",
            "ad_group_ad",
            "ad_group_ad_asset_combination_view",
            "ad_group_ad_asset_view",
            "ad_group_ad_label",
            "ad_group_asset",
            "ad_group_asset_set",
            "ad_group_audience_view",
            "ad_group_bid_modifier",
            "ad_group_criterion",
            "ad_group_criterion_customizer",
            "ad_group_criterion_label",
            "ad_group_criterion_simulation",
            "ad_group_customizer",
            "ad_group_extension_setting",
            "ad_group_feed",
            "ad_group_label",
            "ad_group_simulation",
            "ad_parameter",
            "age_range_view",
            "ad_schedule_view",
            "domain_category",
            "asset",
            "asset_field_type_view",
            "asset_group_asset",
            "asset_group_signal",
            "asset_group_listing_group_filter",
            "asset_group_product_group_view",
            "asset_group",
            "asset_set_asset",
            "asset_set",
            "asset_set_type_view",
            "batch_job",
            "bidding_data_exclusion",
            "bidding_seasonality_adjustment",
            "bidding_strategy",
            "bidding_strategy_simulation",
            "billing_setup",
            "call_view",
            "campaign_budget",
            "campaign",
            "campaign_asset",
            "campaign_asset_set",
            "campaign_audience_view",
            "campaign_bid_modifier",
            "campaign_conversion_goal",
            "campaign_criterion",
            "campaign_customizer",
            "campaign_draft",
            "campaign_extension_setting",
            "campaign_feed",
            "campaign_group",
            "campaign_label",
            "campaign_search_term_insight",
            "campaign_shared_set",
            "campaign_simulation",
            "carrier_constant",
            "change_event",
            "change_status",
            "combined_audience",
            "audience",
            "conversion_action",
            "conversion_custom_variable",
            "conversion_goal_campaign_config",
            "conversion_value_rule",
            "conversion_value_rule_set",
            "click_view",
            "currency_constant",
            "custom_audience",
            "custom_conversion_goal",
            "custom_interest",
            "customer",
            "customer_asset",
            "customer_asset_set",
            "accessible_bidding_strategy",
            "customer_customizer",
            "customer_manager_link",
            "customer_client_link",
            "customer_client",
            "customer_conversion_goal",
            "customer_extension_setting",
            "customer_feed",
            "customer_label",
            "customer_negative_criterion",
            "customer_search_term_insight",
            "customer_user_access",
            "customer_user_access_invitation",
            "customizer_attribute",
            "detail_placement_view",
            "detailed_demographic",
            "display_keyword_view",
            "distance_view",
            "dynamic_search_ads_search_term_view",
            "expanded_landing_page_view",
            "extension_feed_item",
            "feed",
            "feed_item",
            "feed_item_set",
            "feed_item_set_link",
            "feed_item_target",
            "feed_mapping",
            "feed_placeholder_view",
            "gender_view",
            "geo_target_constant",
            "geographic_view",
            "group_placement_view",
            "hotel_group_view",
            "hotel_performance_view",
            "hotel_reconciliation",
            "income_range_view",
            "keyword_view",
            "keyword_plan",
            "keyword_plan_campaign",
            "keyword_plan_campaign_keyword",
            "keyword_plan_ad_group",
            "keyword_plan_ad_group_keyword",
            "keyword_theme_constant",
            "label",
            "landing_page_view",
            "language_constant",
            "location_view",
            "managed_placement_view",
            "media_file",
            "mobile_app_category_constant",
            "mobile_device_constant",
            "offline_user_data_job",
            "operating_system_version_constant",
            "paid_organic_search_term_view",
            "qualifying_question",
            "parental_status_view",
            "per_store_view",
            "product_bidding_category_constant",
            "product_group_view",
            "product_link",
            "recommendation",
            "search_term_view",
            "shared_criterion",
            "shared_set",
            "smart_campaign_setting",
            "shopping_performance_view",
            "smart_campaign_search_term_view",
            "third_party_app_analytics_link",
            "topic_view",
            "travel_activity_group_view",
            "travel_activity_performance_view",
            "experiment",
            "experiment_arm",
            "user_interest",
            "life_event",
            "user_list",
            "user_location_view",
            "remarketing_action",
            "topic_constant",
            "video",
            "webpage_view",
            "lead_form_submission_data",
            "metrics",
            "segments",
        ],
    ) -> bool: ...

class MutateGoogleAdsRequest(proto.Message):
    customer_id: str
    mutate_operations: MutableSequence[MutateOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        mutate_operations: MutableSequence[MutateOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "mutate_operations",
            "partial_failure",
            "validate_only",
            "response_content_type",
        ],
    ) -> bool: ...

class MutateGoogleAdsResponse(proto.Message):
    partial_failure_error: Status
    mutate_operation_responses: MutableSequence[MutateOperationResponse]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        mutate_operation_responses: MutableSequence[MutateOperationResponse] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "mutate_operation_responses"]
    ) -> bool: ...

class MutateOperation(proto.Message):
    ad_group_ad_label_operation: AdGroupAdLabelOperation
    ad_group_ad_operation: AdGroupAdOperation
    ad_group_asset_operation: AdGroupAssetOperation
    ad_group_bid_modifier_operation: AdGroupBidModifierOperation
    ad_group_criterion_customizer_operation: AdGroupCriterionCustomizerOperation
    ad_group_criterion_label_operation: AdGroupCriterionLabelOperation
    ad_group_criterion_operation: AdGroupCriterionOperation
    ad_group_customizer_operation: AdGroupCustomizerOperation
    ad_group_extension_setting_operation: AdGroupExtensionSettingOperation
    ad_group_feed_operation: AdGroupFeedOperation
    ad_group_label_operation: AdGroupLabelOperation
    ad_group_operation: AdGroupOperation
    ad_operation: AdOperation
    ad_parameter_operation: AdParameterOperation
    asset_operation: AssetOperation
    asset_group_asset_operation: AssetGroupAssetOperation
    asset_group_listing_group_filter_operation: AssetGroupListingGroupFilterOperation
    asset_group_signal_operation: AssetGroupSignalOperation
    asset_group_operation: AssetGroupOperation
    asset_set_asset_operation: AssetSetAssetOperation
    asset_set_operation: AssetSetOperation
    audience_operation: AudienceOperation
    bidding_data_exclusion_operation: BiddingDataExclusionOperation
    bidding_seasonality_adjustment_operation: BiddingSeasonalityAdjustmentOperation
    bidding_strategy_operation: BiddingStrategyOperation
    campaign_asset_operation: CampaignAssetOperation
    campaign_asset_set_operation: CampaignAssetSetOperation
    campaign_bid_modifier_operation: CampaignBidModifierOperation
    campaign_budget_operation: CampaignBudgetOperation
    campaign_conversion_goal_operation: CampaignConversionGoalOperation
    campaign_criterion_operation: CampaignCriterionOperation
    campaign_customizer_operation: CampaignCustomizerOperation
    campaign_draft_operation: CampaignDraftOperation
    campaign_extension_setting_operation: CampaignExtensionSettingOperation
    campaign_feed_operation: CampaignFeedOperation
    campaign_group_operation: CampaignGroupOperation
    campaign_label_operation: CampaignLabelOperation
    campaign_operation: CampaignOperation
    campaign_shared_set_operation: CampaignSharedSetOperation
    conversion_action_operation: ConversionActionOperation
    conversion_custom_variable_operation: ConversionCustomVariableOperation
    conversion_goal_campaign_config_operation: ConversionGoalCampaignConfigOperation
    conversion_value_rule_operation: ConversionValueRuleOperation
    conversion_value_rule_set_operation: ConversionValueRuleSetOperation
    custom_conversion_goal_operation: CustomConversionGoalOperation
    customer_asset_operation: CustomerAssetOperation
    customer_conversion_goal_operation: CustomerConversionGoalOperation
    customer_customizer_operation: CustomerCustomizerOperation
    customer_extension_setting_operation: CustomerExtensionSettingOperation
    customer_feed_operation: CustomerFeedOperation
    customer_label_operation: CustomerLabelOperation
    customer_negative_criterion_operation: CustomerNegativeCriterionOperation
    customer_operation: CustomerOperation
    customizer_attribute_operation: CustomizerAttributeOperation
    experiment_operation: ExperimentOperation
    experiment_arm_operation: ExperimentArmOperation
    extension_feed_item_operation: ExtensionFeedItemOperation
    feed_item_operation: FeedItemOperation
    feed_item_set_operation: FeedItemSetOperation
    feed_item_set_link_operation: FeedItemSetLinkOperation
    feed_item_target_operation: FeedItemTargetOperation
    feed_mapping_operation: FeedMappingOperation
    feed_operation: FeedOperation
    keyword_plan_ad_group_operation: KeywordPlanAdGroupOperation
    keyword_plan_ad_group_keyword_operation: KeywordPlanAdGroupKeywordOperation
    keyword_plan_campaign_keyword_operation: KeywordPlanCampaignKeywordOperation
    keyword_plan_campaign_operation: KeywordPlanCampaignOperation
    keyword_plan_operation: KeywordPlanOperation
    label_operation: LabelOperation
    media_file_operation: MediaFileOperation
    remarketing_action_operation: RemarketingActionOperation
    shared_criterion_operation: SharedCriterionOperation
    shared_set_operation: SharedSetOperation
    smart_campaign_setting_operation: SmartCampaignSettingOperation
    user_list_operation: UserListOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_group_ad_label_operation: AdGroupAdLabelOperation = ...,
        ad_group_ad_operation: AdGroupAdOperation = ...,
        ad_group_asset_operation: AdGroupAssetOperation = ...,
        ad_group_bid_modifier_operation: AdGroupBidModifierOperation = ...,
        ad_group_criterion_customizer_operation: AdGroupCriterionCustomizerOperation = ...,
        ad_group_criterion_label_operation: AdGroupCriterionLabelOperation = ...,
        ad_group_criterion_operation: AdGroupCriterionOperation = ...,
        ad_group_customizer_operation: AdGroupCustomizerOperation = ...,
        ad_group_extension_setting_operation: AdGroupExtensionSettingOperation = ...,
        ad_group_feed_operation: AdGroupFeedOperation = ...,
        ad_group_label_operation: AdGroupLabelOperation = ...,
        ad_group_operation: AdGroupOperation = ...,
        ad_operation: AdOperation = ...,
        ad_parameter_operation: AdParameterOperation = ...,
        asset_operation: AssetOperation = ...,
        asset_group_asset_operation: AssetGroupAssetOperation = ...,
        asset_group_listing_group_filter_operation: AssetGroupListingGroupFilterOperation = ...,
        asset_group_signal_operation: AssetGroupSignalOperation = ...,
        asset_group_operation: AssetGroupOperation = ...,
        asset_set_asset_operation: AssetSetAssetOperation = ...,
        asset_set_operation: AssetSetOperation = ...,
        audience_operation: AudienceOperation = ...,
        bidding_data_exclusion_operation: BiddingDataExclusionOperation = ...,
        bidding_seasonality_adjustment_operation: BiddingSeasonalityAdjustmentOperation = ...,
        bidding_strategy_operation: BiddingStrategyOperation = ...,
        campaign_asset_operation: CampaignAssetOperation = ...,
        campaign_asset_set_operation: CampaignAssetSetOperation = ...,
        campaign_bid_modifier_operation: CampaignBidModifierOperation = ...,
        campaign_budget_operation: CampaignBudgetOperation = ...,
        campaign_conversion_goal_operation: CampaignConversionGoalOperation = ...,
        campaign_criterion_operation: CampaignCriterionOperation = ...,
        campaign_customizer_operation: CampaignCustomizerOperation = ...,
        campaign_draft_operation: CampaignDraftOperation = ...,
        campaign_extension_setting_operation: CampaignExtensionSettingOperation = ...,
        campaign_feed_operation: CampaignFeedOperation = ...,
        campaign_group_operation: CampaignGroupOperation = ...,
        campaign_label_operation: CampaignLabelOperation = ...,
        campaign_operation: CampaignOperation = ...,
        campaign_shared_set_operation: CampaignSharedSetOperation = ...,
        conversion_action_operation: ConversionActionOperation = ...,
        conversion_custom_variable_operation: ConversionCustomVariableOperation = ...,
        conversion_goal_campaign_config_operation: ConversionGoalCampaignConfigOperation = ...,
        conversion_value_rule_operation: ConversionValueRuleOperation = ...,
        conversion_value_rule_set_operation: ConversionValueRuleSetOperation = ...,
        custom_conversion_goal_operation: CustomConversionGoalOperation = ...,
        customer_asset_operation: CustomerAssetOperation = ...,
        customer_conversion_goal_operation: CustomerConversionGoalOperation = ...,
        customer_customizer_operation: CustomerCustomizerOperation = ...,
        customer_extension_setting_operation: CustomerExtensionSettingOperation = ...,
        customer_feed_operation: CustomerFeedOperation = ...,
        customer_label_operation: CustomerLabelOperation = ...,
        customer_negative_criterion_operation: CustomerNegativeCriterionOperation = ...,
        customer_operation: CustomerOperation = ...,
        customizer_attribute_operation: CustomizerAttributeOperation = ...,
        experiment_operation: ExperimentOperation = ...,
        experiment_arm_operation: ExperimentArmOperation = ...,
        extension_feed_item_operation: ExtensionFeedItemOperation = ...,
        feed_item_operation: FeedItemOperation = ...,
        feed_item_set_operation: FeedItemSetOperation = ...,
        feed_item_set_link_operation: FeedItemSetLinkOperation = ...,
        feed_item_target_operation: FeedItemTargetOperation = ...,
        feed_mapping_operation: FeedMappingOperation = ...,
        feed_operation: FeedOperation = ...,
        keyword_plan_ad_group_operation: KeywordPlanAdGroupOperation = ...,
        keyword_plan_ad_group_keyword_operation: KeywordPlanAdGroupKeywordOperation = ...,
        keyword_plan_campaign_keyword_operation: KeywordPlanCampaignKeywordOperation = ...,
        keyword_plan_campaign_operation: KeywordPlanCampaignOperation = ...,
        keyword_plan_operation: KeywordPlanOperation = ...,
        label_operation: LabelOperation = ...,
        media_file_operation: MediaFileOperation = ...,
        remarketing_action_operation: RemarketingActionOperation = ...,
        shared_criterion_operation: SharedCriterionOperation = ...,
        shared_set_operation: SharedSetOperation = ...,
        smart_campaign_setting_operation: SmartCampaignSettingOperation = ...,
        user_list_operation: UserListOperation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "ad_group_ad_label_operation",
            "ad_group_ad_operation",
            "ad_group_asset_operation",
            "ad_group_bid_modifier_operation",
            "ad_group_criterion_customizer_operation",
            "ad_group_criterion_label_operation",
            "ad_group_criterion_operation",
            "ad_group_customizer_operation",
            "ad_group_extension_setting_operation",
            "ad_group_feed_operation",
            "ad_group_label_operation",
            "ad_group_operation",
            "ad_operation",
            "ad_parameter_operation",
            "asset_operation",
            "asset_group_asset_operation",
            "asset_group_listing_group_filter_operation",
            "asset_group_signal_operation",
            "asset_group_operation",
            "asset_set_asset_operation",
            "asset_set_operation",
            "audience_operation",
            "bidding_data_exclusion_operation",
            "bidding_seasonality_adjustment_operation",
            "bidding_strategy_operation",
            "campaign_asset_operation",
            "campaign_asset_set_operation",
            "campaign_bid_modifier_operation",
            "campaign_budget_operation",
            "campaign_conversion_goal_operation",
            "campaign_criterion_operation",
            "campaign_customizer_operation",
            "campaign_draft_operation",
            "campaign_extension_setting_operation",
            "campaign_feed_operation",
            "campaign_group_operation",
            "campaign_label_operation",
            "campaign_operation",
            "campaign_shared_set_operation",
            "conversion_action_operation",
            "conversion_custom_variable_operation",
            "conversion_goal_campaign_config_operation",
            "conversion_value_rule_operation",
            "conversion_value_rule_set_operation",
            "custom_conversion_goal_operation",
            "customer_asset_operation",
            "customer_conversion_goal_operation",
            "customer_customizer_operation",
            "customer_extension_setting_operation",
            "customer_feed_operation",
            "customer_label_operation",
            "customer_negative_criterion_operation",
            "customer_operation",
            "customizer_attribute_operation",
            "experiment_operation",
            "experiment_arm_operation",
            "extension_feed_item_operation",
            "feed_item_operation",
            "feed_item_set_operation",
            "feed_item_set_link_operation",
            "feed_item_target_operation",
            "feed_mapping_operation",
            "feed_operation",
            "keyword_plan_ad_group_operation",
            "keyword_plan_ad_group_keyword_operation",
            "keyword_plan_campaign_keyword_operation",
            "keyword_plan_campaign_operation",
            "keyword_plan_operation",
            "label_operation",
            "media_file_operation",
            "remarketing_action_operation",
            "shared_criterion_operation",
            "shared_set_operation",
            "smart_campaign_setting_operation",
            "user_list_operation",
        ],
    ) -> bool: ...

class MutateOperationResponse(proto.Message):
    ad_group_ad_label_result: MutateAdGroupAdLabelResult
    ad_group_ad_result: MutateAdGroupAdResult
    ad_group_asset_result: MutateAdGroupAssetResult
    ad_group_bid_modifier_result: MutateAdGroupBidModifierResult
    ad_group_criterion_customizer_result: MutateAdGroupCriterionCustomizerResult
    ad_group_criterion_label_result: MutateAdGroupCriterionLabelResult
    ad_group_criterion_result: MutateAdGroupCriterionResult
    ad_group_customizer_result: MutateAdGroupCustomizerResult
    ad_group_extension_setting_result: MutateAdGroupExtensionSettingResult
    ad_group_feed_result: MutateAdGroupFeedResult
    ad_group_label_result: MutateAdGroupLabelResult
    ad_group_result: MutateAdGroupResult
    ad_parameter_result: MutateAdParameterResult
    ad_result: MutateAdResult
    asset_result: MutateAssetResult
    asset_group_asset_result: MutateAssetGroupAssetResult
    asset_group_listing_group_filter_result: MutateAssetGroupListingGroupFilterResult
    asset_group_signal_result: MutateAssetGroupSignalResult
    asset_group_result: MutateAssetGroupResult
    asset_set_asset_result: MutateAssetSetAssetResult
    asset_set_result: MutateAssetSetResult
    audience_result: MutateAudienceResult
    bidding_data_exclusion_result: MutateBiddingDataExclusionsResult
    bidding_seasonality_adjustment_result: MutateBiddingSeasonalityAdjustmentsResult
    bidding_strategy_result: MutateBiddingStrategyResult
    campaign_asset_result: MutateCampaignAssetResult
    campaign_asset_set_result: MutateCampaignAssetSetResult
    campaign_bid_modifier_result: MutateCampaignBidModifierResult
    campaign_budget_result: MutateCampaignBudgetResult
    campaign_conversion_goal_result: MutateCampaignConversionGoalResult
    campaign_criterion_result: MutateCampaignCriterionResult
    campaign_customizer_result: MutateCampaignCustomizerResult
    campaign_draft_result: MutateCampaignDraftResult
    campaign_extension_setting_result: MutateCampaignExtensionSettingResult
    campaign_feed_result: MutateCampaignFeedResult
    campaign_group_result: MutateCampaignGroupResult
    campaign_label_result: MutateCampaignLabelResult
    campaign_result: MutateCampaignResult
    campaign_shared_set_result: MutateCampaignSharedSetResult
    conversion_action_result: MutateConversionActionResult
    conversion_custom_variable_result: MutateConversionCustomVariableResult
    conversion_goal_campaign_config_result: MutateConversionGoalCampaignConfigResult
    conversion_value_rule_result: MutateConversionValueRuleResult
    conversion_value_rule_set_result: MutateConversionValueRuleSetResult
    custom_conversion_goal_result: MutateCustomConversionGoalResult
    customer_asset_result: MutateCustomerAssetResult
    customer_conversion_goal_result: MutateCustomerConversionGoalResult
    customer_customizer_result: MutateCustomerCustomizerResult
    customer_extension_setting_result: MutateCustomerExtensionSettingResult
    customer_feed_result: MutateCustomerFeedResult
    customer_label_result: MutateCustomerLabelResult
    customer_negative_criterion_result: MutateCustomerNegativeCriteriaResult
    customer_result: MutateCustomerResult
    customizer_attribute_result: MutateCustomizerAttributeResult
    experiment_result: MutateExperimentResult
    experiment_arm_result: MutateExperimentArmResult
    extension_feed_item_result: MutateExtensionFeedItemResult
    feed_item_result: MutateFeedItemResult
    feed_item_set_result: MutateFeedItemSetResult
    feed_item_set_link_result: MutateFeedItemSetLinkResult
    feed_item_target_result: MutateFeedItemTargetResult
    feed_mapping_result: MutateFeedMappingResult
    feed_result: MutateFeedResult
    keyword_plan_ad_group_result: MutateKeywordPlanAdGroupResult
    keyword_plan_campaign_result: MutateKeywordPlanCampaignResult
    keyword_plan_ad_group_keyword_result: MutateKeywordPlanAdGroupKeywordResult
    keyword_plan_campaign_keyword_result: MutateKeywordPlanCampaignKeywordResult
    keyword_plan_result: MutateKeywordPlansResult
    label_result: MutateLabelResult
    media_file_result: MutateMediaFileResult
    remarketing_action_result: MutateRemarketingActionResult
    shared_criterion_result: MutateSharedCriterionResult
    shared_set_result: MutateSharedSetResult
    smart_campaign_setting_result: MutateSmartCampaignSettingResult
    user_list_result: MutateUserListResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_group_ad_label_result: MutateAdGroupAdLabelResult = ...,
        ad_group_ad_result: MutateAdGroupAdResult = ...,
        ad_group_asset_result: MutateAdGroupAssetResult = ...,
        ad_group_bid_modifier_result: MutateAdGroupBidModifierResult = ...,
        ad_group_criterion_customizer_result: MutateAdGroupCriterionCustomizerResult = ...,
        ad_group_criterion_label_result: MutateAdGroupCriterionLabelResult = ...,
        ad_group_criterion_result: MutateAdGroupCriterionResult = ...,
        ad_group_customizer_result: MutateAdGroupCustomizerResult = ...,
        ad_group_extension_setting_result: MutateAdGroupExtensionSettingResult = ...,
        ad_group_feed_result: MutateAdGroupFeedResult = ...,
        ad_group_label_result: MutateAdGroupLabelResult = ...,
        ad_group_result: MutateAdGroupResult = ...,
        ad_parameter_result: MutateAdParameterResult = ...,
        ad_result: MutateAdResult = ...,
        asset_result: MutateAssetResult = ...,
        asset_group_asset_result: MutateAssetGroupAssetResult = ...,
        asset_group_listing_group_filter_result: MutateAssetGroupListingGroupFilterResult = ...,
        asset_group_signal_result: MutateAssetGroupSignalResult = ...,
        asset_group_result: MutateAssetGroupResult = ...,
        asset_set_asset_result: MutateAssetSetAssetResult = ...,
        asset_set_result: MutateAssetSetResult = ...,
        audience_result: MutateAudienceResult = ...,
        bidding_data_exclusion_result: MutateBiddingDataExclusionsResult = ...,
        bidding_seasonality_adjustment_result: MutateBiddingSeasonalityAdjustmentsResult = ...,
        bidding_strategy_result: MutateBiddingStrategyResult = ...,
        campaign_asset_result: MutateCampaignAssetResult = ...,
        campaign_asset_set_result: MutateCampaignAssetSetResult = ...,
        campaign_bid_modifier_result: MutateCampaignBidModifierResult = ...,
        campaign_budget_result: MutateCampaignBudgetResult = ...,
        campaign_conversion_goal_result: MutateCampaignConversionGoalResult = ...,
        campaign_criterion_result: MutateCampaignCriterionResult = ...,
        campaign_customizer_result: MutateCampaignCustomizerResult = ...,
        campaign_draft_result: MutateCampaignDraftResult = ...,
        campaign_extension_setting_result: MutateCampaignExtensionSettingResult = ...,
        campaign_feed_result: MutateCampaignFeedResult = ...,
        campaign_group_result: MutateCampaignGroupResult = ...,
        campaign_label_result: MutateCampaignLabelResult = ...,
        campaign_result: MutateCampaignResult = ...,
        campaign_shared_set_result: MutateCampaignSharedSetResult = ...,
        conversion_action_result: MutateConversionActionResult = ...,
        conversion_custom_variable_result: MutateConversionCustomVariableResult = ...,
        conversion_goal_campaign_config_result: MutateConversionGoalCampaignConfigResult = ...,
        conversion_value_rule_result: MutateConversionValueRuleResult = ...,
        conversion_value_rule_set_result: MutateConversionValueRuleSetResult = ...,
        custom_conversion_goal_result: MutateCustomConversionGoalResult = ...,
        customer_asset_result: MutateCustomerAssetResult = ...,
        customer_conversion_goal_result: MutateCustomerConversionGoalResult = ...,
        customer_customizer_result: MutateCustomerCustomizerResult = ...,
        customer_extension_setting_result: MutateCustomerExtensionSettingResult = ...,
        customer_feed_result: MutateCustomerFeedResult = ...,
        customer_label_result: MutateCustomerLabelResult = ...,
        customer_negative_criterion_result: MutateCustomerNegativeCriteriaResult = ...,
        customer_result: MutateCustomerResult = ...,
        customizer_attribute_result: MutateCustomizerAttributeResult = ...,
        experiment_result: MutateExperimentResult = ...,
        experiment_arm_result: MutateExperimentArmResult = ...,
        extension_feed_item_result: MutateExtensionFeedItemResult = ...,
        feed_item_result: MutateFeedItemResult = ...,
        feed_item_set_result: MutateFeedItemSetResult = ...,
        feed_item_set_link_result: MutateFeedItemSetLinkResult = ...,
        feed_item_target_result: MutateFeedItemTargetResult = ...,
        feed_mapping_result: MutateFeedMappingResult = ...,
        feed_result: MutateFeedResult = ...,
        keyword_plan_ad_group_result: MutateKeywordPlanAdGroupResult = ...,
        keyword_plan_campaign_result: MutateKeywordPlanCampaignResult = ...,
        keyword_plan_ad_group_keyword_result: MutateKeywordPlanAdGroupKeywordResult = ...,
        keyword_plan_campaign_keyword_result: MutateKeywordPlanCampaignKeywordResult = ...,
        keyword_plan_result: MutateKeywordPlansResult = ...,
        label_result: MutateLabelResult = ...,
        media_file_result: MutateMediaFileResult = ...,
        remarketing_action_result: MutateRemarketingActionResult = ...,
        shared_criterion_result: MutateSharedCriterionResult = ...,
        shared_set_result: MutateSharedSetResult = ...,
        smart_campaign_setting_result: MutateSmartCampaignSettingResult = ...,
        user_list_result: MutateUserListResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "ad_group_ad_label_result",
            "ad_group_ad_result",
            "ad_group_asset_result",
            "ad_group_bid_modifier_result",
            "ad_group_criterion_customizer_result",
            "ad_group_criterion_label_result",
            "ad_group_criterion_result",
            "ad_group_customizer_result",
            "ad_group_extension_setting_result",
            "ad_group_feed_result",
            "ad_group_label_result",
            "ad_group_result",
            "ad_parameter_result",
            "ad_result",
            "asset_result",
            "asset_group_asset_result",
            "asset_group_listing_group_filter_result",
            "asset_group_signal_result",
            "asset_group_result",
            "asset_set_asset_result",
            "asset_set_result",
            "audience_result",
            "bidding_data_exclusion_result",
            "bidding_seasonality_adjustment_result",
            "bidding_strategy_result",
            "campaign_asset_result",
            "campaign_asset_set_result",
            "campaign_bid_modifier_result",
            "campaign_budget_result",
            "campaign_conversion_goal_result",
            "campaign_criterion_result",
            "campaign_customizer_result",
            "campaign_draft_result",
            "campaign_extension_setting_result",
            "campaign_feed_result",
            "campaign_group_result",
            "campaign_label_result",
            "campaign_result",
            "campaign_shared_set_result",
            "conversion_action_result",
            "conversion_custom_variable_result",
            "conversion_goal_campaign_config_result",
            "conversion_value_rule_result",
            "conversion_value_rule_set_result",
            "custom_conversion_goal_result",
            "customer_asset_result",
            "customer_conversion_goal_result",
            "customer_customizer_result",
            "customer_extension_setting_result",
            "customer_feed_result",
            "customer_label_result",
            "customer_negative_criterion_result",
            "customer_result",
            "customizer_attribute_result",
            "experiment_result",
            "experiment_arm_result",
            "extension_feed_item_result",
            "feed_item_result",
            "feed_item_set_result",
            "feed_item_set_link_result",
            "feed_item_target_result",
            "feed_mapping_result",
            "feed_result",
            "keyword_plan_ad_group_result",
            "keyword_plan_campaign_result",
            "keyword_plan_ad_group_keyword_result",
            "keyword_plan_campaign_keyword_result",
            "keyword_plan_result",
            "label_result",
            "media_file_result",
            "remarketing_action_result",
            "shared_criterion_result",
            "shared_set_result",
            "smart_campaign_setting_result",
            "user_list_result",
        ],
    ) -> bool: ...

class SearchGoogleAdsRequest(proto.Message):
    customer_id: str
    query: str
    page_token: str
    page_size: int
    validate_only: bool
    return_total_results_count: bool
    summary_row_setting: SummaryRowSettingEnum.SummaryRowSetting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        query: str = ...,
        page_token: str = ...,
        page_size: int = ...,
        validate_only: bool = ...,
        return_total_results_count: bool = ...,
        summary_row_setting: SummaryRowSettingEnum.SummaryRowSetting = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "query",
            "page_token",
            "page_size",
            "validate_only",
            "return_total_results_count",
            "summary_row_setting",
        ],
    ) -> bool: ...

class SearchGoogleAdsResponse(proto.Message):
    results: MutableSequence[GoogleAdsRow]
    next_page_token: str
    total_results_count: int
    field_mask: FieldMask
    summary_row: GoogleAdsRow
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[GoogleAdsRow] = ...,
        next_page_token: str = ...,
        total_results_count: int = ...,
        field_mask: FieldMask = ...,
        summary_row: GoogleAdsRow = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "results",
            "next_page_token",
            "total_results_count",
            "field_mask",
            "summary_row",
        ],
    ) -> bool: ...

class SearchGoogleAdsStreamRequest(proto.Message):
    customer_id: str
    query: str
    summary_row_setting: SummaryRowSettingEnum.SummaryRowSetting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        query: str = ...,
        summary_row_setting: SummaryRowSettingEnum.SummaryRowSetting = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "query", "summary_row_setting"]
    ) -> bool: ...

class SearchGoogleAdsStreamResponse(proto.Message):
    results: MutableSequence[GoogleAdsRow]
    field_mask: FieldMask
    summary_row: GoogleAdsRow
    request_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[GoogleAdsRow] = ...,
        field_mask: FieldMask = ...,
        summary_row: GoogleAdsRow = ...,
        request_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results", "field_mask", "summary_row", "request_id"]
    ) -> bool: ...
