from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.duration_pb2 import Duration
from typing_extensions import Literal

from google.ads.googleads.v16.common.types.policy import (
    PolicyTopicEntry,
    PolicyViolationKey,
)
from google.ads.googleads.v16.common.types.value import Value
from google.ads.googleads.v16.enums.types.resource_limit_type import (
    ResourceLimitTypeEnum,
)
from google.ads.googleads.v16.errors.types.access_invitation_error import (
    AccessInvitationErrorEnum,
)
from google.ads.googleads.v16.errors.types.account_budget_proposal_error import (
    AccountBudgetProposalErrorEnum,
)
from google.ads.googleads.v16.errors.types.account_link_error import (
    AccountLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_customizer_error import (
    AdCustomizerErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_error import AdErrorEnum
from google.ads.googleads.v16.errors.types.ad_group_ad_error import AdGroupAdErrorEnum
from google.ads.googleads.v16.errors.types.ad_group_bid_modifier_error import (
    AdGroupBidModifierErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_group_criterion_customizer_error import (
    AdGroupCriterionCustomizerErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_group_criterion_error import (
    AdGroupCriterionErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_group_customizer_error import (
    AdGroupCustomizerErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_group_error import AdGroupErrorEnum
from google.ads.googleads.v16.errors.types.ad_group_feed_error import (
    AdGroupFeedErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_parameter_error import (
    AdParameterErrorEnum,
)
from google.ads.googleads.v16.errors.types.ad_sharing_error import AdSharingErrorEnum
from google.ads.googleads.v16.errors.types.adx_error import AdxErrorEnum
from google.ads.googleads.v16.errors.types.asset_error import AssetErrorEnum
from google.ads.googleads.v16.errors.types.asset_group_asset_error import (
    AssetGroupAssetErrorEnum,
)
from google.ads.googleads.v16.errors.types.asset_group_error import AssetGroupErrorEnum
from google.ads.googleads.v16.errors.types.asset_group_listing_group_filter_error import (
    AssetGroupListingGroupFilterErrorEnum,
)
from google.ads.googleads.v16.errors.types.asset_group_signal_error import (
    AssetGroupSignalErrorEnum,
)
from google.ads.googleads.v16.errors.types.asset_link_error import AssetLinkErrorEnum
from google.ads.googleads.v16.errors.types.asset_set_asset_error import (
    AssetSetAssetErrorEnum,
)
from google.ads.googleads.v16.errors.types.asset_set_error import AssetSetErrorEnum
from google.ads.googleads.v16.errors.types.asset_set_link_error import (
    AssetSetLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.audience_error import AudienceErrorEnum
from google.ads.googleads.v16.errors.types.audience_insights_error import (
    AudienceInsightsErrorEnum,
)
from google.ads.googleads.v16.errors.types.authentication_error import (
    AuthenticationErrorEnum,
)
from google.ads.googleads.v16.errors.types.authorization_error import (
    AuthorizationErrorEnum,
)
from google.ads.googleads.v16.errors.types.batch_job_error import BatchJobErrorEnum
from google.ads.googleads.v16.errors.types.bidding_error import BiddingErrorEnum
from google.ads.googleads.v16.errors.types.bidding_strategy_error import (
    BiddingStrategyErrorEnum,
)
from google.ads.googleads.v16.errors.types.billing_setup_error import (
    BillingSetupErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_budget_error import (
    CampaignBudgetErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_conversion_goal_error import (
    CampaignConversionGoalErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_criterion_error import (
    CampaignCriterionErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_customizer_error import (
    CampaignCustomizerErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_draft_error import (
    CampaignDraftErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_error import CampaignErrorEnum
from google.ads.googleads.v16.errors.types.campaign_experiment_error import (
    CampaignExperimentErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_feed_error import (
    CampaignFeedErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_lifecycle_goal_error import (
    CampaignLifecycleGoalErrorEnum,
)
from google.ads.googleads.v16.errors.types.campaign_shared_set_error import (
    CampaignSharedSetErrorEnum,
)
from google.ads.googleads.v16.errors.types.change_event_error import (
    ChangeEventErrorEnum,
)
from google.ads.googleads.v16.errors.types.change_status_error import (
    ChangeStatusErrorEnum,
)
from google.ads.googleads.v16.errors.types.collection_size_error import (
    CollectionSizeErrorEnum,
)
from google.ads.googleads.v16.errors.types.context_error import ContextErrorEnum
from google.ads.googleads.v16.errors.types.conversion_action_error import (
    ConversionActionErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_adjustment_upload_error import (
    ConversionAdjustmentUploadErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_custom_variable_error import (
    ConversionCustomVariableErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_goal_campaign_config_error import (
    ConversionGoalCampaignConfigErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_upload_error import (
    ConversionUploadErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_value_rule_error import (
    ConversionValueRuleErrorEnum,
)
from google.ads.googleads.v16.errors.types.conversion_value_rule_set_error import (
    ConversionValueRuleSetErrorEnum,
)
from google.ads.googleads.v16.errors.types.country_code_error import (
    CountryCodeErrorEnum,
)
from google.ads.googleads.v16.errors.types.criterion_error import CriterionErrorEnum
from google.ads.googleads.v16.errors.types.currency_code_error import (
    CurrencyCodeErrorEnum,
)
from google.ads.googleads.v16.errors.types.currency_error import CurrencyErrorEnum
from google.ads.googleads.v16.errors.types.custom_audience_error import (
    CustomAudienceErrorEnum,
)
from google.ads.googleads.v16.errors.types.custom_conversion_goal_error import (
    CustomConversionGoalErrorEnum,
)
from google.ads.googleads.v16.errors.types.custom_interest_error import (
    CustomInterestErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_client_link_error import (
    CustomerClientLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_customizer_error import (
    CustomerCustomizerErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_error import CustomerErrorEnum
from google.ads.googleads.v16.errors.types.customer_feed_error import (
    CustomerFeedErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_lifecycle_goal_error import (
    CustomerLifecycleGoalErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_manager_link_error import (
    CustomerManagerLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_sk_ad_network_conversion_value_schema_error import (
    CustomerSkAdNetworkConversionValueSchemaErrorEnum,
)
from google.ads.googleads.v16.errors.types.customer_user_access_error import (
    CustomerUserAccessErrorEnum,
)
from google.ads.googleads.v16.errors.types.customizer_attribute_error import (
    CustomizerAttributeErrorEnum,
)
from google.ads.googleads.v16.errors.types.database_error import DatabaseErrorEnum
from google.ads.googleads.v16.errors.types.date_error import DateErrorEnum
from google.ads.googleads.v16.errors.types.date_range_error import DateRangeErrorEnum
from google.ads.googleads.v16.errors.types.distinct_error import DistinctErrorEnum
from google.ads.googleads.v16.errors.types.enum_error import EnumErrorEnum
from google.ads.googleads.v16.errors.types.experiment_arm_error import (
    ExperimentArmErrorEnum,
)
from google.ads.googleads.v16.errors.types.experiment_error import ExperimentErrorEnum
from google.ads.googleads.v16.errors.types.extension_feed_item_error import (
    ExtensionFeedItemErrorEnum,
)
from google.ads.googleads.v16.errors.types.extension_setting_error import (
    ExtensionSettingErrorEnum,
)
from google.ads.googleads.v16.errors.types.feed_attribute_reference_error import (
    FeedAttributeReferenceErrorEnum,
)
from google.ads.googleads.v16.errors.types.feed_error import FeedErrorEnum
from google.ads.googleads.v16.errors.types.feed_item_error import FeedItemErrorEnum
from google.ads.googleads.v16.errors.types.feed_item_set_error import (
    FeedItemSetErrorEnum,
)
from google.ads.googleads.v16.errors.types.feed_item_set_link_error import (
    FeedItemSetLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.feed_item_target_error import (
    FeedItemTargetErrorEnum,
)
from google.ads.googleads.v16.errors.types.feed_item_validation_error import (
    FeedItemValidationErrorEnum,
)
from google.ads.googleads.v16.errors.types.feed_mapping_error import (
    FeedMappingErrorEnum,
)
from google.ads.googleads.v16.errors.types.field_error import FieldErrorEnum
from google.ads.googleads.v16.errors.types.field_mask_error import FieldMaskErrorEnum
from google.ads.googleads.v16.errors.types.function_error import FunctionErrorEnum
from google.ads.googleads.v16.errors.types.function_parsing_error import (
    FunctionParsingErrorEnum,
)
from google.ads.googleads.v16.errors.types.geo_target_constant_suggestion_error import (
    GeoTargetConstantSuggestionErrorEnum,
)
from google.ads.googleads.v16.errors.types.header_error import HeaderErrorEnum
from google.ads.googleads.v16.errors.types.id_error import IdErrorEnum
from google.ads.googleads.v16.errors.types.identity_verification_error import (
    IdentityVerificationErrorEnum,
)
from google.ads.googleads.v16.errors.types.image_error import ImageErrorEnum
from google.ads.googleads.v16.errors.types.internal_error import InternalErrorEnum
from google.ads.googleads.v16.errors.types.invoice_error import InvoiceErrorEnum
from google.ads.googleads.v16.errors.types.keyword_plan_ad_group_error import (
    KeywordPlanAdGroupErrorEnum,
)
from google.ads.googleads.v16.errors.types.keyword_plan_ad_group_keyword_error import (
    KeywordPlanAdGroupKeywordErrorEnum,
)
from google.ads.googleads.v16.errors.types.keyword_plan_campaign_error import (
    KeywordPlanCampaignErrorEnum,
)
from google.ads.googleads.v16.errors.types.keyword_plan_campaign_keyword_error import (
    KeywordPlanCampaignKeywordErrorEnum,
)
from google.ads.googleads.v16.errors.types.keyword_plan_error import (
    KeywordPlanErrorEnum,
)
from google.ads.googleads.v16.errors.types.keyword_plan_idea_error import (
    KeywordPlanIdeaErrorEnum,
)
from google.ads.googleads.v16.errors.types.label_error import LabelErrorEnum
from google.ads.googleads.v16.errors.types.language_code_error import (
    LanguageCodeErrorEnum,
)
from google.ads.googleads.v16.errors.types.list_operation_error import (
    ListOperationErrorEnum,
)
from google.ads.googleads.v16.errors.types.manager_link_error import (
    ManagerLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.media_bundle_error import (
    MediaBundleErrorEnum,
)
from google.ads.googleads.v16.errors.types.media_file_error import MediaFileErrorEnum
from google.ads.googleads.v16.errors.types.media_upload_error import (
    MediaUploadErrorEnum,
)
from google.ads.googleads.v16.errors.types.merchant_center_error import (
    MerchantCenterErrorEnum,
)
from google.ads.googleads.v16.errors.types.multiplier_error import MultiplierErrorEnum
from google.ads.googleads.v16.errors.types.mutate_error import MutateErrorEnum
from google.ads.googleads.v16.errors.types.new_resource_creation_error import (
    NewResourceCreationErrorEnum,
)
from google.ads.googleads.v16.errors.types.not_allowlisted_error import (
    NotAllowlistedErrorEnum,
)
from google.ads.googleads.v16.errors.types.not_empty_error import NotEmptyErrorEnum
from google.ads.googleads.v16.errors.types.null_error import NullErrorEnum
from google.ads.googleads.v16.errors.types.offline_user_data_job_error import (
    OfflineUserDataJobErrorEnum,
)
from google.ads.googleads.v16.errors.types.operation_access_denied_error import (
    OperationAccessDeniedErrorEnum,
)
from google.ads.googleads.v16.errors.types.operator_error import OperatorErrorEnum
from google.ads.googleads.v16.errors.types.partial_failure_error import (
    PartialFailureErrorEnum,
)
from google.ads.googleads.v16.errors.types.payments_account_error import (
    PaymentsAccountErrorEnum,
)
from google.ads.googleads.v16.errors.types.policy_finding_error import (
    PolicyFindingErrorEnum,
)
from google.ads.googleads.v16.errors.types.policy_validation_parameter_error import (
    PolicyValidationParameterErrorEnum,
)
from google.ads.googleads.v16.errors.types.policy_violation_error import (
    PolicyViolationErrorEnum,
)
from google.ads.googleads.v16.errors.types.product_link_error import (
    ProductLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.product_link_invitation_error import (
    ProductLinkInvitationErrorEnum,
)
from google.ads.googleads.v16.errors.types.query_error import QueryErrorEnum
from google.ads.googleads.v16.errors.types.quota_error import QuotaErrorEnum
from google.ads.googleads.v16.errors.types.range_error import RangeErrorEnum
from google.ads.googleads.v16.errors.types.reach_plan_error import ReachPlanErrorEnum
from google.ads.googleads.v16.errors.types.recommendation_error import (
    RecommendationErrorEnum,
)
from google.ads.googleads.v16.errors.types.recommendation_subscription_error import (
    RecommendationSubscriptionErrorEnum,
)
from google.ads.googleads.v16.errors.types.region_code_error import RegionCodeErrorEnum
from google.ads.googleads.v16.errors.types.request_error import RequestErrorEnum
from google.ads.googleads.v16.errors.types.resource_access_denied_error import (
    ResourceAccessDeniedErrorEnum,
)
from google.ads.googleads.v16.errors.types.resource_count_limit_exceeded_error import (
    ResourceCountLimitExceededErrorEnum,
)
from google.ads.googleads.v16.errors.types.search_term_insight_error import (
    SearchTermInsightErrorEnum,
)
from google.ads.googleads.v16.errors.types.setting_error import SettingErrorEnum
from google.ads.googleads.v16.errors.types.shared_criterion_error import (
    SharedCriterionErrorEnum,
)
from google.ads.googleads.v16.errors.types.shared_set_error import SharedSetErrorEnum
from google.ads.googleads.v16.errors.types.size_limit_error import SizeLimitErrorEnum
from google.ads.googleads.v16.errors.types.smart_campaign_error import (
    SmartCampaignErrorEnum,
)
from google.ads.googleads.v16.errors.types.string_format_error import (
    StringFormatErrorEnum,
)
from google.ads.googleads.v16.errors.types.string_length_error import (
    StringLengthErrorEnum,
)
from google.ads.googleads.v16.errors.types.third_party_app_analytics_link_error import (
    ThirdPartyAppAnalyticsLinkErrorEnum,
)
from google.ads.googleads.v16.errors.types.time_zone_error import TimeZoneErrorEnum
from google.ads.googleads.v16.errors.types.url_field_error import UrlFieldErrorEnum
from google.ads.googleads.v16.errors.types.user_data_error import UserDataErrorEnum
from google.ads.googleads.v16.errors.types.user_list_error import UserListErrorEnum
from google.ads.googleads.v16.errors.types.youtube_video_registration_error import (
    YoutubeVideoRegistrationErrorEnum,
)

_M = TypeVar("_M")

class ErrorCode(proto.Message):
    request_error: RequestErrorEnum.RequestError
    bidding_strategy_error: BiddingStrategyErrorEnum.BiddingStrategyError
    url_field_error: UrlFieldErrorEnum.UrlFieldError
    list_operation_error: ListOperationErrorEnum.ListOperationError
    query_error: QueryErrorEnum.QueryError
    mutate_error: MutateErrorEnum.MutateError
    field_mask_error: FieldMaskErrorEnum.FieldMaskError
    authorization_error: AuthorizationErrorEnum.AuthorizationError
    internal_error: InternalErrorEnum.InternalError
    quota_error: QuotaErrorEnum.QuotaError
    ad_error: AdErrorEnum.AdError
    ad_group_error: AdGroupErrorEnum.AdGroupError
    campaign_budget_error: CampaignBudgetErrorEnum.CampaignBudgetError
    campaign_error: CampaignErrorEnum.CampaignError
    authentication_error: AuthenticationErrorEnum.AuthenticationError
    ad_group_criterion_customizer_error: (
        AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError
    )
    ad_group_criterion_error: AdGroupCriterionErrorEnum.AdGroupCriterionError
    ad_group_customizer_error: AdGroupCustomizerErrorEnum.AdGroupCustomizerError
    ad_customizer_error: AdCustomizerErrorEnum.AdCustomizerError
    ad_group_ad_error: AdGroupAdErrorEnum.AdGroupAdError
    ad_sharing_error: AdSharingErrorEnum.AdSharingError
    adx_error: AdxErrorEnum.AdxError
    asset_error: AssetErrorEnum.AssetError
    asset_group_asset_error: AssetGroupAssetErrorEnum.AssetGroupAssetError
    asset_group_listing_group_filter_error: (
        AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    )
    asset_group_error: AssetGroupErrorEnum.AssetGroupError
    asset_set_asset_error: AssetSetAssetErrorEnum.AssetSetAssetError
    asset_set_link_error: AssetSetLinkErrorEnum.AssetSetLinkError
    asset_set_error: AssetSetErrorEnum.AssetSetError
    bidding_error: BiddingErrorEnum.BiddingError
    campaign_criterion_error: CampaignCriterionErrorEnum.CampaignCriterionError
    campaign_conversion_goal_error: (
        CampaignConversionGoalErrorEnum.CampaignConversionGoalError
    )
    campaign_customizer_error: CampaignCustomizerErrorEnum.CampaignCustomizerError
    collection_size_error: CollectionSizeErrorEnum.CollectionSizeError
    conversion_goal_campaign_config_error: (
        ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    )
    country_code_error: CountryCodeErrorEnum.CountryCodeError
    criterion_error: CriterionErrorEnum.CriterionError
    custom_conversion_goal_error: (
        CustomConversionGoalErrorEnum.CustomConversionGoalError
    )
    customer_customizer_error: CustomerCustomizerErrorEnum.CustomerCustomizerError
    customer_error: CustomerErrorEnum.CustomerError
    customizer_attribute_error: CustomizerAttributeErrorEnum.CustomizerAttributeError
    date_error: DateErrorEnum.DateError
    date_range_error: DateRangeErrorEnum.DateRangeError
    distinct_error: DistinctErrorEnum.DistinctError
    feed_attribute_reference_error: (
        FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
    )
    function_error: FunctionErrorEnum.FunctionError
    function_parsing_error: FunctionParsingErrorEnum.FunctionParsingError
    id_error: IdErrorEnum.IdError
    image_error: ImageErrorEnum.ImageError
    language_code_error: LanguageCodeErrorEnum.LanguageCodeError
    media_bundle_error: MediaBundleErrorEnum.MediaBundleError
    media_upload_error: MediaUploadErrorEnum.MediaUploadError
    media_file_error: MediaFileErrorEnum.MediaFileError
    merchant_center_error: MerchantCenterErrorEnum.MerchantCenterError
    multiplier_error: MultiplierErrorEnum.MultiplierError
    new_resource_creation_error: NewResourceCreationErrorEnum.NewResourceCreationError
    not_empty_error: NotEmptyErrorEnum.NotEmptyError
    null_error: NullErrorEnum.NullError
    operator_error: OperatorErrorEnum.OperatorError
    range_error: RangeErrorEnum.RangeError
    recommendation_error: RecommendationErrorEnum.RecommendationError
    recommendation_subscription_error: (
        RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError
    )
    region_code_error: RegionCodeErrorEnum.RegionCodeError
    setting_error: SettingErrorEnum.SettingError
    string_format_error: StringFormatErrorEnum.StringFormatError
    string_length_error: StringLengthErrorEnum.StringLengthError
    operation_access_denied_error: (
        OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    )
    resource_access_denied_error: (
        ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError
    )
    resource_count_limit_exceeded_error: (
        ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    )
    youtube_video_registration_error: (
        YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    )
    ad_group_bid_modifier_error: AdGroupBidModifierErrorEnum.AdGroupBidModifierError
    context_error: ContextErrorEnum.ContextError
    field_error: FieldErrorEnum.FieldError
    shared_set_error: SharedSetErrorEnum.SharedSetError
    shared_criterion_error: SharedCriterionErrorEnum.SharedCriterionError
    campaign_shared_set_error: CampaignSharedSetErrorEnum.CampaignSharedSetError
    conversion_action_error: ConversionActionErrorEnum.ConversionActionError
    conversion_adjustment_upload_error: (
        ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    )
    conversion_custom_variable_error: (
        ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    )
    conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError
    conversion_value_rule_error: ConversionValueRuleErrorEnum.ConversionValueRuleError
    conversion_value_rule_set_error: (
        ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    )
    header_error: HeaderErrorEnum.HeaderError
    database_error: DatabaseErrorEnum.DatabaseError
    policy_finding_error: PolicyFindingErrorEnum.PolicyFindingError
    enum_error: EnumErrorEnum.EnumError
    keyword_plan_error: KeywordPlanErrorEnum.KeywordPlanError
    keyword_plan_campaign_error: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    keyword_plan_campaign_keyword_error: (
        KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError
    )
    keyword_plan_ad_group_error: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError
    keyword_plan_ad_group_keyword_error: (
        KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    )
    keyword_plan_idea_error: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError
    account_budget_proposal_error: (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    )
    user_list_error: UserListErrorEnum.UserListError
    change_event_error: ChangeEventErrorEnum.ChangeEventError
    change_status_error: ChangeStatusErrorEnum.ChangeStatusError
    feed_error: FeedErrorEnum.FeedError
    geo_target_constant_suggestion_error: (
        GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
    )
    campaign_draft_error: CampaignDraftErrorEnum.CampaignDraftError
    feed_item_error: FeedItemErrorEnum.FeedItemError
    label_error: LabelErrorEnum.LabelError
    billing_setup_error: BillingSetupErrorEnum.BillingSetupError
    customer_client_link_error: CustomerClientLinkErrorEnum.CustomerClientLinkError
    customer_manager_link_error: CustomerManagerLinkErrorEnum.CustomerManagerLinkError
    feed_mapping_error: FeedMappingErrorEnum.FeedMappingError
    customer_feed_error: CustomerFeedErrorEnum.CustomerFeedError
    ad_group_feed_error: AdGroupFeedErrorEnum.AdGroupFeedError
    campaign_feed_error: CampaignFeedErrorEnum.CampaignFeedError
    custom_interest_error: CustomInterestErrorEnum.CustomInterestError
    campaign_experiment_error: CampaignExperimentErrorEnum.CampaignExperimentError
    extension_feed_item_error: ExtensionFeedItemErrorEnum.ExtensionFeedItemError
    ad_parameter_error: AdParameterErrorEnum.AdParameterError
    feed_item_validation_error: FeedItemValidationErrorEnum.FeedItemValidationError
    extension_setting_error: ExtensionSettingErrorEnum.ExtensionSettingError
    feed_item_set_error: FeedItemSetErrorEnum.FeedItemSetError
    feed_item_set_link_error: FeedItemSetLinkErrorEnum.FeedItemSetLinkError
    feed_item_target_error: FeedItemTargetErrorEnum.FeedItemTargetError
    policy_violation_error: PolicyViolationErrorEnum.PolicyViolationError
    partial_failure_error: PartialFailureErrorEnum.PartialFailureError
    policy_validation_parameter_error: (
        PolicyValidationParameterErrorEnum.PolicyValidationParameterError
    )
    size_limit_error: SizeLimitErrorEnum.SizeLimitError
    offline_user_data_job_error: OfflineUserDataJobErrorEnum.OfflineUserDataJobError
    not_allowlisted_error: NotAllowlistedErrorEnum.NotAllowlistedError
    manager_link_error: ManagerLinkErrorEnum.ManagerLinkError
    currency_code_error: CurrencyCodeErrorEnum.CurrencyCodeError
    experiment_error: ExperimentErrorEnum.ExperimentError
    access_invitation_error: AccessInvitationErrorEnum.AccessInvitationError
    reach_plan_error: ReachPlanErrorEnum.ReachPlanError
    invoice_error: InvoiceErrorEnum.InvoiceError
    payments_account_error: PaymentsAccountErrorEnum.PaymentsAccountError
    time_zone_error: TimeZoneErrorEnum.TimeZoneError
    asset_link_error: AssetLinkErrorEnum.AssetLinkError
    user_data_error: UserDataErrorEnum.UserDataError
    batch_job_error: BatchJobErrorEnum.BatchJobError
    account_link_error: AccountLinkErrorEnum.AccountLinkError
    third_party_app_analytics_link_error: (
        ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    )
    customer_user_access_error: CustomerUserAccessErrorEnum.CustomerUserAccessError
    custom_audience_error: CustomAudienceErrorEnum.CustomAudienceError
    audience_error: AudienceErrorEnum.AudienceError
    search_term_insight_error: SearchTermInsightErrorEnum.SearchTermInsightError
    smart_campaign_error: SmartCampaignErrorEnum.SmartCampaignError
    experiment_arm_error: ExperimentArmErrorEnum.ExperimentArmError
    audience_insights_error: AudienceInsightsErrorEnum.AudienceInsightsError
    product_link_error: ProductLinkErrorEnum.ProductLinkError
    customer_sk_ad_network_conversion_value_schema_error: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError
    currency_error: CurrencyErrorEnum.CurrencyError
    asset_group_signal_error: AssetGroupSignalErrorEnum.AssetGroupSignalError
    product_link_invitation_error: (
        ProductLinkInvitationErrorEnum.ProductLinkInvitationError
    )
    customer_lifecycle_goal_error: (
        CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError
    )
    campaign_lifecycle_goal_error: (
        CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError
    )
    identity_verification_error: IdentityVerificationErrorEnum.IdentityVerificationError
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        request_error: RequestErrorEnum.RequestError = ...,
        bidding_strategy_error: BiddingStrategyErrorEnum.BiddingStrategyError = ...,
        url_field_error: UrlFieldErrorEnum.UrlFieldError = ...,
        list_operation_error: ListOperationErrorEnum.ListOperationError = ...,
        query_error: QueryErrorEnum.QueryError = ...,
        mutate_error: MutateErrorEnum.MutateError = ...,
        field_mask_error: FieldMaskErrorEnum.FieldMaskError = ...,
        authorization_error: AuthorizationErrorEnum.AuthorizationError = ...,
        internal_error: InternalErrorEnum.InternalError = ...,
        quota_error: QuotaErrorEnum.QuotaError = ...,
        ad_error: AdErrorEnum.AdError = ...,
        ad_group_error: AdGroupErrorEnum.AdGroupError = ...,
        campaign_budget_error: CampaignBudgetErrorEnum.CampaignBudgetError = ...,
        campaign_error: CampaignErrorEnum.CampaignError = ...,
        authentication_error: AuthenticationErrorEnum.AuthenticationError = ...,
        ad_group_criterion_customizer_error: AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError = ...,
        ad_group_criterion_error: AdGroupCriterionErrorEnum.AdGroupCriterionError = ...,
        ad_group_customizer_error: AdGroupCustomizerErrorEnum.AdGroupCustomizerError = ...,
        ad_customizer_error: AdCustomizerErrorEnum.AdCustomizerError = ...,
        ad_group_ad_error: AdGroupAdErrorEnum.AdGroupAdError = ...,
        ad_sharing_error: AdSharingErrorEnum.AdSharingError = ...,
        adx_error: AdxErrorEnum.AdxError = ...,
        asset_error: AssetErrorEnum.AssetError = ...,
        asset_group_asset_error: AssetGroupAssetErrorEnum.AssetGroupAssetError = ...,
        asset_group_listing_group_filter_error: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError = ...,
        asset_group_error: AssetGroupErrorEnum.AssetGroupError = ...,
        asset_set_asset_error: AssetSetAssetErrorEnum.AssetSetAssetError = ...,
        asset_set_link_error: AssetSetLinkErrorEnum.AssetSetLinkError = ...,
        asset_set_error: AssetSetErrorEnum.AssetSetError = ...,
        bidding_error: BiddingErrorEnum.BiddingError = ...,
        campaign_criterion_error: CampaignCriterionErrorEnum.CampaignCriterionError = ...,
        campaign_conversion_goal_error: CampaignConversionGoalErrorEnum.CampaignConversionGoalError = ...,
        campaign_customizer_error: CampaignCustomizerErrorEnum.CampaignCustomizerError = ...,
        collection_size_error: CollectionSizeErrorEnum.CollectionSizeError = ...,
        conversion_goal_campaign_config_error: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError = ...,
        country_code_error: CountryCodeErrorEnum.CountryCodeError = ...,
        criterion_error: CriterionErrorEnum.CriterionError = ...,
        custom_conversion_goal_error: CustomConversionGoalErrorEnum.CustomConversionGoalError = ...,
        customer_customizer_error: CustomerCustomizerErrorEnum.CustomerCustomizerError = ...,
        customer_error: CustomerErrorEnum.CustomerError = ...,
        customizer_attribute_error: CustomizerAttributeErrorEnum.CustomizerAttributeError = ...,
        date_error: DateErrorEnum.DateError = ...,
        date_range_error: DateRangeErrorEnum.DateRangeError = ...,
        distinct_error: DistinctErrorEnum.DistinctError = ...,
        feed_attribute_reference_error: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError = ...,
        function_error: FunctionErrorEnum.FunctionError = ...,
        function_parsing_error: FunctionParsingErrorEnum.FunctionParsingError = ...,
        id_error: IdErrorEnum.IdError = ...,
        image_error: ImageErrorEnum.ImageError = ...,
        language_code_error: LanguageCodeErrorEnum.LanguageCodeError = ...,
        media_bundle_error: MediaBundleErrorEnum.MediaBundleError = ...,
        media_upload_error: MediaUploadErrorEnum.MediaUploadError = ...,
        media_file_error: MediaFileErrorEnum.MediaFileError = ...,
        merchant_center_error: MerchantCenterErrorEnum.MerchantCenterError = ...,
        multiplier_error: MultiplierErrorEnum.MultiplierError = ...,
        new_resource_creation_error: NewResourceCreationErrorEnum.NewResourceCreationError = ...,
        not_empty_error: NotEmptyErrorEnum.NotEmptyError = ...,
        null_error: NullErrorEnum.NullError = ...,
        operator_error: OperatorErrorEnum.OperatorError = ...,
        range_error: RangeErrorEnum.RangeError = ...,
        recommendation_error: RecommendationErrorEnum.RecommendationError = ...,
        recommendation_subscription_error: RecommendationSubscriptionErrorEnum.RecommendationSubscriptionError = ...,
        region_code_error: RegionCodeErrorEnum.RegionCodeError = ...,
        setting_error: SettingErrorEnum.SettingError = ...,
        string_format_error: StringFormatErrorEnum.StringFormatError = ...,
        string_length_error: StringLengthErrorEnum.StringLengthError = ...,
        operation_access_denied_error: OperationAccessDeniedErrorEnum.OperationAccessDeniedError = ...,
        resource_access_denied_error: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError = ...,
        resource_count_limit_exceeded_error: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError = ...,
        youtube_video_registration_error: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError = ...,
        ad_group_bid_modifier_error: AdGroupBidModifierErrorEnum.AdGroupBidModifierError = ...,
        context_error: ContextErrorEnum.ContextError = ...,
        field_error: FieldErrorEnum.FieldError = ...,
        shared_set_error: SharedSetErrorEnum.SharedSetError = ...,
        shared_criterion_error: SharedCriterionErrorEnum.SharedCriterionError = ...,
        campaign_shared_set_error: CampaignSharedSetErrorEnum.CampaignSharedSetError = ...,
        conversion_action_error: ConversionActionErrorEnum.ConversionActionError = ...,
        conversion_adjustment_upload_error: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError = ...,
        conversion_custom_variable_error: ConversionCustomVariableErrorEnum.ConversionCustomVariableError = ...,
        conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError = ...,
        conversion_value_rule_error: ConversionValueRuleErrorEnum.ConversionValueRuleError = ...,
        conversion_value_rule_set_error: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError = ...,
        header_error: HeaderErrorEnum.HeaderError = ...,
        database_error: DatabaseErrorEnum.DatabaseError = ...,
        policy_finding_error: PolicyFindingErrorEnum.PolicyFindingError = ...,
        enum_error: EnumErrorEnum.EnumError = ...,
        keyword_plan_error: KeywordPlanErrorEnum.KeywordPlanError = ...,
        keyword_plan_campaign_error: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError = ...,
        keyword_plan_campaign_keyword_error: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError = ...,
        keyword_plan_ad_group_error: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError = ...,
        keyword_plan_ad_group_keyword_error: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError = ...,
        keyword_plan_idea_error: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError = ...,
        account_budget_proposal_error: AccountBudgetProposalErrorEnum.AccountBudgetProposalError = ...,
        user_list_error: UserListErrorEnum.UserListError = ...,
        change_event_error: ChangeEventErrorEnum.ChangeEventError = ...,
        change_status_error: ChangeStatusErrorEnum.ChangeStatusError = ...,
        feed_error: FeedErrorEnum.FeedError = ...,
        geo_target_constant_suggestion_error: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError = ...,
        campaign_draft_error: CampaignDraftErrorEnum.CampaignDraftError = ...,
        feed_item_error: FeedItemErrorEnum.FeedItemError = ...,
        label_error: LabelErrorEnum.LabelError = ...,
        billing_setup_error: BillingSetupErrorEnum.BillingSetupError = ...,
        customer_client_link_error: CustomerClientLinkErrorEnum.CustomerClientLinkError = ...,
        customer_manager_link_error: CustomerManagerLinkErrorEnum.CustomerManagerLinkError = ...,
        feed_mapping_error: FeedMappingErrorEnum.FeedMappingError = ...,
        customer_feed_error: CustomerFeedErrorEnum.CustomerFeedError = ...,
        ad_group_feed_error: AdGroupFeedErrorEnum.AdGroupFeedError = ...,
        campaign_feed_error: CampaignFeedErrorEnum.CampaignFeedError = ...,
        custom_interest_error: CustomInterestErrorEnum.CustomInterestError = ...,
        campaign_experiment_error: CampaignExperimentErrorEnum.CampaignExperimentError = ...,
        extension_feed_item_error: ExtensionFeedItemErrorEnum.ExtensionFeedItemError = ...,
        ad_parameter_error: AdParameterErrorEnum.AdParameterError = ...,
        feed_item_validation_error: FeedItemValidationErrorEnum.FeedItemValidationError = ...,
        extension_setting_error: ExtensionSettingErrorEnum.ExtensionSettingError = ...,
        feed_item_set_error: FeedItemSetErrorEnum.FeedItemSetError = ...,
        feed_item_set_link_error: FeedItemSetLinkErrorEnum.FeedItemSetLinkError = ...,
        feed_item_target_error: FeedItemTargetErrorEnum.FeedItemTargetError = ...,
        policy_violation_error: PolicyViolationErrorEnum.PolicyViolationError = ...,
        partial_failure_error: PartialFailureErrorEnum.PartialFailureError = ...,
        policy_validation_parameter_error: PolicyValidationParameterErrorEnum.PolicyValidationParameterError = ...,
        size_limit_error: SizeLimitErrorEnum.SizeLimitError = ...,
        offline_user_data_job_error: OfflineUserDataJobErrorEnum.OfflineUserDataJobError = ...,
        not_allowlisted_error: NotAllowlistedErrorEnum.NotAllowlistedError = ...,
        manager_link_error: ManagerLinkErrorEnum.ManagerLinkError = ...,
        currency_code_error: CurrencyCodeErrorEnum.CurrencyCodeError = ...,
        experiment_error: ExperimentErrorEnum.ExperimentError = ...,
        access_invitation_error: AccessInvitationErrorEnum.AccessInvitationError = ...,
        reach_plan_error: ReachPlanErrorEnum.ReachPlanError = ...,
        invoice_error: InvoiceErrorEnum.InvoiceError = ...,
        payments_account_error: PaymentsAccountErrorEnum.PaymentsAccountError = ...,
        time_zone_error: TimeZoneErrorEnum.TimeZoneError = ...,
        asset_link_error: AssetLinkErrorEnum.AssetLinkError = ...,
        user_data_error: UserDataErrorEnum.UserDataError = ...,
        batch_job_error: BatchJobErrorEnum.BatchJobError = ...,
        account_link_error: AccountLinkErrorEnum.AccountLinkError = ...,
        third_party_app_analytics_link_error: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError = ...,
        customer_user_access_error: CustomerUserAccessErrorEnum.CustomerUserAccessError = ...,
        custom_audience_error: CustomAudienceErrorEnum.CustomAudienceError = ...,
        audience_error: AudienceErrorEnum.AudienceError = ...,
        search_term_insight_error: SearchTermInsightErrorEnum.SearchTermInsightError = ...,
        smart_campaign_error: SmartCampaignErrorEnum.SmartCampaignError = ...,
        experiment_arm_error: ExperimentArmErrorEnum.ExperimentArmError = ...,
        audience_insights_error: AudienceInsightsErrorEnum.AudienceInsightsError = ...,
        product_link_error: ProductLinkErrorEnum.ProductLinkError = ...,
        customer_sk_ad_network_conversion_value_schema_error: CustomerSkAdNetworkConversionValueSchemaErrorEnum.CustomerSkAdNetworkConversionValueSchemaError = ...,
        currency_error: CurrencyErrorEnum.CurrencyError = ...,
        asset_group_signal_error: AssetGroupSignalErrorEnum.AssetGroupSignalError = ...,
        product_link_invitation_error: ProductLinkInvitationErrorEnum.ProductLinkInvitationError = ...,
        customer_lifecycle_goal_error: CustomerLifecycleGoalErrorEnum.CustomerLifecycleGoalError = ...,
        campaign_lifecycle_goal_error: CampaignLifecycleGoalErrorEnum.CampaignLifecycleGoalError = ...,
        identity_verification_error: IdentityVerificationErrorEnum.IdentityVerificationError = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "request_error",
            "bidding_strategy_error",
            "url_field_error",
            "list_operation_error",
            "query_error",
            "mutate_error",
            "field_mask_error",
            "authorization_error",
            "internal_error",
            "quota_error",
            "ad_error",
            "ad_group_error",
            "campaign_budget_error",
            "campaign_error",
            "authentication_error",
            "ad_group_criterion_customizer_error",
            "ad_group_criterion_error",
            "ad_group_customizer_error",
            "ad_customizer_error",
            "ad_group_ad_error",
            "ad_sharing_error",
            "adx_error",
            "asset_error",
            "asset_group_asset_error",
            "asset_group_listing_group_filter_error",
            "asset_group_error",
            "asset_set_asset_error",
            "asset_set_link_error",
            "asset_set_error",
            "bidding_error",
            "campaign_criterion_error",
            "campaign_conversion_goal_error",
            "campaign_customizer_error",
            "collection_size_error",
            "conversion_goal_campaign_config_error",
            "country_code_error",
            "criterion_error",
            "custom_conversion_goal_error",
            "customer_customizer_error",
            "customer_error",
            "customizer_attribute_error",
            "date_error",
            "date_range_error",
            "distinct_error",
            "feed_attribute_reference_error",
            "function_error",
            "function_parsing_error",
            "id_error",
            "image_error",
            "language_code_error",
            "media_bundle_error",
            "media_upload_error",
            "media_file_error",
            "merchant_center_error",
            "multiplier_error",
            "new_resource_creation_error",
            "not_empty_error",
            "null_error",
            "operator_error",
            "range_error",
            "recommendation_error",
            "recommendation_subscription_error",
            "region_code_error",
            "setting_error",
            "string_format_error",
            "string_length_error",
            "operation_access_denied_error",
            "resource_access_denied_error",
            "resource_count_limit_exceeded_error",
            "youtube_video_registration_error",
            "ad_group_bid_modifier_error",
            "context_error",
            "field_error",
            "shared_set_error",
            "shared_criterion_error",
            "campaign_shared_set_error",
            "conversion_action_error",
            "conversion_adjustment_upload_error",
            "conversion_custom_variable_error",
            "conversion_upload_error",
            "conversion_value_rule_error",
            "conversion_value_rule_set_error",
            "header_error",
            "database_error",
            "policy_finding_error",
            "enum_error",
            "keyword_plan_error",
            "keyword_plan_campaign_error",
            "keyword_plan_campaign_keyword_error",
            "keyword_plan_ad_group_error",
            "keyword_plan_ad_group_keyword_error",
            "keyword_plan_idea_error",
            "account_budget_proposal_error",
            "user_list_error",
            "change_event_error",
            "change_status_error",
            "feed_error",
            "geo_target_constant_suggestion_error",
            "campaign_draft_error",
            "feed_item_error",
            "label_error",
            "billing_setup_error",
            "customer_client_link_error",
            "customer_manager_link_error",
            "feed_mapping_error",
            "customer_feed_error",
            "ad_group_feed_error",
            "campaign_feed_error",
            "custom_interest_error",
            "campaign_experiment_error",
            "extension_feed_item_error",
            "ad_parameter_error",
            "feed_item_validation_error",
            "extension_setting_error",
            "feed_item_set_error",
            "feed_item_set_link_error",
            "feed_item_target_error",
            "policy_violation_error",
            "partial_failure_error",
            "policy_validation_parameter_error",
            "size_limit_error",
            "offline_user_data_job_error",
            "not_allowlisted_error",
            "manager_link_error",
            "currency_code_error",
            "experiment_error",
            "access_invitation_error",
            "reach_plan_error",
            "invoice_error",
            "payments_account_error",
            "time_zone_error",
            "asset_link_error",
            "user_data_error",
            "batch_job_error",
            "account_link_error",
            "third_party_app_analytics_link_error",
            "customer_user_access_error",
            "custom_audience_error",
            "audience_error",
            "search_term_insight_error",
            "smart_campaign_error",
            "experiment_arm_error",
            "audience_insights_error",
            "product_link_error",
            "customer_sk_ad_network_conversion_value_schema_error",
            "currency_error",
            "asset_group_signal_error",
            "product_link_invitation_error",
            "customer_lifecycle_goal_error",
            "campaign_lifecycle_goal_error",
            "identity_verification_error",
        ],
    ) -> bool: ...

class ErrorDetails(proto.Message):
    unpublished_error_code: str
    policy_violation_details: PolicyViolationDetails
    policy_finding_details: PolicyFindingDetails
    quota_error_details: QuotaErrorDetails
    resource_count_details: ResourceCountDetails
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        unpublished_error_code: str = ...,
        policy_violation_details: PolicyViolationDetails = ...,
        policy_finding_details: PolicyFindingDetails = ...,
        quota_error_details: QuotaErrorDetails = ...,
        resource_count_details: ResourceCountDetails = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "unpublished_error_code",
            "policy_violation_details",
            "policy_finding_details",
            "quota_error_details",
            "resource_count_details",
        ],
    ) -> bool: ...

class ErrorLocation(proto.Message):
    class FieldPathElement(proto.Message):
        field_name: str
        index: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            field_name: str = ...,
            index: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["field_name", "index"]
        ) -> bool: ...

    field_path_elements: MutableSequence[ErrorLocation.FieldPathElement]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        field_path_elements: MutableSequence[ErrorLocation.FieldPathElement] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["field_path_elements"]
    ) -> bool: ...

class GoogleAdsError(proto.Message):
    error_code: ErrorCode
    message: str
    trigger: Value
    location: ErrorLocation
    details: ErrorDetails
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        error_code: ErrorCode = ...,
        message: str = ...,
        trigger: Value = ...,
        location: ErrorLocation = ...,
        details: ErrorDetails = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["error_code", "message", "trigger", "location", "details"]
    ) -> bool: ...

class GoogleAdsFailure(proto.Message):
    errors: MutableSequence[GoogleAdsError]
    request_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        errors: MutableSequence[GoogleAdsError] = ...,
        request_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["errors", "request_id"]
    ) -> bool: ...

class PolicyFindingDetails(proto.Message):
    policy_topic_entries: MutableSequence[PolicyTopicEntry]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        policy_topic_entries: MutableSequence[PolicyTopicEntry] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["policy_topic_entries"]
    ) -> bool: ...

class PolicyViolationDetails(proto.Message):
    external_policy_description: str
    key: PolicyViolationKey
    external_policy_name: str
    is_exemptible: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        external_policy_description: str = ...,
        key: PolicyViolationKey = ...,
        external_policy_name: str = ...,
        is_exemptible: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "external_policy_description",
            "key",
            "external_policy_name",
            "is_exemptible",
        ],
    ) -> bool: ...

class QuotaErrorDetails(proto.Message):
    class QuotaRateScope(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACCOUNT = 2
        DEVELOPER = 3

    rate_scope: QuotaErrorDetails.QuotaRateScope
    rate_name: str
    retry_delay: Duration
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        rate_scope: QuotaErrorDetails.QuotaRateScope = ...,
        rate_name: str = ...,
        retry_delay: Duration = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["rate_scope", "rate_name", "retry_delay"]
    ) -> bool: ...

class ResourceCountDetails(proto.Message):
    enclosing_id: str
    enclosing_resource: str
    limit: int
    limit_type: ResourceLimitTypeEnum.ResourceLimitType
    existing_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        enclosing_id: str = ...,
        enclosing_resource: str = ...,
        limit: int = ...,
        limit_type: ResourceLimitTypeEnum.ResourceLimitType = ...,
        existing_count: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "enclosing_id",
            "enclosing_resource",
            "limit",
            "limit_type",
            "existing_count",
        ],
    ) -> bool: ...
