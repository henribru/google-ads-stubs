from typing import Any

import proto
from google.protobuf.duration_pb2 import Duration

from google.ads.googleads.v11.common.types.policy import (
    PolicyTopicEntry,
    PolicyViolationKey,
)
from google.ads.googleads.v11.common.types.value import Value
from google.ads.googleads.v11.enums.types.resource_limit_type import (
    ResourceLimitTypeEnum,
)
from google.ads.googleads.v11.errors.types.access_invitation_error import (
    AccessInvitationErrorEnum,
)
from google.ads.googleads.v11.errors.types.account_budget_proposal_error import (
    AccountBudgetProposalErrorEnum,
)
from google.ads.googleads.v11.errors.types.account_link_error import (
    AccountLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_customizer_error import (
    AdCustomizerErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_error import AdErrorEnum
from google.ads.googleads.v11.errors.types.ad_group_ad_error import AdGroupAdErrorEnum
from google.ads.googleads.v11.errors.types.ad_group_bid_modifier_error import (
    AdGroupBidModifierErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_group_criterion_customizer_error import (
    AdGroupCriterionCustomizerErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_group_criterion_error import (
    AdGroupCriterionErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_group_customizer_error import (
    AdGroupCustomizerErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_group_error import AdGroupErrorEnum
from google.ads.googleads.v11.errors.types.ad_group_feed_error import (
    AdGroupFeedErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_parameter_error import (
    AdParameterErrorEnum,
)
from google.ads.googleads.v11.errors.types.ad_sharing_error import AdSharingErrorEnum
from google.ads.googleads.v11.errors.types.adx_error import AdxErrorEnum
from google.ads.googleads.v11.errors.types.asset_error import AssetErrorEnum
from google.ads.googleads.v11.errors.types.asset_group_asset_error import (
    AssetGroupAssetErrorEnum,
)
from google.ads.googleads.v11.errors.types.asset_group_error import AssetGroupErrorEnum
from google.ads.googleads.v11.errors.types.asset_group_listing_group_filter_error import (
    AssetGroupListingGroupFilterErrorEnum,
)
from google.ads.googleads.v11.errors.types.asset_link_error import AssetLinkErrorEnum
from google.ads.googleads.v11.errors.types.asset_set_asset_error import (
    AssetSetAssetErrorEnum,
)
from google.ads.googleads.v11.errors.types.asset_set_error import AssetSetErrorEnum
from google.ads.googleads.v11.errors.types.asset_set_link_error import (
    AssetSetLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.audience_error import AudienceErrorEnum
from google.ads.googleads.v11.errors.types.audience_insights_error import (
    AudienceInsightsErrorEnum,
)
from google.ads.googleads.v11.errors.types.authentication_error import (
    AuthenticationErrorEnum,
)
from google.ads.googleads.v11.errors.types.authorization_error import (
    AuthorizationErrorEnum,
)
from google.ads.googleads.v11.errors.types.batch_job_error import BatchJobErrorEnum
from google.ads.googleads.v11.errors.types.bidding_error import BiddingErrorEnum
from google.ads.googleads.v11.errors.types.bidding_strategy_error import (
    BiddingStrategyErrorEnum,
)
from google.ads.googleads.v11.errors.types.billing_setup_error import (
    BillingSetupErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_budget_error import (
    CampaignBudgetErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_conversion_goal_error import (
    CampaignConversionGoalErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_criterion_error import (
    CampaignCriterionErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_customizer_error import (
    CampaignCustomizerErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_draft_error import (
    CampaignDraftErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_error import CampaignErrorEnum
from google.ads.googleads.v11.errors.types.campaign_experiment_error import (
    CampaignExperimentErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_feed_error import (
    CampaignFeedErrorEnum,
)
from google.ads.googleads.v11.errors.types.campaign_shared_set_error import (
    CampaignSharedSetErrorEnum,
)
from google.ads.googleads.v11.errors.types.change_event_error import (
    ChangeEventErrorEnum,
)
from google.ads.googleads.v11.errors.types.change_status_error import (
    ChangeStatusErrorEnum,
)
from google.ads.googleads.v11.errors.types.collection_size_error import (
    CollectionSizeErrorEnum,
)
from google.ads.googleads.v11.errors.types.context_error import ContextErrorEnum
from google.ads.googleads.v11.errors.types.conversion_action_error import (
    ConversionActionErrorEnum,
)
from google.ads.googleads.v11.errors.types.conversion_adjustment_upload_error import (
    ConversionAdjustmentUploadErrorEnum,
)
from google.ads.googleads.v11.errors.types.conversion_custom_variable_error import (
    ConversionCustomVariableErrorEnum,
)
from google.ads.googleads.v11.errors.types.conversion_goal_campaign_config_error import (
    ConversionGoalCampaignConfigErrorEnum,
)
from google.ads.googleads.v11.errors.types.conversion_upload_error import (
    ConversionUploadErrorEnum,
)
from google.ads.googleads.v11.errors.types.conversion_value_rule_error import (
    ConversionValueRuleErrorEnum,
)
from google.ads.googleads.v11.errors.types.conversion_value_rule_set_error import (
    ConversionValueRuleSetErrorEnum,
)
from google.ads.googleads.v11.errors.types.country_code_error import (
    CountryCodeErrorEnum,
)
from google.ads.googleads.v11.errors.types.criterion_error import CriterionErrorEnum
from google.ads.googleads.v11.errors.types.currency_code_error import (
    CurrencyCodeErrorEnum,
)
from google.ads.googleads.v11.errors.types.custom_audience_error import (
    CustomAudienceErrorEnum,
)
from google.ads.googleads.v11.errors.types.custom_conversion_goal_error import (
    CustomConversionGoalErrorEnum,
)
from google.ads.googleads.v11.errors.types.custom_interest_error import (
    CustomInterestErrorEnum,
)
from google.ads.googleads.v11.errors.types.customer_client_link_error import (
    CustomerClientLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.customer_customizer_error import (
    CustomerCustomizerErrorEnum,
)
from google.ads.googleads.v11.errors.types.customer_error import CustomerErrorEnum
from google.ads.googleads.v11.errors.types.customer_feed_error import (
    CustomerFeedErrorEnum,
)
from google.ads.googleads.v11.errors.types.customer_manager_link_error import (
    CustomerManagerLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.customer_user_access_error import (
    CustomerUserAccessErrorEnum,
)
from google.ads.googleads.v11.errors.types.customizer_attribute_error import (
    CustomizerAttributeErrorEnum,
)
from google.ads.googleads.v11.errors.types.database_error import DatabaseErrorEnum
from google.ads.googleads.v11.errors.types.date_error import DateErrorEnum
from google.ads.googleads.v11.errors.types.date_range_error import DateRangeErrorEnum
from google.ads.googleads.v11.errors.types.distinct_error import DistinctErrorEnum
from google.ads.googleads.v11.errors.types.enum_error import EnumErrorEnum
from google.ads.googleads.v11.errors.types.experiment_arm_error import (
    ExperimentArmErrorEnum,
)
from google.ads.googleads.v11.errors.types.experiment_error import ExperimentErrorEnum
from google.ads.googleads.v11.errors.types.extension_feed_item_error import (
    ExtensionFeedItemErrorEnum,
)
from google.ads.googleads.v11.errors.types.extension_setting_error import (
    ExtensionSettingErrorEnum,
)
from google.ads.googleads.v11.errors.types.feed_attribute_reference_error import (
    FeedAttributeReferenceErrorEnum,
)
from google.ads.googleads.v11.errors.types.feed_error import FeedErrorEnum
from google.ads.googleads.v11.errors.types.feed_item_error import FeedItemErrorEnum
from google.ads.googleads.v11.errors.types.feed_item_set_error import (
    FeedItemSetErrorEnum,
)
from google.ads.googleads.v11.errors.types.feed_item_set_link_error import (
    FeedItemSetLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.feed_item_target_error import (
    FeedItemTargetErrorEnum,
)
from google.ads.googleads.v11.errors.types.feed_item_validation_error import (
    FeedItemValidationErrorEnum,
)
from google.ads.googleads.v11.errors.types.feed_mapping_error import (
    FeedMappingErrorEnum,
)
from google.ads.googleads.v11.errors.types.field_error import FieldErrorEnum
from google.ads.googleads.v11.errors.types.field_mask_error import FieldMaskErrorEnum
from google.ads.googleads.v11.errors.types.function_error import FunctionErrorEnum
from google.ads.googleads.v11.errors.types.function_parsing_error import (
    FunctionParsingErrorEnum,
)
from google.ads.googleads.v11.errors.types.geo_target_constant_suggestion_error import (
    GeoTargetConstantSuggestionErrorEnum,
)
from google.ads.googleads.v11.errors.types.header_error import HeaderErrorEnum
from google.ads.googleads.v11.errors.types.id_error import IdErrorEnum
from google.ads.googleads.v11.errors.types.image_error import ImageErrorEnum
from google.ads.googleads.v11.errors.types.internal_error import InternalErrorEnum
from google.ads.googleads.v11.errors.types.invoice_error import InvoiceErrorEnum
from google.ads.googleads.v11.errors.types.keyword_plan_ad_group_error import (
    KeywordPlanAdGroupErrorEnum,
)
from google.ads.googleads.v11.errors.types.keyword_plan_ad_group_keyword_error import (
    KeywordPlanAdGroupKeywordErrorEnum,
)
from google.ads.googleads.v11.errors.types.keyword_plan_campaign_error import (
    KeywordPlanCampaignErrorEnum,
)
from google.ads.googleads.v11.errors.types.keyword_plan_campaign_keyword_error import (
    KeywordPlanCampaignKeywordErrorEnum,
)
from google.ads.googleads.v11.errors.types.keyword_plan_error import (
    KeywordPlanErrorEnum,
)
from google.ads.googleads.v11.errors.types.keyword_plan_idea_error import (
    KeywordPlanIdeaErrorEnum,
)
from google.ads.googleads.v11.errors.types.label_error import LabelErrorEnum
from google.ads.googleads.v11.errors.types.language_code_error import (
    LanguageCodeErrorEnum,
)
from google.ads.googleads.v11.errors.types.list_operation_error import (
    ListOperationErrorEnum,
)
from google.ads.googleads.v11.errors.types.manager_link_error import (
    ManagerLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.media_bundle_error import (
    MediaBundleErrorEnum,
)
from google.ads.googleads.v11.errors.types.media_file_error import MediaFileErrorEnum
from google.ads.googleads.v11.errors.types.media_upload_error import (
    MediaUploadErrorEnum,
)
from google.ads.googleads.v11.errors.types.merchant_center_error import (
    MerchantCenterErrorEnum,
)
from google.ads.googleads.v11.errors.types.multiplier_error import MultiplierErrorEnum
from google.ads.googleads.v11.errors.types.mutate_error import MutateErrorEnum
from google.ads.googleads.v11.errors.types.new_resource_creation_error import (
    NewResourceCreationErrorEnum,
)
from google.ads.googleads.v11.errors.types.not_allowlisted_error import (
    NotAllowlistedErrorEnum,
)
from google.ads.googleads.v11.errors.types.not_empty_error import NotEmptyErrorEnum
from google.ads.googleads.v11.errors.types.null_error import NullErrorEnum
from google.ads.googleads.v11.errors.types.offline_user_data_job_error import (
    OfflineUserDataJobErrorEnum,
)
from google.ads.googleads.v11.errors.types.operation_access_denied_error import (
    OperationAccessDeniedErrorEnum,
)
from google.ads.googleads.v11.errors.types.operator_error import OperatorErrorEnum
from google.ads.googleads.v11.errors.types.partial_failure_error import (
    PartialFailureErrorEnum,
)
from google.ads.googleads.v11.errors.types.payments_account_error import (
    PaymentsAccountErrorEnum,
)
from google.ads.googleads.v11.errors.types.policy_finding_error import (
    PolicyFindingErrorEnum,
)
from google.ads.googleads.v11.errors.types.policy_validation_parameter_error import (
    PolicyValidationParameterErrorEnum,
)
from google.ads.googleads.v11.errors.types.policy_violation_error import (
    PolicyViolationErrorEnum,
)
from google.ads.googleads.v11.errors.types.query_error import QueryErrorEnum
from google.ads.googleads.v11.errors.types.quota_error import QuotaErrorEnum
from google.ads.googleads.v11.errors.types.range_error import RangeErrorEnum
from google.ads.googleads.v11.errors.types.reach_plan_error import ReachPlanErrorEnum
from google.ads.googleads.v11.errors.types.recommendation_error import (
    RecommendationErrorEnum,
)
from google.ads.googleads.v11.errors.types.region_code_error import RegionCodeErrorEnum
from google.ads.googleads.v11.errors.types.request_error import RequestErrorEnum
from google.ads.googleads.v11.errors.types.resource_access_denied_error import (
    ResourceAccessDeniedErrorEnum,
)
from google.ads.googleads.v11.errors.types.resource_count_limit_exceeded_error import (
    ResourceCountLimitExceededErrorEnum,
)
from google.ads.googleads.v11.errors.types.setting_error import SettingErrorEnum
from google.ads.googleads.v11.errors.types.shared_criterion_error import (
    SharedCriterionErrorEnum,
)
from google.ads.googleads.v11.errors.types.shared_set_error import SharedSetErrorEnum
from google.ads.googleads.v11.errors.types.size_limit_error import SizeLimitErrorEnum
from google.ads.googleads.v11.errors.types.string_format_error import (
    StringFormatErrorEnum,
)
from google.ads.googleads.v11.errors.types.string_length_error import (
    StringLengthErrorEnum,
)
from google.ads.googleads.v11.errors.types.third_party_app_analytics_link_error import (
    ThirdPartyAppAnalyticsLinkErrorEnum,
)
from google.ads.googleads.v11.errors.types.time_zone_error import TimeZoneErrorEnum
from google.ads.googleads.v11.errors.types.url_field_error import UrlFieldErrorEnum
from google.ads.googleads.v11.errors.types.user_data_error import UserDataErrorEnum
from google.ads.googleads.v11.errors.types.user_list_error import UserListErrorEnum
from google.ads.googleads.v11.errors.types.youtube_video_registration_error import (
    YoutubeVideoRegistrationErrorEnum,
)

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
    ad_group_criterion_customizer_error: AdGroupCriterionCustomizerErrorEnum.AdGroupCriterionCustomizerError
    ad_group_criterion_error: AdGroupCriterionErrorEnum.AdGroupCriterionError
    ad_group_customizer_error: AdGroupCustomizerErrorEnum.AdGroupCustomizerError
    ad_customizer_error: AdCustomizerErrorEnum.AdCustomizerError
    ad_group_ad_error: AdGroupAdErrorEnum.AdGroupAdError
    ad_sharing_error: AdSharingErrorEnum.AdSharingError
    adx_error: AdxErrorEnum.AdxError
    asset_error: AssetErrorEnum.AssetError
    asset_group_asset_error: AssetGroupAssetErrorEnum.AssetGroupAssetError
    asset_group_listing_group_filter_error: AssetGroupListingGroupFilterErrorEnum.AssetGroupListingGroupFilterError
    asset_group_error: AssetGroupErrorEnum.AssetGroupError
    asset_set_asset_error: AssetSetAssetErrorEnum.AssetSetAssetError
    asset_set_link_error: AssetSetLinkErrorEnum.AssetSetLinkError
    asset_set_error: AssetSetErrorEnum.AssetSetError
    bidding_error: BiddingErrorEnum.BiddingError
    campaign_criterion_error: CampaignCriterionErrorEnum.CampaignCriterionError
    campaign_conversion_goal_error: CampaignConversionGoalErrorEnum.CampaignConversionGoalError
    campaign_customizer_error: CampaignCustomizerErrorEnum.CampaignCustomizerError
    collection_size_error: CollectionSizeErrorEnum.CollectionSizeError
    conversion_goal_campaign_config_error: ConversionGoalCampaignConfigErrorEnum.ConversionGoalCampaignConfigError
    country_code_error: CountryCodeErrorEnum.CountryCodeError
    criterion_error: CriterionErrorEnum.CriterionError
    custom_conversion_goal_error: CustomConversionGoalErrorEnum.CustomConversionGoalError
    customer_customizer_error: CustomerCustomizerErrorEnum.CustomerCustomizerError
    customer_error: CustomerErrorEnum.CustomerError
    customizer_attribute_error: CustomizerAttributeErrorEnum.CustomizerAttributeError
    date_error: DateErrorEnum.DateError
    date_range_error: DateRangeErrorEnum.DateRangeError
    distinct_error: DistinctErrorEnum.DistinctError
    feed_attribute_reference_error: FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError
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
    region_code_error: RegionCodeErrorEnum.RegionCodeError
    setting_error: SettingErrorEnum.SettingError
    string_format_error: StringFormatErrorEnum.StringFormatError
    string_length_error: StringLengthErrorEnum.StringLengthError
    operation_access_denied_error: OperationAccessDeniedErrorEnum.OperationAccessDeniedError
    resource_access_denied_error: ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError
    resource_count_limit_exceeded_error: ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError
    youtube_video_registration_error: YoutubeVideoRegistrationErrorEnum.YoutubeVideoRegistrationError
    ad_group_bid_modifier_error: AdGroupBidModifierErrorEnum.AdGroupBidModifierError
    context_error: ContextErrorEnum.ContextError
    field_error: FieldErrorEnum.FieldError
    shared_set_error: SharedSetErrorEnum.SharedSetError
    shared_criterion_error: SharedCriterionErrorEnum.SharedCriterionError
    campaign_shared_set_error: CampaignSharedSetErrorEnum.CampaignSharedSetError
    conversion_action_error: ConversionActionErrorEnum.ConversionActionError
    conversion_adjustment_upload_error: ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError
    conversion_custom_variable_error: ConversionCustomVariableErrorEnum.ConversionCustomVariableError
    conversion_upload_error: ConversionUploadErrorEnum.ConversionUploadError
    conversion_value_rule_error: ConversionValueRuleErrorEnum.ConversionValueRuleError
    conversion_value_rule_set_error: ConversionValueRuleSetErrorEnum.ConversionValueRuleSetError
    header_error: HeaderErrorEnum.HeaderError
    database_error: DatabaseErrorEnum.DatabaseError
    policy_finding_error: PolicyFindingErrorEnum.PolicyFindingError
    enum_error: EnumErrorEnum.EnumError
    keyword_plan_error: KeywordPlanErrorEnum.KeywordPlanError
    keyword_plan_campaign_error: KeywordPlanCampaignErrorEnum.KeywordPlanCampaignError
    keyword_plan_campaign_keyword_error: KeywordPlanCampaignKeywordErrorEnum.KeywordPlanCampaignKeywordError
    keyword_plan_ad_group_error: KeywordPlanAdGroupErrorEnum.KeywordPlanAdGroupError
    keyword_plan_ad_group_keyword_error: KeywordPlanAdGroupKeywordErrorEnum.KeywordPlanAdGroupKeywordError
    keyword_plan_idea_error: KeywordPlanIdeaErrorEnum.KeywordPlanIdeaError
    account_budget_proposal_error: AccountBudgetProposalErrorEnum.AccountBudgetProposalError
    user_list_error: UserListErrorEnum.UserListError
    change_event_error: ChangeEventErrorEnum.ChangeEventError
    change_status_error: ChangeStatusErrorEnum.ChangeStatusError
    feed_error: FeedErrorEnum.FeedError
    geo_target_constant_suggestion_error: GeoTargetConstantSuggestionErrorEnum.GeoTargetConstantSuggestionError
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
    policy_validation_parameter_error: PolicyValidationParameterErrorEnum.PolicyValidationParameterError
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
    third_party_app_analytics_link_error: ThirdPartyAppAnalyticsLinkErrorEnum.ThirdPartyAppAnalyticsLinkError
    customer_user_access_error: CustomerUserAccessErrorEnum.CustomerUserAccessError
    custom_audience_error: CustomAudienceErrorEnum.CustomAudienceError
    audience_error: AudienceErrorEnum.AudienceError
    experiment_arm_error: ExperimentArmErrorEnum.ExperimentArmError
    audience_insights_error: AudienceInsightsErrorEnum.AudienceInsightsError
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        experiment_arm_error: ExperimentArmErrorEnum.ExperimentArmError = ...,
        audience_insights_error: AudienceInsightsErrorEnum.AudienceInsightsError = ...
    ) -> None: ...

class ErrorDetails(proto.Message):
    unpublished_error_code: str
    policy_violation_details: PolicyViolationDetails
    policy_finding_details: PolicyFindingDetails
    quota_error_details: QuotaErrorDetails
    resource_count_details: ResourceCountDetails
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        unpublished_error_code: str = ...,
        policy_violation_details: PolicyViolationDetails = ...,
        policy_finding_details: PolicyFindingDetails = ...,
        quota_error_details: QuotaErrorDetails = ...,
        resource_count_details: ResourceCountDetails = ...
    ) -> None: ...

class ErrorLocation(proto.Message):
    class FieldPathElement(proto.Message):
        field_name: str
        index: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            field_name: str = ...,
            index: int = ...
        ) -> None: ...
    field_path_elements: list[ErrorLocation.FieldPathElement]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        field_path_elements: list[ErrorLocation.FieldPathElement] = ...
    ) -> None: ...

class GoogleAdsError(proto.Message):
    error_code: ErrorCode
    message: str
    trigger: Value
    location: ErrorLocation
    details: ErrorDetails
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        error_code: ErrorCode = ...,
        message: str = ...,
        trigger: Value = ...,
        location: ErrorLocation = ...,
        details: ErrorDetails = ...
    ) -> None: ...

class GoogleAdsFailure(proto.Message):
    errors: list[GoogleAdsError]
    request_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        errors: list[GoogleAdsError] = ...,
        request_id: str = ...
    ) -> None: ...

class PolicyFindingDetails(proto.Message):
    policy_topic_entries: list[PolicyTopicEntry]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_topic_entries: list[PolicyTopicEntry] = ...
    ) -> None: ...

class PolicyViolationDetails(proto.Message):
    external_policy_description: str
    key: PolicyViolationKey
    external_policy_name: str
    is_exemptible: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        external_policy_description: str = ...,
        key: PolicyViolationKey = ...,
        external_policy_name: str = ...,
        is_exemptible: bool = ...
    ) -> None: ...

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        rate_scope: QuotaErrorDetails.QuotaRateScope = ...,
        rate_name: str = ...,
        retry_delay: Duration = ...
    ) -> None: ...

class ResourceCountDetails(proto.Message):
    enclosing_id: str
    enclosing_resource: str
    limit: int
    limit_type: ResourceLimitTypeEnum.ResourceLimitType
    existing_count: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        enclosing_id: str = ...,
        enclosing_resource: str = ...,
        limit: int = ...,
        limit_type: ResourceLimitTypeEnum.ResourceLimitType = ...,
        existing_count: int = ...
    ) -> None: ...
