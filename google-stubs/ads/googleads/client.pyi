import types
from typing import Any, overload

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

import google.ads.googleads.v21.services.services.account_budget_proposal_service
import google.ads.googleads.v21.services.services.account_link_service
import google.ads.googleads.v21.services.services.ad_group_ad_label_service
import google.ads.googleads.v21.services.services.ad_group_ad_service
import google.ads.googleads.v21.services.services.ad_group_asset_service
import google.ads.googleads.v21.services.services.ad_group_asset_set_service
import google.ads.googleads.v21.services.services.ad_group_bid_modifier_service
import google.ads.googleads.v21.services.services.ad_group_criterion_customizer_service
import google.ads.googleads.v21.services.services.ad_group_criterion_label_service
import google.ads.googleads.v21.services.services.ad_group_criterion_service
import google.ads.googleads.v21.services.services.ad_group_customizer_service
import google.ads.googleads.v21.services.services.ad_group_extension_setting_service
import google.ads.googleads.v21.services.services.ad_group_feed_service
import google.ads.googleads.v21.services.services.ad_group_label_service
import google.ads.googleads.v21.services.services.ad_group_service
import google.ads.googleads.v21.services.services.ad_parameter_service
import google.ads.googleads.v21.services.services.ad_service
import google.ads.googleads.v21.services.services.asset_group_asset_service
import google.ads.googleads.v21.services.services.asset_group_listing_group_filter_service
import google.ads.googleads.v21.services.services.asset_group_service
import google.ads.googleads.v21.services.services.asset_group_signal_service
import google.ads.googleads.v21.services.services.asset_service
import google.ads.googleads.v21.services.services.asset_set_asset_service
import google.ads.googleads.v21.services.services.asset_set_service
import google.ads.googleads.v21.services.services.audience_insights_service
import google.ads.googleads.v21.services.services.audience_service
import google.ads.googleads.v21.services.services.batch_job_service
import google.ads.googleads.v21.services.services.bidding_data_exclusion_service
import google.ads.googleads.v21.services.services.bidding_seasonality_adjustment_service
import google.ads.googleads.v21.services.services.bidding_strategy_service
import google.ads.googleads.v21.services.services.billing_setup_service
import google.ads.googleads.v21.services.services.brand_suggestion_service
import google.ads.googleads.v21.services.services.campaign_asset_service
import google.ads.googleads.v21.services.services.campaign_asset_set_service
import google.ads.googleads.v21.services.services.campaign_bid_modifier_service
import google.ads.googleads.v21.services.services.campaign_budget_service
import google.ads.googleads.v21.services.services.campaign_conversion_goal_service
import google.ads.googleads.v21.services.services.campaign_criterion_service
import google.ads.googleads.v21.services.services.campaign_customizer_service
import google.ads.googleads.v21.services.services.campaign_draft_service
import google.ads.googleads.v21.services.services.campaign_extension_setting_service
import google.ads.googleads.v21.services.services.campaign_feed_service
import google.ads.googleads.v21.services.services.campaign_group_service
import google.ads.googleads.v21.services.services.campaign_label_service
import google.ads.googleads.v21.services.services.campaign_lifecycle_goal_service
import google.ads.googleads.v21.services.services.campaign_service
import google.ads.googleads.v21.services.services.campaign_shared_set_service
import google.ads.googleads.v21.services.services.content_creator_insights_service
import google.ads.googleads.v21.services.services.conversion_action_service
import google.ads.googleads.v21.services.services.conversion_adjustment_upload_service
import google.ads.googleads.v21.services.services.conversion_custom_variable_service
import google.ads.googleads.v21.services.services.conversion_goal_campaign_config_service
import google.ads.googleads.v21.services.services.conversion_upload_service
import google.ads.googleads.v21.services.services.conversion_value_rule_service
import google.ads.googleads.v21.services.services.conversion_value_rule_set_service
import google.ads.googleads.v21.services.services.custom_audience_service
import google.ads.googleads.v21.services.services.custom_conversion_goal_service
import google.ads.googleads.v21.services.services.custom_interest_service
import google.ads.googleads.v21.services.services.customer_asset_service
import google.ads.googleads.v21.services.services.customer_asset_set_service
import google.ads.googleads.v21.services.services.customer_client_link_service
import google.ads.googleads.v21.services.services.customer_conversion_goal_service
import google.ads.googleads.v21.services.services.customer_customizer_service
import google.ads.googleads.v21.services.services.customer_extension_setting_service
import google.ads.googleads.v21.services.services.customer_feed_service
import google.ads.googleads.v21.services.services.customer_label_service
import google.ads.googleads.v21.services.services.customer_lifecycle_goal_service
import google.ads.googleads.v21.services.services.customer_manager_link_service
import google.ads.googleads.v21.services.services.customer_negative_criterion_service
import google.ads.googleads.v21.services.services.customer_service
import google.ads.googleads.v21.services.services.customer_sk_ad_network_conversion_value_schema_service
import google.ads.googleads.v21.services.services.customer_user_access_invitation_service
import google.ads.googleads.v21.services.services.customer_user_access_service
import google.ads.googleads.v21.services.services.customizer_attribute_service
import google.ads.googleads.v21.services.services.data_link_service
import google.ads.googleads.v21.services.services.experiment_arm_service
import google.ads.googleads.v21.services.services.experiment_service
import google.ads.googleads.v21.services.services.extension_feed_item_service
import google.ads.googleads.v21.services.services.feed_item_service
import google.ads.googleads.v21.services.services.feed_item_set_link_service
import google.ads.googleads.v21.services.services.feed_item_set_service
import google.ads.googleads.v21.services.services.feed_item_target_service
import google.ads.googleads.v21.services.services.feed_mapping_service
import google.ads.googleads.v21.services.services.feed_service

# Autogenerated service imports
import google.ads.googleads.v18.services.services.geo_target_constant_service
import google.ads.googleads.v18.services.services.google_ads_field_service
import google.ads.googleads.v18.services.services.google_ads_service
import google.ads.googleads.v18.services.services.identity_verification_service
import google.ads.googleads.v18.services.services.invoice_service
import google.ads.googleads.v18.services.services.keyword_plan_ad_group_keyword_service
import google.ads.googleads.v18.services.services.keyword_plan_ad_group_service
import google.ads.googleads.v18.services.services.keyword_plan_campaign_keyword_service
import google.ads.googleads.v18.services.services.keyword_plan_campaign_service
import google.ads.googleads.v18.services.services.keyword_plan_idea_service
import google.ads.googleads.v18.services.services.keyword_plan_service
import google.ads.googleads.v18.services.services.keyword_theme_constant_service
import google.ads.googleads.v18.services.services.label_service
import google.ads.googleads.v18.services.services.local_services_lead_service
import google.ads.googleads.v18.services.services.offline_user_data_job_service
import google.ads.googleads.v18.services.services.payments_account_service
import google.ads.googleads.v18.services.services.product_link_invitation_service
import google.ads.googleads.v18.services.services.product_link_service
import google.ads.googleads.v18.services.services.reach_plan_service
import google.ads.googleads.v18.services.services.recommendation_service
import google.ads.googleads.v18.services.services.recommendation_subscription_service
import google.ads.googleads.v18.services.services.remarketing_action_service
import google.ads.googleads.v18.services.services.shareable_preview_service
import google.ads.googleads.v18.services.services.shared_criterion_service
import google.ads.googleads.v18.services.services.shared_set_service
import google.ads.googleads.v18.services.services.smart_campaign_setting_service
import google.ads.googleads.v18.services.services.smart_campaign_suggest_service
import google.ads.googleads.v18.services.services.third_party_app_analytics_link_service
import google.ads.googleads.v18.services.services.travel_asset_suggestion_service
import google.ads.googleads.v18.services.services.user_data_service
import google.ads.googleads.v18.services.services.user_list_customer_type_service
import google.ads.googleads.v18.services.services.user_list_service
import google.ads.googleads.v19.services.services.account_budget_proposal_service
import google.ads.googleads.v19.services.services.account_link_service
import google.ads.googleads.v19.services.services.ad_group_ad_label_service
import google.ads.googleads.v19.services.services.ad_group_ad_service
import google.ads.googleads.v19.services.services.ad_group_asset_service
import google.ads.googleads.v19.services.services.ad_group_asset_set_service
import google.ads.googleads.v19.services.services.ad_group_bid_modifier_service
import google.ads.googleads.v19.services.services.ad_group_criterion_customizer_service
import google.ads.googleads.v19.services.services.ad_group_criterion_label_service
import google.ads.googleads.v19.services.services.ad_group_criterion_service
import google.ads.googleads.v19.services.services.ad_group_customizer_service
import google.ads.googleads.v19.services.services.ad_group_label_service
import google.ads.googleads.v19.services.services.ad_group_service
import google.ads.googleads.v19.services.services.ad_parameter_service
import google.ads.googleads.v19.services.services.ad_service
import google.ads.googleads.v19.services.services.asset_group_asset_service
import google.ads.googleads.v19.services.services.asset_group_listing_group_filter_service
import google.ads.googleads.v19.services.services.asset_group_service
import google.ads.googleads.v19.services.services.asset_group_signal_service
import google.ads.googleads.v19.services.services.asset_service
import google.ads.googleads.v19.services.services.asset_set_asset_service
import google.ads.googleads.v19.services.services.asset_set_service
import google.ads.googleads.v19.services.services.audience_insights_service
import google.ads.googleads.v19.services.services.audience_service
import google.ads.googleads.v19.services.services.batch_job_service
import google.ads.googleads.v19.services.services.bidding_data_exclusion_service
import google.ads.googleads.v19.services.services.bidding_seasonality_adjustment_service
import google.ads.googleads.v19.services.services.bidding_strategy_service
import google.ads.googleads.v19.services.services.billing_setup_service
import google.ads.googleads.v19.services.services.brand_suggestion_service
import google.ads.googleads.v19.services.services.campaign_asset_service
import google.ads.googleads.v19.services.services.campaign_asset_set_service
import google.ads.googleads.v19.services.services.campaign_bid_modifier_service
import google.ads.googleads.v19.services.services.campaign_budget_service
import google.ads.googleads.v19.services.services.campaign_conversion_goal_service
import google.ads.googleads.v19.services.services.campaign_criterion_service
import google.ads.googleads.v19.services.services.campaign_customizer_service
import google.ads.googleads.v19.services.services.campaign_draft_service
import google.ads.googleads.v19.services.services.campaign_group_service
import google.ads.googleads.v19.services.services.campaign_label_service
import google.ads.googleads.v19.services.services.campaign_lifecycle_goal_service
import google.ads.googleads.v19.services.services.campaign_service
import google.ads.googleads.v19.services.services.campaign_shared_set_service
import google.ads.googleads.v19.services.services.content_creator_insights_service
import google.ads.googleads.v19.services.services.conversion_action_service
import google.ads.googleads.v19.services.services.conversion_adjustment_upload_service
import google.ads.googleads.v19.services.services.conversion_custom_variable_service
import google.ads.googleads.v19.services.services.conversion_goal_campaign_config_service
import google.ads.googleads.v19.services.services.conversion_upload_service
import google.ads.googleads.v19.services.services.conversion_value_rule_service
import google.ads.googleads.v19.services.services.conversion_value_rule_set_service
import google.ads.googleads.v19.services.services.custom_audience_service
import google.ads.googleads.v19.services.services.custom_conversion_goal_service
import google.ads.googleads.v19.services.services.custom_interest_service
import google.ads.googleads.v19.services.services.customer_asset_service
import google.ads.googleads.v19.services.services.customer_asset_set_service
import google.ads.googleads.v19.services.services.customer_client_link_service
import google.ads.googleads.v19.services.services.customer_conversion_goal_service
import google.ads.googleads.v19.services.services.customer_customizer_service
import google.ads.googleads.v19.services.services.customer_label_service
import google.ads.googleads.v19.services.services.customer_lifecycle_goal_service
import google.ads.googleads.v19.services.services.customer_manager_link_service
import google.ads.googleads.v19.services.services.customer_negative_criterion_service
import google.ads.googleads.v19.services.services.customer_service
import google.ads.googleads.v19.services.services.customer_sk_ad_network_conversion_value_schema_service
import google.ads.googleads.v19.services.services.customer_user_access_invitation_service
import google.ads.googleads.v19.services.services.customer_user_access_service
import google.ads.googleads.v19.services.services.customizer_attribute_service
import google.ads.googleads.v19.services.services.data_link_service
import google.ads.googleads.v19.services.services.experiment_arm_service
import google.ads.googleads.v19.services.services.experiment_service
import google.ads.googleads.v19.services.services.geo_target_constant_service
import google.ads.googleads.v19.services.services.google_ads_field_service
import google.ads.googleads.v19.services.services.google_ads_service
import google.ads.googleads.v19.services.services.identity_verification_service
import google.ads.googleads.v19.services.services.invoice_service
import google.ads.googleads.v19.services.services.keyword_plan_ad_group_keyword_service
import google.ads.googleads.v19.services.services.keyword_plan_ad_group_service
import google.ads.googleads.v19.services.services.keyword_plan_campaign_keyword_service
import google.ads.googleads.v19.services.services.keyword_plan_campaign_service
import google.ads.googleads.v19.services.services.keyword_plan_idea_service
import google.ads.googleads.v19.services.services.keyword_plan_service
import google.ads.googleads.v19.services.services.keyword_theme_constant_service
import google.ads.googleads.v19.services.services.label_service
import google.ads.googleads.v19.services.services.local_services_lead_service
import google.ads.googleads.v19.services.services.offline_user_data_job_service
import google.ads.googleads.v19.services.services.payments_account_service
import google.ads.googleads.v19.services.services.product_link_invitation_service
import google.ads.googleads.v19.services.services.product_link_service
import google.ads.googleads.v19.services.services.reach_plan_service
import google.ads.googleads.v19.services.services.recommendation_service
import google.ads.googleads.v19.services.services.recommendation_subscription_service
import google.ads.googleads.v19.services.services.remarketing_action_service
import google.ads.googleads.v19.services.services.shareable_preview_service
import google.ads.googleads.v19.services.services.shared_criterion_service
import google.ads.googleads.v19.services.services.shared_set_service
import google.ads.googleads.v19.services.services.smart_campaign_setting_service
import google.ads.googleads.v19.services.services.smart_campaign_suggest_service
import google.ads.googleads.v19.services.services.third_party_app_analytics_link_service
import google.ads.googleads.v19.services.services.travel_asset_suggestion_service
import google.ads.googleads.v19.services.services.user_data_service
import google.ads.googleads.v19.services.services.user_list_customer_type_service
import google.ads.googleads.v19.services.services.user_list_service
import google.ads.googleads.v20.services.services.account_budget_proposal_service
import google.ads.googleads.v20.services.services.account_link_service
import google.ads.googleads.v20.services.services.ad_group_ad_label_service
import google.ads.googleads.v20.services.services.ad_group_ad_service
import google.ads.googleads.v20.services.services.ad_group_asset_service
import google.ads.googleads.v20.services.services.ad_group_asset_set_service
import google.ads.googleads.v20.services.services.ad_group_bid_modifier_service
import google.ads.googleads.v20.services.services.ad_group_criterion_customizer_service
import google.ads.googleads.v20.services.services.ad_group_criterion_label_service
import google.ads.googleads.v20.services.services.ad_group_criterion_service
import google.ads.googleads.v20.services.services.ad_group_customizer_service
import google.ads.googleads.v20.services.services.ad_group_label_service
import google.ads.googleads.v20.services.services.ad_group_service
import google.ads.googleads.v20.services.services.ad_parameter_service
import google.ads.googleads.v20.services.services.ad_service
import google.ads.googleads.v20.services.services.asset_group_asset_service
import google.ads.googleads.v20.services.services.asset_group_listing_group_filter_service
import google.ads.googleads.v20.services.services.asset_group_service
import google.ads.googleads.v20.services.services.asset_group_signal_service
import google.ads.googleads.v20.services.services.asset_service
import google.ads.googleads.v20.services.services.asset_set_asset_service
import google.ads.googleads.v20.services.services.asset_set_service
import google.ads.googleads.v20.services.services.audience_insights_service
import google.ads.googleads.v20.services.services.audience_service
import google.ads.googleads.v20.services.services.batch_job_service
import google.ads.googleads.v20.services.services.bidding_data_exclusion_service
import google.ads.googleads.v20.services.services.bidding_seasonality_adjustment_service
import google.ads.googleads.v20.services.services.bidding_strategy_service
import google.ads.googleads.v20.services.services.billing_setup_service
import google.ads.googleads.v20.services.services.brand_suggestion_service
import google.ads.googleads.v20.services.services.campaign_asset_service
import google.ads.googleads.v20.services.services.campaign_asset_set_service
import google.ads.googleads.v20.services.services.campaign_bid_modifier_service
import google.ads.googleads.v20.services.services.campaign_budget_service
import google.ads.googleads.v20.services.services.campaign_conversion_goal_service
import google.ads.googleads.v20.services.services.campaign_criterion_service
import google.ads.googleads.v20.services.services.campaign_customizer_service
import google.ads.googleads.v20.services.services.campaign_draft_service
import google.ads.googleads.v20.services.services.campaign_group_service
import google.ads.googleads.v20.services.services.campaign_label_service
import google.ads.googleads.v20.services.services.campaign_lifecycle_goal_service
import google.ads.googleads.v20.services.services.campaign_service
import google.ads.googleads.v20.services.services.campaign_shared_set_service
import google.ads.googleads.v20.services.services.content_creator_insights_service
import google.ads.googleads.v20.services.services.conversion_action_service
import google.ads.googleads.v20.services.services.conversion_adjustment_upload_service
import google.ads.googleads.v20.services.services.conversion_custom_variable_service
import google.ads.googleads.v20.services.services.conversion_goal_campaign_config_service
import google.ads.googleads.v20.services.services.conversion_upload_service
import google.ads.googleads.v20.services.services.conversion_value_rule_service
import google.ads.googleads.v20.services.services.conversion_value_rule_set_service
import google.ads.googleads.v20.services.services.custom_audience_service
import google.ads.googleads.v20.services.services.custom_conversion_goal_service
import google.ads.googleads.v20.services.services.custom_interest_service
import google.ads.googleads.v20.services.services.customer_asset_service
import google.ads.googleads.v20.services.services.customer_asset_set_service
import google.ads.googleads.v20.services.services.customer_client_link_service
import google.ads.googleads.v20.services.services.customer_conversion_goal_service
import google.ads.googleads.v20.services.services.customer_customizer_service
import google.ads.googleads.v20.services.services.customer_label_service
import google.ads.googleads.v20.services.services.customer_lifecycle_goal_service
import google.ads.googleads.v20.services.services.customer_manager_link_service
import google.ads.googleads.v20.services.services.customer_negative_criterion_service
import google.ads.googleads.v20.services.services.customer_service
import google.ads.googleads.v20.services.services.customer_sk_ad_network_conversion_value_schema_service
import google.ads.googleads.v20.services.services.customer_user_access_invitation_service
import google.ads.googleads.v20.services.services.customer_user_access_service
import google.ads.googleads.v20.services.services.customizer_attribute_service
import google.ads.googleads.v20.services.services.data_link_service
import google.ads.googleads.v20.services.services.experiment_arm_service
import google.ads.googleads.v20.services.services.experiment_service
import google.ads.googleads.v20.services.services.geo_target_constant_service
import google.ads.googleads.v20.services.services.google_ads_field_service
import google.ads.googleads.v20.services.services.google_ads_service
import google.ads.googleads.v20.services.services.identity_verification_service
import google.ads.googleads.v20.services.services.invoice_service
import google.ads.googleads.v20.services.services.keyword_plan_ad_group_keyword_service
import google.ads.googleads.v20.services.services.keyword_plan_ad_group_service
import google.ads.googleads.v20.services.services.keyword_plan_campaign_keyword_service
import google.ads.googleads.v20.services.services.keyword_plan_campaign_service
import google.ads.googleads.v20.services.services.keyword_plan_idea_service
import google.ads.googleads.v20.services.services.keyword_plan_service
import google.ads.googleads.v20.services.services.keyword_theme_constant_service
import google.ads.googleads.v20.services.services.label_service
import google.ads.googleads.v20.services.services.local_services_lead_service
import google.ads.googleads.v20.services.services.offline_user_data_job_service
import google.ads.googleads.v20.services.services.payments_account_service
import google.ads.googleads.v20.services.services.product_link_invitation_service
import google.ads.googleads.v20.services.services.product_link_service
import google.ads.googleads.v20.services.services.reach_plan_service
import google.ads.googleads.v20.services.services.recommendation_service
import google.ads.googleads.v20.services.services.recommendation_subscription_service
import google.ads.googleads.v20.services.services.remarketing_action_service
import google.ads.googleads.v20.services.services.shareable_preview_service
import google.ads.googleads.v20.services.services.shared_criterion_service
import google.ads.googleads.v20.services.services.shared_set_service
import google.ads.googleads.v20.services.services.smart_campaign_setting_service
import google.ads.googleads.v20.services.services.smart_campaign_suggest_service
import google.ads.googleads.v20.services.services.third_party_app_analytics_link_service
import google.ads.googleads.v20.services.services.travel_asset_suggestion_service
import google.ads.googleads.v20.services.services.user_data_service
import google.ads.googleads.v20.services.services.user_list_customer_type_service
import google.ads.googleads.v20.services.services.user_list_service

# End of autogenerated service imports
from google.ads.googleads import v21
from google.ads.googleads.config import _ConfigDataUnparsed

_V19 = Literal["v19"]
_V20 = Literal["v20"]
_V21 = Literal["v21"]
_V = _V19 | _V20 | _V21

class _EnumGetter:
    # Autogenerated enums
    AccessInvitationStatusEnum: type[
        v20.enums.AccessInvitationStatusEnum.AccessInvitationStatus
    ]
    AccessReasonEnum: type[v20.enums.AccessReasonEnum.AccessReason]
    AccessRoleEnum: type[v20.enums.AccessRoleEnum.AccessRole]
    AccountBudgetProposalStatusEnum: type[
        v20.enums.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    ]
    AccountBudgetProposalTypeEnum: type[
        v20.enums.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    ]
    AccountBudgetStatusEnum: type[v20.enums.AccountBudgetStatusEnum.AccountBudgetStatus]
    AccountLinkStatusEnum: type[v20.enums.AccountLinkStatusEnum.AccountLinkStatus]
    AdDestinationTypeEnum: type[v20.enums.AdDestinationTypeEnum.AdDestinationType]
    AdFormatTypeEnum: type[v20.enums.AdFormatTypeEnum.AdFormatType]
    AdGroupAdPrimaryStatusEnum: type[
        v20.enums.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    ]
    AdGroupAdPrimaryStatusReasonEnum: type[
        v20.enums.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    ]
    AdGroupAdRotationModeEnum: type[
        v20.enums.AdGroupAdRotationModeEnum.AdGroupAdRotationMode
    ]
    AdGroupAdStatusEnum: type[v20.enums.AdGroupAdStatusEnum.AdGroupAdStatus]
    AdGroupCriterionApprovalStatusEnum: type[
        v20.enums.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    ]
    AdGroupCriterionPrimaryStatusEnum: type[
        v20.enums.AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    ]
    AdGroupCriterionPrimaryStatusReasonEnum: type[
        v20.enums.AdGroupCriterionPrimaryStatusReasonEnum.AdGroupCriterionPrimaryStatusReason
    ]
    AdGroupCriterionStatusEnum: type[
        v20.enums.AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    ]
    AdGroupPrimaryStatusEnum: type[
        v20.enums.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus
    ]
    AdGroupPrimaryStatusReasonEnum: type[
        v20.enums.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    ]
    AdGroupStatusEnum: type[v20.enums.AdGroupStatusEnum.AdGroupStatus]
    AdGroupTypeEnum: type[v20.enums.AdGroupTypeEnum.AdGroupType]
    AdNetworkTypeEnum: type[v20.enums.AdNetworkTypeEnum.AdNetworkType]
    AdServingOptimizationStatusEnum: type[
        v20.enums.AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    ]
    AdStrengthActionItemTypeEnum: type[
        v20.enums.AdStrengthActionItemTypeEnum.AdStrengthActionItemType
    ]
    AdStrengthEnum: type[v20.enums.AdStrengthEnum.AdStrength]
    AdTypeEnum: type[v20.enums.AdTypeEnum.AdType]
    AdvertisingChannelSubTypeEnum: type[
        v20.enums.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    ]
    AdvertisingChannelTypeEnum: type[
        v20.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType
    ]
    AgeRangeTypeEnum: type[v20.enums.AgeRangeTypeEnum.AgeRangeType]
    AndroidPrivacyInteractionTypeEnum: type[
        v20.enums.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    ]
    AndroidPrivacyNetworkTypeEnum: type[
        v20.enums.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    ]
    AppBiddingGoalEnum: type[v20.enums.AppBiddingGoalEnum.AppBiddingGoal]
    AppCampaignAppStoreEnum: type[v20.enums.AppCampaignAppStoreEnum.AppCampaignAppStore]
    AppCampaignBiddingStrategyGoalTypeEnum: type[
        v20.enums.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    ]
    AppPaymentModelTypeEnum: type[v20.enums.AppPaymentModelTypeEnum.AppPaymentModelType]
    AppUrlOperatingSystemTypeEnum: type[
        v20.enums.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    ]
    ApplicationInstanceEnum: type[v20.enums.ApplicationInstanceEnum.ApplicationInstance]
    AssetAutomationStatusEnum: type[
        v20.enums.AssetAutomationStatusEnum.AssetAutomationStatus
    ]
    AssetAutomationTypeEnum: type[v20.enums.AssetAutomationTypeEnum.AssetAutomationType]
    AssetCoverageVideoAspectRatioRequirementEnum: type[
        v20.enums.AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
    ]
    AssetFieldTypeEnum: type[v20.enums.AssetFieldTypeEnum.AssetFieldType]
    AssetGroupPrimaryStatusEnum: type[
        v20.enums.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    ]
    AssetGroupPrimaryStatusReasonEnum: type[
        v20.enums.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ]
    AssetGroupSignalApprovalStatusEnum: type[
        v20.enums.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    ]
    AssetGroupStatusEnum: type[v20.enums.AssetGroupStatusEnum.AssetGroupStatus]
    AssetLinkPrimaryStatusEnum: type[
        v20.enums.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    ]
    AssetLinkPrimaryStatusReasonEnum: type[
        v20.enums.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ]
    AssetLinkStatusEnum: type[v20.enums.AssetLinkStatusEnum.AssetLinkStatus]
    AssetOfflineEvaluationErrorReasonsEnum: type[
        v20.enums.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    ]
    AssetPerformanceLabelEnum: type[
        v20.enums.AssetPerformanceLabelEnum.AssetPerformanceLabel
    ]
    AssetSetAssetStatusEnum: type[v20.enums.AssetSetAssetStatusEnum.AssetSetAssetStatus]
    AssetSetLinkStatusEnum: type[v20.enums.AssetSetLinkStatusEnum.AssetSetLinkStatus]
    AssetSetStatusEnum: type[v20.enums.AssetSetStatusEnum.AssetSetStatus]
    AssetSetTypeEnum: type[v20.enums.AssetSetTypeEnum.AssetSetType]
    AssetSourceEnum: type[v20.enums.AssetSourceEnum.AssetSource]
    AssetTypeEnum: type[v20.enums.AssetTypeEnum.AssetType]
    AsyncActionStatusEnum: type[v20.enums.AsyncActionStatusEnum.AsyncActionStatus]
    AttributionModelEnum: type[v20.enums.AttributionModelEnum.AttributionModel]
    AudienceInsightsDimensionEnum: type[
        v20.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    ]
    AudienceInsightsMarketingObjectiveEnum: type[
        v20.enums.AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective
    ]
    AudienceScopeEnum: type[v20.enums.AudienceScopeEnum.AudienceScope]
    AudienceStatusEnum: type[v20.enums.AudienceStatusEnum.AudienceStatus]
    BatchJobStatusEnum: type[v20.enums.BatchJobStatusEnum.BatchJobStatus]
    BidModifierSourceEnum: type[v20.enums.BidModifierSourceEnum.BidModifierSource]
    BiddingSourceEnum: type[v20.enums.BiddingSourceEnum.BiddingSource]
    BiddingStrategyStatusEnum: type[
        v20.enums.BiddingStrategyStatusEnum.BiddingStrategyStatus
    ]
    BiddingStrategySystemStatusEnum: type[
        v20.enums.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ]
    BiddingStrategyTypeEnum: type[v20.enums.BiddingStrategyTypeEnum.BiddingStrategyType]
    BillingSetupStatusEnum: type[v20.enums.BillingSetupStatusEnum.BillingSetupStatus]
    BrandRequestRejectionReasonEnum: type[
        v20.enums.BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    ]
    BrandSafetySuitabilityEnum: type[
        v20.enums.BrandSafetySuitabilityEnum.BrandSafetySuitability
    ]
    BrandStateEnum: type[v20.enums.BrandStateEnum.BrandState]
    BudgetCampaignAssociationStatusEnum: type[
        v20.enums.BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    ]
    BudgetDeliveryMethodEnum: type[
        v20.enums.BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    ]
    BudgetPeriodEnum: type[v20.enums.BudgetPeriodEnum.BudgetPeriod]
    BudgetStatusEnum: type[v20.enums.BudgetStatusEnum.BudgetStatus]
    BudgetTypeEnum: type[v20.enums.BudgetTypeEnum.BudgetType]
    BusinessMessageCallToActionTypeEnum: type[
        v20.enums.BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    ]
    BusinessMessageProviderEnum: type[
        v20.enums.BusinessMessageProviderEnum.BusinessMessageProvider
    ]
    CallConversionReportingStateEnum: type[
        v20.enums.CallConversionReportingStateEnum.CallConversionReportingState
    ]
    CallToActionTypeEnum: type[v20.enums.CallToActionTypeEnum.CallToActionType]
    CallTrackingDisplayLocationEnum: type[
        v20.enums.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    ]
    CallTypeEnum: type[v20.enums.CallTypeEnum.CallType]
    CampaignCriterionStatusEnum: type[
        v20.enums.CampaignCriterionStatusEnum.CampaignCriterionStatus
    ]
    CampaignDraftStatusEnum: type[v20.enums.CampaignDraftStatusEnum.CampaignDraftStatus]
    CampaignExperimentTypeEnum: type[
        v20.enums.CampaignExperimentTypeEnum.CampaignExperimentType
    ]
    CampaignGroupStatusEnum: type[v20.enums.CampaignGroupStatusEnum.CampaignGroupStatus]
    CampaignKeywordMatchTypeEnum: type[
        v20.enums.CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType
    ]
    CampaignPrimaryStatusEnum: type[
        v20.enums.CampaignPrimaryStatusEnum.CampaignPrimaryStatus
    ]
    CampaignPrimaryStatusReasonEnum: type[
        v20.enums.CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    ]
    CampaignServingStatusEnum: type[
        v20.enums.CampaignServingStatusEnum.CampaignServingStatus
    ]
    CampaignSharedSetStatusEnum: type[
        v20.enums.CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    ]
    CampaignStatusEnum: type[v20.enums.CampaignStatusEnum.CampaignStatus]
    ChainRelationshipTypeEnum: type[
        v20.enums.ChainRelationshipTypeEnum.ChainRelationshipType
    ]
    ChangeClientTypeEnum: type[v20.enums.ChangeClientTypeEnum.ChangeClientType]
    ChangeEventResourceTypeEnum: type[
        v20.enums.ChangeEventResourceTypeEnum.ChangeEventResourceType
    ]
    ChangeStatusOperationEnum: type[
        v20.enums.ChangeStatusOperationEnum.ChangeStatusOperation
    ]
    ChangeStatusResourceTypeEnum: type[
        v20.enums.ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    ]
    ClickTypeEnum: type[v20.enums.ClickTypeEnum.ClickType]
    CombinedAudienceStatusEnum: type[
        v20.enums.CombinedAudienceStatusEnum.CombinedAudienceStatus
    ]
    ConsentStatusEnum: type[v20.enums.ConsentStatusEnum.ConsentStatus]
    ContentLabelTypeEnum: type[v20.enums.ContentLabelTypeEnum.ContentLabelType]
    ConversionActionCategoryEnum: type[
        v20.enums.ConversionActionCategoryEnum.ConversionActionCategory
    ]
    ConversionActionCountingTypeEnum: type[
        v20.enums.ConversionActionCountingTypeEnum.ConversionActionCountingType
    ]
    ConversionActionStatusEnum: type[
        v20.enums.ConversionActionStatusEnum.ConversionActionStatus
    ]
    ConversionActionTypeEnum: type[
        v20.enums.ConversionActionTypeEnum.ConversionActionType
    ]
    ConversionAdjustmentTypeEnum: type[
        v20.enums.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    ]
    ConversionAttributionEventTypeEnum: type[
        v20.enums.ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    ]
    ConversionCustomVariableStatusEnum: type[
        v20.enums.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    ]
    ConversionCustomerTypeEnum: type[
        v20.enums.ConversionCustomerTypeEnum.ConversionCustomerType
    ]
    ConversionEnvironmentEnum: type[
        v20.enums.ConversionEnvironmentEnum.ConversionEnvironment
    ]
    ConversionLagBucketEnum: type[v20.enums.ConversionLagBucketEnum.ConversionLagBucket]
    ConversionOrAdjustmentLagBucketEnum: type[
        v20.enums.ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    ]
    ConversionOriginEnum: type[v20.enums.ConversionOriginEnum.ConversionOrigin]
    ConversionTrackingStatusEnum: type[
        v20.enums.ConversionTrackingStatusEnum.ConversionTrackingStatus
    ]
    ConversionValueRulePrimaryDimensionEnum: type[
        v20.enums.ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    ]
    ConversionValueRuleSetStatusEnum: type[
        v20.enums.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    ]
    ConversionValueRuleStatusEnum: type[
        v20.enums.ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    ]
    ConvertingUserPriorEngagementTypeAndLtvBucketEnum: type[
        v20.enums.ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket
    ]
    CriterionCategoryChannelAvailabilityModeEnum: type[
        v20.enums.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    ]
    CriterionCategoryLocaleAvailabilityModeEnum: type[
        v20.enums.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    ]
    CriterionSystemServingStatusEnum: type[
        v20.enums.CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    ]
    CriterionTypeEnum: type[v20.enums.CriterionTypeEnum.CriterionType]
    CustomAudienceMemberTypeEnum: type[
        v20.enums.CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    ]
    CustomAudienceStatusEnum: type[
        v20.enums.CustomAudienceStatusEnum.CustomAudienceStatus
    ]
    CustomAudienceTypeEnum: type[v20.enums.CustomAudienceTypeEnum.CustomAudienceType]
    CustomConversionGoalStatusEnum: type[
        v20.enums.CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    ]
    CustomInterestMemberTypeEnum: type[
        v20.enums.CustomInterestMemberTypeEnum.CustomInterestMemberType
    ]
    CustomInterestStatusEnum: type[
        v20.enums.CustomInterestStatusEnum.CustomInterestStatus
    ]
    CustomInterestTypeEnum: type[v20.enums.CustomInterestTypeEnum.CustomInterestType]
    CustomerAcquisitionOptimizationModeEnum: type[
        v20.enums.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    ]
    CustomerMatchUploadKeyTypeEnum: type[
        v20.enums.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    ]
    CustomerPayPerConversionEligibilityFailureReasonEnum: type[
        v20.enums.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    ]
    CustomerStatusEnum: type[v20.enums.CustomerStatusEnum.CustomerStatus]
    CustomizerAttributeStatusEnum: type[
        v20.enums.CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    ]
    CustomizerAttributeTypeEnum: type[
        v20.enums.CustomizerAttributeTypeEnum.CustomizerAttributeType
    ]
    CustomizerValueStatusEnum: type[
        v20.enums.CustomizerValueStatusEnum.CustomizerValueStatus
    ]
    DataDrivenModelStatusEnum: type[
        v20.enums.DataDrivenModelStatusEnum.DataDrivenModelStatus
    ]
    DataLinkStatusEnum: type[v20.enums.DataLinkStatusEnum.DataLinkStatus]
    DataLinkTypeEnum: type[v20.enums.DataLinkTypeEnum.DataLinkType]
    DayOfWeekEnum: type[v20.enums.DayOfWeekEnum.DayOfWeek]
    DemandGenChannelConfigEnum: type[
        v20.enums.DemandGenChannelConfigEnum.DemandGenChannelConfig
    ]
    DemandGenChannelStrategyEnum: type[
        v20.enums.DemandGenChannelStrategyEnum.DemandGenChannelStrategy
    ]
    DeviceEnum: type[v20.enums.DeviceEnum.Device]
    DisplayAdFormatSettingEnum: type[
        v20.enums.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    ]
    DisplayUploadProductTypeEnum: type[
        v20.enums.DisplayUploadProductTypeEnum.DisplayUploadProductType
    ]
    DistanceBucketEnum: type[v20.enums.DistanceBucketEnum.DistanceBucket]
    ExperimentMetricDirectionEnum: type[
        v20.enums.ExperimentMetricDirectionEnum.ExperimentMetricDirection
    ]
    ExperimentMetricEnum: type[v20.enums.ExperimentMetricEnum.ExperimentMetric]
    ExperimentStatusEnum: type[v20.enums.ExperimentStatusEnum.ExperimentStatus]
    ExperimentTypeEnum: type[v20.enums.ExperimentTypeEnum.ExperimentType]
    ExternalConversionSourceEnum: type[
        v20.enums.ExternalConversionSourceEnum.ExternalConversionSource
    ]
    FixedCpmGoalEnum: type[v20.enums.FixedCpmGoalEnum.FixedCpmGoal]
    FixedCpmTargetFrequencyTimeUnitEnum: type[
        v20.enums.FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit
    ]
    FrequencyCapEventTypeEnum: type[
        v20.enums.FrequencyCapEventTypeEnum.FrequencyCapEventType
    ]
    FrequencyCapLevelEnum: type[v20.enums.FrequencyCapLevelEnum.FrequencyCapLevel]
    FrequencyCapTimeUnitEnum: type[
        v20.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    ]
    GenderTypeEnum: type[v20.enums.GenderTypeEnum.GenderType]
    GeoTargetConstantStatusEnum: type[
        v20.enums.GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    ]
    GeoTargetingTypeEnum: type[v20.enums.GeoTargetingTypeEnum.GeoTargetingType]
    GoalConfigLevelEnum: type[v20.enums.GoalConfigLevelEnum.GoalConfigLevel]
    GoogleAdsFieldCategoryEnum: type[
        v20.enums.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    ]
    GoogleAdsFieldDataTypeEnum: type[
        v20.enums.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    ]
    GoogleVoiceCallStatusEnum: type[
        v20.enums.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
    ]
    HotelAssetSuggestionStatusEnum: type[
        v20.enums.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    ]
    HotelDateSelectionTypeEnum: type[
        v20.enums.HotelDateSelectionTypeEnum.HotelDateSelectionType
    ]
    HotelPriceBucketEnum: type[v20.enums.HotelPriceBucketEnum.HotelPriceBucket]
    HotelRateTypeEnum: type[v20.enums.HotelRateTypeEnum.HotelRateType]
    HotelReconciliationStatusEnum: type[
        v20.enums.HotelReconciliationStatusEnum.HotelReconciliationStatus
    ]
    IdentityVerificationProgramEnum: type[
        v20.enums.IdentityVerificationProgramEnum.IdentityVerificationProgram
    ]
    IdentityVerificationProgramStatusEnum: type[
        v20.enums.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    ]
    IncomeRangeTypeEnum: type[v20.enums.IncomeRangeTypeEnum.IncomeRangeType]
    InsightsKnowledgeGraphEntityCapabilitiesEnum: type[
        v20.enums.InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities
    ]
    InsightsTrendEnum: type[v20.enums.InsightsTrendEnum.InsightsTrend]
    InteractionEventTypeEnum: type[
        v20.enums.InteractionEventTypeEnum.InteractionEventType
    ]
    InteractionTypeEnum: type[v20.enums.InteractionTypeEnum.InteractionType]
    InvoiceTypeEnum: type[v20.enums.InvoiceTypeEnum.InvoiceType]
    KeywordMatchTypeEnum: type[v20.enums.KeywordMatchTypeEnum.KeywordMatchType]
    KeywordPlanAggregateMetricTypeEnum: type[
        v20.enums.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    ]
    KeywordPlanCompetitionLevelEnum: type[
        v20.enums.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    ]
    KeywordPlanConceptGroupTypeEnum: type[
        v20.enums.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    ]
    KeywordPlanForecastIntervalEnum: type[
        v20.enums.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    ]
    KeywordPlanKeywordAnnotationEnum: type[
        v20.enums.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
    ]
    KeywordPlanNetworkEnum: type[v20.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork]
    LabelStatusEnum: type[v20.enums.LabelStatusEnum.LabelStatus]
    LeadFormCallToActionTypeEnum: type[
        v20.enums.LeadFormCallToActionTypeEnum.LeadFormCallToActionType
    ]
    LeadFormDesiredIntentEnum: type[
        v20.enums.LeadFormDesiredIntentEnum.LeadFormDesiredIntent
    ]
    LeadFormFieldUserInputTypeEnum: type[
        v20.enums.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    ]
    LeadFormPostSubmitCallToActionTypeEnum: type[
        v20.enums.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    ]
    LegacyAppInstallAdAppStoreEnum: type[
        v20.enums.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    ]
    LinkedAccountTypeEnum: type[v20.enums.LinkedAccountTypeEnum.LinkedAccountType]
    LinkedProductTypeEnum: type[v20.enums.LinkedProductTypeEnum.LinkedProductType]
    ListingGroupFilterCustomAttributeIndexEnum: type[
        v20.enums.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
    ]
    ListingGroupFilterListingSourceEnum: type[
        v20.enums.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    ]
    ListingGroupFilterProductCategoryLevelEnum: type[
        v20.enums.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    ]
    ListingGroupFilterProductChannelEnum: type[
        v20.enums.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    ]
    ListingGroupFilterProductConditionEnum: type[
        v20.enums.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    ]
    ListingGroupFilterProductTypeLevelEnum: type[
        v20.enums.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    ]
    ListingGroupFilterTypeEnum: type[
        v20.enums.ListingGroupFilterTypeEnum.ListingGroupFilterType
    ]
    ListingGroupTypeEnum: type[v20.enums.ListingGroupTypeEnum.ListingGroupType]
    ListingTypeEnum: type[v20.enums.ListingTypeEnum.ListingType]
    LocalServicesBusinessRegistrationCheckRejectionReasonEnum: type[
        v20.enums.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReason
    ]
    LocalServicesBusinessRegistrationTypeEnum: type[
        v20.enums.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    ]
    LocalServicesCreditStateEnum: type[
        v20.enums.LocalServicesCreditStateEnum.CreditState
    ]
    LocalServicesEmployeeStatusEnum: type[
        v20.enums.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    ]
    LocalServicesEmployeeTypeEnum: type[
        v20.enums.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    ]
    LocalServicesInsuranceRejectionReasonEnum: type[
        v20.enums.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    ]
    LocalServicesLeadConversationTypeEnum: type[
        v20.enums.LocalServicesLeadConversationTypeEnum.ConversationType
    ]
    LocalServicesLeadCreditIssuanceDecisionEnum: type[
        v20.enums.LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    ]
    LocalServicesLeadStatusEnum: type[v20.enums.LocalServicesLeadStatusEnum.LeadStatus]
    LocalServicesLeadSurveyAnswerEnum: type[
        v20.enums.LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    ]
    LocalServicesLeadSurveyDissatisfiedReasonEnum: type[
        v20.enums.LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    ]
    LocalServicesLeadSurveySatisfiedReasonEnum: type[
        v20.enums.LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    ]
    LocalServicesLeadTypeEnum: type[v20.enums.LocalServicesLeadTypeEnum.LeadType]
    LocalServicesLicenseRejectionReasonEnum: type[
        v20.enums.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    ]
    LocalServicesParticipantTypeEnum: type[
        v20.enums.LocalServicesParticipantTypeEnum.ParticipantType
    ]
    LocalServicesVerificationArtifactStatusEnum: type[
        v20.enums.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    ]
    LocalServicesVerificationArtifactTypeEnum: type[
        v20.enums.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    ]
    LocalServicesVerificationStatusEnum: type[
        v20.enums.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    ]
    LocationGroupRadiusUnitsEnum: type[
        v20.enums.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    ]
    LocationOwnershipTypeEnum: type[
        v20.enums.LocationOwnershipTypeEnum.LocationOwnershipType
    ]
    LocationSourceTypeEnum: type[v20.enums.LocationSourceTypeEnum.LocationSourceType]
    LocationStringFilterTypeEnum: type[
        v20.enums.LocationStringFilterTypeEnum.LocationStringFilterType
    ]
    LookalikeExpansionLevelEnum: type[
        v20.enums.LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    ]
    ManagerLinkStatusEnum: type[v20.enums.ManagerLinkStatusEnum.ManagerLinkStatus]
    MediaTypeEnum: type[v20.enums.MediaTypeEnum.MediaType]
    MimeTypeEnum: type[v20.enums.MimeTypeEnum.MimeType]
    MinuteOfHourEnum: type[v20.enums.MinuteOfHourEnum.MinuteOfHour]
    MobileAppVendorEnum: type[v20.enums.MobileAppVendorEnum.MobileAppVendor]
    MobileDeviceTypeEnum: type[v20.enums.MobileDeviceTypeEnum.MobileDeviceType]
    MonthOfYearEnum: type[v20.enums.MonthOfYearEnum.MonthOfYear]
    NegativeGeoTargetTypeEnum: type[
        v20.enums.NegativeGeoTargetTypeEnum.NegativeGeoTargetType
    ]
    NonSkippableMaxDurationEnum: type[
        v20.enums.NonSkippableMaxDurationEnum.NonSkippableMaxDuration
    ]
    NonSkippableMinDurationEnum: type[
        v20.enums.NonSkippableMinDurationEnum.NonSkippableMinDuration
    ]
    OfflineConversionDiagnosticStatusEnum: type[
        v20.enums.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    ]
    OfflineEventUploadClientEnum: type[
        v20.enums.OfflineEventUploadClientEnum.OfflineEventUploadClient
    ]
    OfflineUserDataJobFailureReasonEnum: type[
        v20.enums.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    ]
    OfflineUserDataJobMatchRateRangeEnum: type[
        v20.enums.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
    ]
    OfflineUserDataJobStatusEnum: type[
        v20.enums.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    ]
    OfflineUserDataJobTypeEnum: type[
        v20.enums.OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    ]
    OperatingSystemVersionOperatorTypeEnum: type[
        v20.enums.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    ]
    OptimizationGoalTypeEnum: type[
        v20.enums.OptimizationGoalTypeEnum.OptimizationGoalType
    ]
    ParentalStatusTypeEnum: type[v20.enums.ParentalStatusTypeEnum.ParentalStatusType]
    PaymentModeEnum: type[v20.enums.PaymentModeEnum.PaymentMode]
    PerformanceMaxUpgradeStatusEnum: type[
        v20.enums.PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    ]
    PlacementTypeEnum: type[v20.enums.PlacementTypeEnum.PlacementType]
    PolicyApprovalStatusEnum: type[
        v20.enums.PolicyApprovalStatusEnum.PolicyApprovalStatus
    ]
    PolicyReviewStatusEnum: type[v20.enums.PolicyReviewStatusEnum.PolicyReviewStatus]
    PolicyTopicEntryTypeEnum: type[
        v20.enums.PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    ]
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum: type[
        v20.enums.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
    ]
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum: type[
        v20.enums.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    ]
    PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum: type[
        v20.enums.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
    ]
    PositiveGeoTargetTypeEnum: type[
        v20.enums.PositiveGeoTargetTypeEnum.PositiveGeoTargetType
    ]
    PriceExtensionPriceQualifierEnum: type[
        v20.enums.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    ]
    PriceExtensionPriceUnitEnum: type[
        v20.enums.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    ]
    PriceExtensionTypeEnum: type[v20.enums.PriceExtensionTypeEnum.PriceExtensionType]
    ProductAvailabilityEnum: type[v20.enums.ProductAvailabilityEnum.ProductAvailability]
    ProductCategoryLevelEnum: type[
        v20.enums.ProductCategoryLevelEnum.ProductCategoryLevel
    ]
    ProductCategoryStateEnum: type[
        v20.enums.ProductCategoryStateEnum.ProductCategoryState
    ]
    ProductChannelEnum: type[v20.enums.ProductChannelEnum.ProductChannel]
    ProductChannelExclusivityEnum: type[
        v20.enums.ProductChannelExclusivityEnum.ProductChannelExclusivity
    ]
    ProductConditionEnum: type[v20.enums.ProductConditionEnum.ProductCondition]
    ProductCustomAttributeIndexEnum: type[
        v20.enums.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    ]
    ProductIssueSeverityEnum: type[
        v20.enums.ProductIssueSeverityEnum.ProductIssueSeverity
    ]
    ProductLinkInvitationStatusEnum: type[
        v20.enums.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    ]
    ProductStatusEnum: type[v20.enums.ProductStatusEnum.ProductStatus]
    ProductTypeLevelEnum: type[v20.enums.ProductTypeLevelEnum.ProductTypeLevel]
    PromotionExtensionDiscountModifierEnum: type[
        v20.enums.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    ]
    PromotionExtensionOccasionEnum: type[
        v20.enums.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    ]
    ProximityRadiusUnitsEnum: type[
        v20.enums.ProximityRadiusUnitsEnum.ProximityRadiusUnits
    ]
    QualityScoreBucketEnum: type[v20.enums.QualityScoreBucketEnum.QualityScoreBucket]
    ReachPlanAgeRangeEnum: type[v20.enums.ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    ReachPlanConversionRateModelEnum: type[
        v20.enums.ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    ]
    ReachPlanNetworkEnum: type[v20.enums.ReachPlanNetworkEnum.ReachPlanNetwork]
    ReachPlanPlannableUserListStatusEnum: type[
        v20.enums.ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus
    ]
    ReachPlanSurfaceEnum: type[v20.enums.ReachPlanSurfaceEnum.ReachPlanSurface]
    RecommendationSubscriptionStatusEnum: type[
        v20.enums.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    ]
    RecommendationTypeEnum: type[v20.enums.RecommendationTypeEnum.RecommendationType]
    ResourceChangeOperationEnum: type[
        v20.enums.ResourceChangeOperationEnum.ResourceChangeOperation
    ]
    ResourceLimitTypeEnum: type[v20.enums.ResourceLimitTypeEnum.ResourceLimitType]
    ResponseContentTypeEnum: type[v20.enums.ResponseContentTypeEnum.ResponseContentType]
    SearchEngineResultsPageTypeEnum: type[
        v20.enums.SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    ]
    SearchTermMatchTypeEnum: type[v20.enums.SearchTermMatchTypeEnum.SearchTermMatchType]
    SearchTermTargetingStatusEnum: type[
        v20.enums.SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    ]
    SeasonalityEventScopeEnum: type[
        v20.enums.SeasonalityEventScopeEnum.SeasonalityEventScope
    ]
    SeasonalityEventStatusEnum: type[
        v20.enums.SeasonalityEventStatusEnum.SeasonalityEventStatus
    ]
    ServedAssetFieldTypeEnum: type[
        v20.enums.ServedAssetFieldTypeEnum.ServedAssetFieldType
    ]
    SharedSetStatusEnum: type[v20.enums.SharedSetStatusEnum.SharedSetStatus]
    SharedSetTypeEnum: type[v20.enums.SharedSetTypeEnum.SharedSetType]
    ShoppingAddProductsToCampaignRecommendationEnum: type[
        v20.enums.ShoppingAddProductsToCampaignRecommendationEnum.Reason
    ]
    SimulationModificationMethodEnum: type[
        v20.enums.SimulationModificationMethodEnum.SimulationModificationMethod
    ]
    SimulationTypeEnum: type[v20.enums.SimulationTypeEnum.SimulationType]
    SkAdNetworkAdEventTypeEnum: type[
        v20.enums.SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    ]
    SkAdNetworkAttributionCreditEnum: type[
        v20.enums.SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    ]
    SkAdNetworkCoarseConversionValueEnum: type[
        v20.enums.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    ]
    SkAdNetworkSourceTypeEnum: type[
        v20.enums.SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType
    ]
    SkAdNetworkUserTypeEnum: type[v20.enums.SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
    SlotEnum: type[v20.enums.SlotEnum.Slot]
    SmartCampaignNotEligibleReasonEnum: type[
        v20.enums.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    ]
    SmartCampaignStatusEnum: type[v20.enums.SmartCampaignStatusEnum.SmartCampaignStatus]
    SpendingLimitTypeEnum: type[v20.enums.SpendingLimitTypeEnum.SpendingLimitType]
    SummaryRowSettingEnum: type[v20.enums.SummaryRowSettingEnum.SummaryRowSetting]
    SystemManagedResourceSourceEnum: type[
        v20.enums.SystemManagedResourceSourceEnum.SystemManagedResourceSource
    ]
    TargetCpaOptInRecommendationGoalEnum: type[
        v20.enums.TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    ]
    TargetFrequencyTimeUnitEnum: type[
        v20.enums.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    ]
    TargetImpressionShareLocationEnum: type[
        v20.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    ]
    TargetingDimensionEnum: type[v20.enums.TargetingDimensionEnum.TargetingDimension]
    TimeTypeEnum: type[v20.enums.TimeTypeEnum.TimeType]
    TrackingCodePageFormatEnum: type[
        v20.enums.TrackingCodePageFormatEnum.TrackingCodePageFormat
    ]
    TrackingCodeTypeEnum: type[v20.enums.TrackingCodeTypeEnum.TrackingCodeType]
    UserIdentifierSourceEnum: type[
        v20.enums.UserIdentifierSourceEnum.UserIdentifierSource
    ]
    UserInterestTaxonomyTypeEnum: type[
        v20.enums.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    ]
    UserListAccessStatusEnum: type[
        v20.enums.UserListAccessStatusEnum.UserListAccessStatus
    ]
    UserListClosingReasonEnum: type[
        v20.enums.UserListClosingReasonEnum.UserListClosingReason
    ]
    UserListCrmDataSourceTypeEnum: type[
        v20.enums.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    ]
    UserListCustomerTypeCategoryEnum: type[
        v20.enums.UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory
    ]
    UserListDateRuleItemOperatorEnum: type[
        v20.enums.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    ]
    UserListFlexibleRuleOperatorEnum: type[
        v20.enums.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    ]
    UserListLogicalRuleOperatorEnum: type[
        v20.enums.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    ]
    UserListMembershipStatusEnum: type[
        v20.enums.UserListMembershipStatusEnum.UserListMembershipStatus
    ]
    UserListNumberRuleItemOperatorEnum: type[
        v20.enums.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    ]
    UserListPrepopulationStatusEnum: type[
        v20.enums.UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    ]
    UserListRuleTypeEnum: type[v20.enums.UserListRuleTypeEnum.UserListRuleType]
    UserListSizeRangeEnum: type[v20.enums.UserListSizeRangeEnum.UserListSizeRange]
    UserListStringRuleItemOperatorEnum: type[
        v20.enums.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    ]
    UserListTypeEnum: type[v20.enums.UserListTypeEnum.UserListType]
    ValueRuleDeviceTypeEnum: type[v20.enums.ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
    ValueRuleGeoLocationMatchTypeEnum: type[
        v20.enums.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    ]
    ValueRuleOperationEnum: type[v20.enums.ValueRuleOperationEnum.ValueRuleOperation]
    ValueRuleSetAttachmentTypeEnum: type[
        v20.enums.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    ]
    ValueRuleSetDimensionEnum: type[
        v20.enums.ValueRuleSetDimensionEnum.ValueRuleSetDimension
    ]
    VanityPharmaDisplayUrlModeEnum: type[
        v20.enums.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
    ]
    VanityPharmaTextEnum: type[v20.enums.VanityPharmaTextEnum.VanityPharmaText]
    VideoAdFormatRestrictionEnum: type[
        v20.enums.VideoAdFormatRestrictionEnum.VideoAdFormatRestriction
    ]
    VideoThumbnailEnum: type[v20.enums.VideoThumbnailEnum.VideoThumbnail]
    WebpageConditionOperandEnum: type[
        v20.enums.WebpageConditionOperandEnum.WebpageConditionOperand
    ]
    WebpageConditionOperatorEnum: type[
        v20.enums.WebpageConditionOperatorEnum.WebpageConditionOperator
    ]
    # End of autogenerated enums

class GoogleAdsClient:
    credentials: Credentials
    developer_token: str
    endpoint: str | None
    login_customer_id: str | None
    linked_customer_id: str | None
    version: str | None
    http_proxy: str | None
    use_proto_plus: bool
    enums: _EnumGetter
    @classmethod
    def copy_from(
        cls,
        destination: proto.Message | Message,
        origin: proto.Message | Message,
    ) -> None: ...
    @classmethod
    def load_from_env(cls, version: str | None = None) -> GoogleAdsClient: ...
    @classmethod
    def load_from_string(
        cls, yaml_str: str, version: str | None = None
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_storage(
        cls, path: str | None = None, version: str | None = None
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_dict(
        cls, config_dict: _ConfigDataUnparsed, version: str | None = None
    ) -> GoogleAdsClient: ...
    def __init__(
        self,
        credentials: Credentials,
        developer_token: str,
        endpoint: str | None = None,
        login_customer_id: str | None = None,
        logging_config: dict[Any, Any] | None = None,
        linked_customer_id: str | None = None,
        version: str | None = None,
        http_proxy: str | None = None,
        use_proto_plus: bool = False,
        use_cloud_org_for_api_access: bool | None = None,
    ) -> None: ...
    def get_type(cls, name: str, version: _V = "v21") -> Any: ...
    # Autogenerated service overloads
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.geo_target_constant_service.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.geo_target_constant_service.GeoTargetConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_asset_service.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_asset_service.AdGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_target_service.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_target_service.FeedItemTargetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.offline_user_data_job_service.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.offline_user_data_job_service.OfflineUserDataJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_user_access_service.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_user_access_service.CustomerUserAccessServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_label_service.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_label_service.CampaignLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_signal_service.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_signal_service.AssetGroupSignalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_criterion_service.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_criterion_service.AdGroupCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.google_ads_service.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.google_ads_service.GoogleAdsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.product_link_invitation_service.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.product_link_invitation_service.ProductLinkInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_draft_service.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_draft_service.CampaignDraftServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.billing_setup_service.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.billing_setup_service.BillingSetupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_service.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_service.AssetGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_shared_set_service.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_shared_set_service.CampaignSharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.shared_criterion_service.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.shared_criterion_service.SharedCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_service.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_service.CustomerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_action_service.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_action_service.ConversionActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.reach_plan_service.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.reach_plan_service.ReachPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.user_list_service.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.user_list_service.UserListServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_asset_service.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_asset_service.CustomerAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_upload_service.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_upload_service.ConversionUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.payments_account_service.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.payments_account_service.PaymentsAccountServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_service.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedServiceAsync"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.feed_service.FeedServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_criterion_service.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_criterion_service.CampaignCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_group_service.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_group_service.CampaignGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_customizer_service.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_customizer_service.CampaignCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_parameter_service.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_parameter_service.AdParameterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.remarketing_action_service.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.remarketing_action_service.RemarketingActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.bidding_strategy_service.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.bidding_strategy_service.BiddingStrategyServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.experiment_arm_service.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.experiment_arm_service.ExperimentArmServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_service.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_service.KeywordPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.brand_suggestion_service.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.brand_suggestion_service.BrandSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_ad_service.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_ad_service.AdGroupAdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.product_link_service.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.product_link_service.ProductLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_extension_setting_service.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_extension_setting_service.AdGroupExtensionSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.google_ads_field_service.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.google_ads_field_service.GoogleAdsFieldServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_label_service.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_label_service.AdGroupLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.content_creator_insights_service.ContentCreatorInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.content_creator_insights_service.ContentCreatorInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_asset_service.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_asset_service.CampaignAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_budget_service.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_budget_service.CampaignBudgetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.ad_group_service.AdGroupServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_service.AdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_label_service.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_label_service.CustomerLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_feed_service.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_feed_service.AdGroupFeedServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.recommendation_service.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.recommendation_service.RecommendationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_mapping_service.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_mapping_service.FeedMappingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.extension_feed_item_service.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.extension_feed_item_service.ExtensionFeedItemServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_asset_set_service.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_asset_set_service.CampaignAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_value_rule_service.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_value_rule_service.ConversionValueRuleServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_customizer_service.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_customizer_service.AdGroupCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_customizer_service.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_customizer_service.CustomerCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_asset_service.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_asset_service.AssetGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.custom_interest_service.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.custom_interest_service.CustomInterestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.account_link_service.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.account_link_service.AccountLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.account_budget_proposal_service.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.account_budget_proposal_service.AccountBudgetProposalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.user_data_service.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.user_data_service.UserDataServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.asset_service.AssetServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AssetServiceAsync"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.asset_service.AssetServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V18,
    ) -> google.ads.googleads.v18.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaServiceAsync"],
        version: _V18,
    ) -> google.ads.googleads.v18.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_feed_service.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_feed_service.CampaignFeedServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_service.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_service.CampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.shareable_preview_service.ShareablePreviewServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.shareable_preview_service.ShareablePreviewServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.identity_verification_service.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.identity_verification_service.IdentityVerificationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_extension_setting_service.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_extension_setting_service.CustomerExtensionSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_set_link_service.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_set_link_service.FeedItemSetLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_service.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_service.AdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_manager_link_service.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_manager_link_service.CustomerManagerLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_feed_service.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_feed_service.CustomerFeedServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.user_list_customer_type_service.UserListCustomerTypeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.user_list_customer_type_service.UserListCustomerTypeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_set_service.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_set_service.FeedItemSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.audience_service.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.audience_service.AudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_client_link_service.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_client_link_service.CustomerClientLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_set_service.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_set_service.AssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.custom_conversion_goal_service.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.custom_conversion_goal_service.CustomConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.local_services_lead_service.LocalServicesLeadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.local_services_lead_service.LocalServicesLeadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.custom_audience_service.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.custom_audience_service.CustomAudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.batch_job_service.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.batch_job_service.BatchJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customizer_attribute_service.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customizer_attribute_service.CustomizerAttributeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.label_service.LabelServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["LabelServiceAsync"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.label_service.LabelServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.audience_insights_service.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.audience_insights_service.AudienceInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_asset_set_service.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.customer_asset_set_service.CustomerAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.shared_set_service.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.shared_set_service.SharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_extension_setting_service.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.campaign_extension_setting_service.CampaignExtensionSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.data_link_service.DataLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.data_link_service.DataLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.experiment_service.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.experiment_service.ExperimentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_set_asset_service.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.asset_set_asset_service.AssetSetAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V18
    ) -> (
        google.ads.googleads.v18.services.services.invoice_service.InvoiceServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["InvoiceServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.invoice_service.InvoiceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_service.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemServiceAsync"], version: _V18
    ) -> google.ads.googleads.v18.services.services.feed_item_service.FeedItemServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.geo_target_constant_service.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.geo_target_constant_service.GeoTargetConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_asset_service.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_asset_service.AdGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.offline_user_data_job_service.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.offline_user_data_job_service.OfflineUserDataJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_user_access_service.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_user_access_service.CustomerUserAccessServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_label_service.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_label_service.CampaignLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_signal_service.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_signal_service.AssetGroupSignalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_criterion_service.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_criterion_service.AdGroupCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.google_ads_service.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.google_ads_service.GoogleAdsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.product_link_invitation_service.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.product_link_invitation_service.ProductLinkInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_draft_service.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_draft_service.CampaignDraftServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.billing_setup_service.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.billing_setup_service.BillingSetupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_service.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_service.AssetGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_shared_set_service.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_shared_set_service.CampaignSharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.shared_criterion_service.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.shared_criterion_service.SharedCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_service.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_service.CustomerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_action_service.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_action_service.ConversionActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.reach_plan_service.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.reach_plan_service.ReachPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.user_list_service.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.user_list_service.UserListServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_asset_service.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_asset_service.CustomerAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_upload_service.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_upload_service.ConversionUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.payments_account_service.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.payments_account_service.PaymentsAccountServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_criterion_service.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_criterion_service.CampaignCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_group_service.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_group_service.CampaignGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_customizer_service.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_customizer_service.CampaignCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_parameter_service.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_parameter_service.AdParameterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.remarketing_action_service.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.remarketing_action_service.RemarketingActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.bidding_strategy_service.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.bidding_strategy_service.BiddingStrategyServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.experiment_arm_service.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.experiment_arm_service.ExperimentArmServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_service.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_service.KeywordPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.brand_suggestion_service.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.brand_suggestion_service.BrandSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_ad_service.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_ad_service.AdGroupAdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.product_link_service.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.product_link_service.ProductLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.google_ads_field_service.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.google_ads_field_service.GoogleAdsFieldServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_label_service.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_label_service.AdGroupLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.content_creator_insights_service.ContentCreatorInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.content_creator_insights_service.ContentCreatorInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_asset_service.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_asset_service.CampaignAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_budget_service.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_budget_service.CampaignBudgetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V19
    ) -> (
        google.ads.googleads.v19.services.services.ad_group_service.AdGroupServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_service.AdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_label_service.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_label_service.CustomerLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.recommendation_service.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.recommendation_service.RecommendationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_asset_set_service.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_asset_set_service.CampaignAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_value_rule_service.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_value_rule_service.ConversionValueRuleServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_customizer_service.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_customizer_service.AdGroupCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_customizer_service.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_customizer_service.CustomerCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_asset_service.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_asset_service.AssetGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.custom_interest_service.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.custom_interest_service.CustomInterestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.account_link_service.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.account_link_service.AccountLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.account_budget_proposal_service.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.account_budget_proposal_service.AccountBudgetProposalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.user_data_service.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.user_data_service.UserDataServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V19
    ) -> (
        google.ads.googleads.v19.services.services.asset_service.AssetServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AssetServiceAsync"], version: _V19
    ) -> (
        google.ads.googleads.v19.services.services.asset_service.AssetServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V19,
    ) -> google.ads.googleads.v19.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaServiceAsync"],
        version: _V19,
    ) -> google.ads.googleads.v19.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_service.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.campaign_service.CampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.shareable_preview_service.ShareablePreviewServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.shareable_preview_service.ShareablePreviewServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.identity_verification_service.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.identity_verification_service.IdentityVerificationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_service.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_service.AdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_manager_link_service.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_manager_link_service.CustomerManagerLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.user_list_customer_type_service.UserListCustomerTypeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.user_list_customer_type_service.UserListCustomerTypeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.audience_service.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.audience_service.AudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_client_link_service.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_client_link_service.CustomerClientLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_set_service.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_set_service.AssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.custom_conversion_goal_service.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.custom_conversion_goal_service.CustomConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.local_services_lead_service.LocalServicesLeadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.local_services_lead_service.LocalServicesLeadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.custom_audience_service.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.custom_audience_service.CustomAudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.batch_job_service.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.batch_job_service.BatchJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customizer_attribute_service.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customizer_attribute_service.CustomizerAttributeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V19
    ) -> (
        google.ads.googleads.v19.services.services.label_service.LabelServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["LabelServiceAsync"], version: _V19
    ) -> (
        google.ads.googleads.v19.services.services.label_service.LabelServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.audience_insights_service.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.audience_insights_service.AudienceInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_asset_set_service.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.customer_asset_set_service.CustomerAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.shared_set_service.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.shared_set_service.SharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.data_link_service.DataLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.data_link_service.DataLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.experiment_service.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.experiment_service.ExperimentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_set_asset_service.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.asset_set_asset_service.AssetSetAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V19
    ) -> (
        google.ads.googleads.v19.services.services.invoice_service.InvoiceServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["InvoiceServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.invoice_service.InvoiceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignServiceAsync"], version: _V19
    ) -> google.ads.googleads.v19.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.geo_target_constant_service.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"]
    ) -> google.ads.googleads.v20.services.services.geo_target_constant_service.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.geo_target_constant_service.GeoTargetConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.geo_target_constant_service.GeoTargetConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_service.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_service.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_service.AdGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_service.AdGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.offline_user_data_job_service.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"]
    ) -> google.ads.googleads.v20.services.services.offline_user_data_job_service.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.offline_user_data_job_service.OfflineUserDataJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.offline_user_data_job_service.OfflineUserDataJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"]
    ) -> google.ads.googleads.v20.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_conversion_goal_service.CampaignConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_user_access_service.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"]
    ) -> google.ads.googleads.v20.services.services.customer_user_access_service.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_user_access_service.CustomerUserAccessServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_user_access_service.CustomerUserAccessServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_service.KeywordPlanAdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_label_service.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"]
    ) -> google.ads.googleads.v20.services.services.campaign_label_service.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_label_service.CampaignLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_label_service.CampaignLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"]
    ) -> google.ads.googleads.v20.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_theme_constant_service.KeywordThemeConstantServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_signal_service.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"]
    ) -> google.ads.googleads.v20.services.services.asset_group_signal_service.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_signal_service.AssetGroupSignalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.asset_group_signal_service.AssetGroupSignalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_bid_modifier_service.AdGroupBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_service.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_service.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_service.AdGroupCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_service.AdGroupCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.google_ads_service.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"]
    ) -> google.ads.googleads.v20.services.services.google_ads_service.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.google_ads_service.GoogleAdsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.google_ads_service.GoogleAdsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.product_link_invitation_service.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"]
    ) -> google.ads.googleads.v20.services.services.product_link_invitation_service.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.product_link_invitation_service.ProductLinkInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.product_link_invitation_service.ProductLinkInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_draft_service.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"]
    ) -> google.ads.googleads.v20.services.services.campaign_draft_service.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_draft_service.CampaignDraftServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_draft_service.CampaignDraftServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.billing_setup_service.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"]
    ) -> google.ads.googleads.v20.services.services.billing_setup_service.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.billing_setup_service.BillingSetupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.billing_setup_service.BillingSetupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_service.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"]
    ) -> google.ads.googleads.v20.services.services.asset_group_service.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_service.AssetGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.asset_group_service.AssetGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_shared_set_service.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"]
    ) -> google.ads.googleads.v20.services.services.campaign_shared_set_service.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_shared_set_service.CampaignSharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_shared_set_service.CampaignSharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_ad_group_keyword_service.KeywordPlanAdGroupKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.shared_criterion_service.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"]
    ) -> google.ads.googleads.v20.services.services.shared_criterion_service.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.shared_criterion_service.SharedCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.shared_criterion_service.SharedCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_service.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"]
    ) -> google.ads.googleads.v20.services.services.customer_service.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_service.CustomerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_service.CustomerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_action_service.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"]
    ) -> google.ads.googleads.v20.services.services.conversion_action_service.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_action_service.ConversionActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_action_service.ConversionActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_customizer_service.AdGroupCriterionCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.reach_plan_service.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"]
    ) -> google.ads.googleads.v20.services.services.reach_plan_service.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.reach_plan_service.ReachPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.reach_plan_service.ReachPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.user_list_service.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"]
    ) -> google.ads.googleads.v20.services.services.user_list_service.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.user_list_service.UserListServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.user_list_service.UserListServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_asset_service.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"]
    ) -> google.ads.googleads.v20.services.services.customer_asset_service.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_asset_service.CustomerAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_asset_service.CustomerAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_upload_service.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"]
    ) -> google.ads.googleads.v20.services.services.conversion_upload_service.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_upload_service.ConversionUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_upload_service.ConversionUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.payments_account_service.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"]
    ) -> google.ads.googleads.v20.services.services.payments_account_service.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.payments_account_service.PaymentsAccountServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.payments_account_service.PaymentsAccountServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"]
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_set_service.ConversionValueRuleSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_criterion_service.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"]
    ) -> google.ads.googleads.v20.services.services.campaign_criterion_service.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_criterion_service.CampaignCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_criterion_service.CampaignCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_group_service.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"]
    ) -> google.ads.googleads.v20.services.services.campaign_group_service.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_group_service.CampaignGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_group_service.CampaignGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_customizer_service.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"]
    ) -> google.ads.googleads.v20.services.services.campaign_customizer_service.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_customizer_service.CampaignCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_customizer_service.CampaignCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_parameter_service.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"]
    ) -> google.ads.googleads.v20.services.services.ad_parameter_service.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_parameter_service.AdParameterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_parameter_service.AdParameterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.remarketing_action_service.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"]
    ) -> google.ads.googleads.v20.services.services.remarketing_action_service.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.remarketing_action_service.RemarketingActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.remarketing_action_service.RemarketingActionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.bidding_strategy_service.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"]
    ) -> google.ads.googleads.v20.services.services.bidding_strategy_service.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.bidding_strategy_service.BiddingStrategyServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.bidding_strategy_service.BiddingStrategyServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.experiment_arm_service.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"]
    ) -> google.ads.googleads.v20.services.services.experiment_arm_service.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.experiment_arm_service.ExperimentArmServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.experiment_arm_service.ExperimentArmServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_service.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_service.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_service.KeywordPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_service.KeywordPlanServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"]
    ) -> google.ads.googleads.v20.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_negative_criterion_service.CustomerNegativeCriterionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.brand_suggestion_service.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"]
    ) -> google.ads.googleads.v20.services.services.brand_suggestion_service.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.brand_suggestion_service.BrandSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.brand_suggestion_service.BrandSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_service.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_service.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_service.AdGroupAdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_service.AdGroupAdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_idea_service.KeywordPlanIdeaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"]
    ) -> google.ads.googleads.v20.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_bid_modifier_service.CampaignBidModifierServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.product_link_service.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"]
    ) -> google.ads.googleads.v20.services.services.product_link_service.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.product_link_service.ProductLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.product_link_service.ProductLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.google_ads_field_service.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"]
    ) -> google.ads.googleads.v20.services.services.google_ads_field_service.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.google_ads_field_service.GoogleAdsFieldServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.google_ads_field_service.GoogleAdsFieldServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_keyword_service.KeywordPlanCampaignKeywordServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_label_service.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_label_service.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_label_service.AdGroupLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_label_service.AdGroupLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.content_creator_insights_service.ContentCreatorInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsService"]
    ) -> google.ads.googleads.v20.services.services.content_creator_insights_service.ContentCreatorInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.content_creator_insights_service.ContentCreatorInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ContentCreatorInsightsServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.content_creator_insights_service.ContentCreatorInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"]
    ) -> google.ads.googleads.v20.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_lifecycle_goal_service.CampaignLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"]
    ) -> google.ads.googleads.v20.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.smart_campaign_suggest_service.SmartCampaignSuggestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_asset_service.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"]
    ) -> google.ads.googleads.v20.services.services.campaign_asset_service.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_asset_service.CampaignAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_asset_service.CampaignAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_asset_set_service.AdGroupAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_budget_service.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"]
    ) -> google.ads.googleads.v20.services.services.campaign_budget_service.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_budget_service.CampaignBudgetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_budget_service.CampaignBudgetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V20
    ) -> (
        google.ads.googleads.v20.services.services.ad_group_service.AdGroupServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"]
    ) -> (
        google.ads.googleads.v20.services.services.ad_group_service.AdGroupServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_service.AdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_service.AdGroupServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_label_service.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"]
    ) -> google.ads.googleads.v20.services.services.customer_label_service.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_label_service.CustomerLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_label_service.CustomerLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.recommendation_service.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"]
    ) -> google.ads.googleads.v20.services.services.recommendation_service.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.recommendation_service.RecommendationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.recommendation_service.RecommendationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"]
    ) -> google.ads.googleads.v20.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.recommendation_subscription_service.RecommendationSubscriptionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"]
    ) -> google.ads.googleads.v20.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_custom_variable_service.ConversionCustomVariableServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_asset_set_service.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"]
    ) -> google.ads.googleads.v20.services.services.campaign_asset_set_service.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_asset_set_service.CampaignAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_asset_set_service.CampaignAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_service.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"]
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_service.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_service.ConversionValueRuleServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_value_rule_service.ConversionValueRuleServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_customizer_service.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_customizer_service.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_customizer_service.AdGroupCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_customizer_service.AdGroupCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_customizer_service.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"]
    ) -> google.ads.googleads.v20.services.services.customer_customizer_service.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_customizer_service.CustomerCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_customizer_service.CustomerCustomizerServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_asset_service.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"]
    ) -> google.ads.googleads.v20.services.services.asset_group_asset_service.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_asset_service.AssetGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.asset_group_asset_service.AssetGroupAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.custom_interest_service.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"]
    ) -> google.ads.googleads.v20.services.services.custom_interest_service.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.custom_interest_service.CustomInterestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.custom_interest_service.CustomInterestServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.account_link_service.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"]
    ) -> google.ads.googleads.v20.services.services.account_link_service.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.account_link_service.AccountLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.account_link_service.AccountLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.account_budget_proposal_service.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"]
    ) -> google.ads.googleads.v20.services.services.account_budget_proposal_service.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.account_budget_proposal_service.AccountBudgetProposalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.account_budget_proposal_service.AccountBudgetProposalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.user_data_service.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"]
    ) -> google.ads.googleads.v20.services.services.user_data_service.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.user_data_service.UserDataServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.user_data_service.UserDataServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V20
    ) -> (
        google.ads.googleads.v20.services.services.asset_service.AssetServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AssetService"]
    ) -> (
        google.ads.googleads.v20.services.services.asset_service.AssetServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AssetServiceAsync"], version: _V20
    ) -> (
        google.ads.googleads.v20.services.services.asset_service.AssetServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AssetServiceAsync"]
    ) -> (
        google.ads.googleads.v20.services.services.asset_service.AssetServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V20,
    ) -> google.ads.googleads.v20.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerSkAdNetworkConversionValueSchemaService"]
    ) -> google.ads.googleads.v20.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaServiceAsync"],
        version: _V20,
    ) -> google.ads.googleads.v20.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerSkAdNetworkConversionValueSchemaServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_sk_ad_network_conversion_value_schema_service.CustomerSkAdNetworkConversionValueSchemaServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"]
    ) -> google.ads.googleads.v20.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_user_access_invitation_service.CustomerUserAccessInvitationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"]
    ) -> google.ads.googleads.v20.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.smart_campaign_setting_service.SmartCampaignSettingServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_service.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"]
    ) -> google.ads.googleads.v20.services.services.campaign_service.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.campaign_service.CampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.campaign_service.CampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.shareable_preview_service.ShareablePreviewServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewService"]
    ) -> google.ads.googleads.v20.services.services.shareable_preview_service.ShareablePreviewServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.shareable_preview_service.ShareablePreviewServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.shareable_preview_service.ShareablePreviewServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.identity_verification_service.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"]
    ) -> google.ads.googleads.v20.services.services.identity_verification_service.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.identity_verification_service.IdentityVerificationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.identity_verification_service.IdentityVerificationServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"]
    ) -> google.ads.googleads.v20.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_lifecycle_goal_service.CustomerLifecycleGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_ad_label_service.AdGroupAdLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_service.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"]
    ) -> google.ads.googleads.v20.services.services.ad_service.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_service.AdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_service.AdServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_manager_link_service.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"]
    ) -> google.ads.googleads.v20.services.services.customer_manager_link_service.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_manager_link_service.CustomerManagerLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_manager_link_service.CustomerManagerLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"]
    ) -> google.ads.googleads.v20.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.asset_group_listing_group_filter_service.AssetGroupListingGroupFilterServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.user_list_customer_type_service.UserListCustomerTypeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeService"]
    ) -> google.ads.googleads.v20.services.services.user_list_customer_type_service.UserListCustomerTypeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.user_list_customer_type_service.UserListCustomerTypeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.user_list_customer_type_service.UserListCustomerTypeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"]
    ) -> google.ads.googleads.v20.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.bidding_seasonality_adjustment_service.BiddingSeasonalityAdjustmentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"]
    ) -> google.ads.googleads.v20.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_goal_campaign_config_service.ConversionGoalCampaignConfigServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"]
    ) -> google.ads.googleads.v20.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.bidding_data_exclusion_service.BiddingDataExclusionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.audience_service.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"]
    ) -> google.ads.googleads.v20.services.services.audience_service.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.audience_service.AudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.audience_service.AudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_client_link_service.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"]
    ) -> google.ads.googleads.v20.services.services.customer_client_link_service.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_client_link_service.CustomerClientLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_client_link_service.CustomerClientLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_set_service.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"]
    ) -> google.ads.googleads.v20.services.services.asset_set_service.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_set_service.AssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.asset_set_service.AssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.custom_conversion_goal_service.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"]
    ) -> google.ads.googleads.v20.services.services.custom_conversion_goal_service.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.custom_conversion_goal_service.CustomConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.custom_conversion_goal_service.CustomConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.local_services_lead_service.LocalServicesLeadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadService"]
    ) -> google.ads.googleads.v20.services.services.local_services_lead_service.LocalServicesLeadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.local_services_lead_service.LocalServicesLeadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.local_services_lead_service.LocalServicesLeadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"]
    ) -> google.ads.googleads.v20.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_conversion_goal_service.CustomerConversionGoalServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"]
    ) -> google.ads.googleads.v20.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.conversion_adjustment_upload_service.ConversionAdjustmentUploadServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.custom_audience_service.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"]
    ) -> google.ads.googleads.v20.services.services.custom_audience_service.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.custom_audience_service.CustomAudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.custom_audience_service.CustomAudienceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.batch_job_service.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"]
    ) -> google.ads.googleads.v20.services.services.batch_job_service.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.batch_job_service.BatchJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.batch_job_service.BatchJobServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"]
    ) -> google.ads.googleads.v20.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.third_party_app_analytics_link_service.ThirdPartyAppAnalyticsLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"]
    ) -> google.ads.googleads.v20.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.travel_asset_suggestion_service.TravelAssetSuggestionServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customizer_attribute_service.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"]
    ) -> google.ads.googleads.v20.services.services.customizer_attribute_service.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customizer_attribute_service.CustomizerAttributeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customizer_attribute_service.CustomizerAttributeServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V20
    ) -> (
        google.ads.googleads.v20.services.services.label_service.LabelServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["LabelService"]
    ) -> (
        google.ads.googleads.v20.services.services.label_service.LabelServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["LabelServiceAsync"], version: _V20
    ) -> (
        google.ads.googleads.v20.services.services.label_service.LabelServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["LabelServiceAsync"]
    ) -> (
        google.ads.googleads.v20.services.services.label_service.LabelServiceAsyncClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"]
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.ad_group_criterion_label_service.AdGroupCriterionLabelServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.audience_insights_service.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"]
    ) -> google.ads.googleads.v20.services.services.audience_insights_service.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.audience_insights_service.AudienceInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.audience_insights_service.AudienceInsightsServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_asset_set_service.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"]
    ) -> google.ads.googleads.v20.services.services.customer_asset_set_service.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.customer_asset_set_service.CustomerAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.customer_asset_set_service.CustomerAssetSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.shared_set_service.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"]
    ) -> google.ads.googleads.v20.services.services.shared_set_service.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.shared_set_service.SharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.shared_set_service.SharedSetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.data_link_service.DataLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkService"]
    ) -> google.ads.googleads.v20.services.services.data_link_service.DataLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.data_link_service.DataLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["DataLinkServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.data_link_service.DataLinkServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.experiment_service.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"]
    ) -> google.ads.googleads.v20.services.services.experiment_service.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.experiment_service.ExperimentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.experiment_service.ExperimentServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_set_asset_service.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"]
    ) -> google.ads.googleads.v20.services.services.asset_set_asset_service.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.asset_set_asset_service.AssetSetAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.asset_set_asset_service.AssetSetAssetServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V20
    ) -> (
        google.ads.googleads.v20.services.services.invoice_service.InvoiceServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"]
    ) -> (
        google.ads.googleads.v20.services.services.invoice_service.InvoiceServiceClient
    ): ...
    @overload
    def get_service(
        self, name: Literal["InvoiceServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.invoice_service.InvoiceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.invoice_service.InvoiceServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignServiceAsync"], version: _V20
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceAsyncClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignServiceAsync"]
    ) -> google.ads.googleads.v20.services.services.keyword_plan_campaign_service.KeywordPlanCampaignServiceAsyncClient: ...
    @overload
    def get_service(self, name: str, version: _V = "v20") -> Any: ...
    # End of autogenerated service overloads
