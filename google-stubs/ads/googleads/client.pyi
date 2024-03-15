from typing import Any, overload

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

from google.ads.googleads import v14, v15, v16
from google.ads.googleads.config import _ConfigDataUnparsed

_V14 = Literal["v14"]
_V15 = Literal["v15"]
_V16 = Literal["v16"]
_V = _V14 | _V15 | _V16

class _EnumGetter:
    AccessInvitationStatusEnum: type[
        v16.AccessInvitationStatusEnum.AccessInvitationStatus
    ]
    AccessReasonEnum: type[v16.AccessReasonEnum.AccessReason]
    AccessRoleEnum: type[v16.AccessRoleEnum.AccessRole]
    AccountBudgetProposalStatusEnum: type[
        v16.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    ]
    AccountBudgetProposalTypeEnum: type[
        v16.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    ]
    AccountBudgetStatusEnum: type[v16.AccountBudgetStatusEnum.AccountBudgetStatus]
    AccountLinkStatusEnum: type[v16.AccountLinkStatusEnum.AccountLinkStatus]
    AdCustomizerPlaceholderFieldEnum: type[
        v16.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    ]
    AdDestinationTypeEnum: type[v16.AdDestinationTypeEnum.AdDestinationType]
    AdGroupAdPrimaryStatusEnum: type[
        v16.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    ]
    AdGroupAdPrimaryStatusReasonEnum: type[
        v16.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    ]
    AdGroupAdRotationModeEnum: type[v16.AdGroupAdRotationModeEnum.AdGroupAdRotationMode]
    AdGroupAdStatusEnum: type[v16.AdGroupAdStatusEnum.AdGroupAdStatus]
    AdGroupCriterionApprovalStatusEnum: type[
        v16.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    ]
    AdGroupCriterionStatusEnum: type[
        v16.AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    ]
    AdGroupPrimaryStatusEnum: type[v16.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
    AdGroupPrimaryStatusReasonEnum: type[
        v16.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    ]
    AdGroupStatusEnum: type[v16.AdGroupStatusEnum.AdGroupStatus]
    AdGroupTypeEnum: type[v16.AdGroupTypeEnum.AdGroupType]
    AdNetworkTypeEnum: type[v16.AdNetworkTypeEnum.AdNetworkType]
    AdServingOptimizationStatusEnum: type[
        v16.AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    ]
    AdStrengthEnum: type[v16.AdStrengthEnum.AdStrength]
    AdTypeEnum: type[v16.AdTypeEnum.AdType]
    AdvertisingChannelSubTypeEnum: type[
        v16.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    ]
    AdvertisingChannelTypeEnum: type[
        v16.AdvertisingChannelTypeEnum.AdvertisingChannelType
    ]
    AffiliateLocationFeedRelationshipTypeEnum: type[
        v16.AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
    ]
    AffiliateLocationPlaceholderFieldEnum: type[
        v16.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField
    ]
    AgeRangeTypeEnum: type[v16.AgeRangeTypeEnum.AgeRangeType]
    AndroidPrivacyInteractionTypeEnum: type[
        v16.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    ]
    AndroidPrivacyNetworkTypeEnum: type[
        v16.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    ]
    AppBiddingGoalEnum: type[v16.AppBiddingGoalEnum.AppBiddingGoal]
    AppCampaignAppStoreEnum: type[v16.AppCampaignAppStoreEnum.AppCampaignAppStore]
    AppCampaignBiddingStrategyGoalTypeEnum: type[
        v16.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    ]
    AppPaymentModelTypeEnum: type[v16.AppPaymentModelTypeEnum.AppPaymentModelType]
    AppPlaceholderFieldEnum: type[v16.AppPlaceholderFieldEnum.AppPlaceholderField]
    AppStoreEnum: type[v16.AppStoreEnum.AppStore]
    AppUrlOperatingSystemTypeEnum: type[
        v16.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    ]
    AssetAutomationStatusEnum: type[v16.AssetAutomationStatusEnum.AssetAutomationStatus]
    AssetAutomationTypeEnum: type[v16.AssetAutomationTypeEnum.AssetAutomationType]
    AssetFieldTypeEnum: type[v16.AssetFieldTypeEnum.AssetFieldType]
    AssetGroupPrimaryStatusEnum: type[
        v16.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    ]
    AssetGroupPrimaryStatusReasonEnum: type[
        v16.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ]
    AssetGroupSignalApprovalStatusEnum: type[
        v16.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    ]
    AssetGroupStatusEnum: type[v16.AssetGroupStatusEnum.AssetGroupStatus]
    AssetLinkPrimaryStatusEnum: type[
        v16.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    ]
    AssetLinkPrimaryStatusReasonEnum: type[
        v16.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ]
    AssetLinkStatusEnum: type[v16.AssetLinkStatusEnum.AssetLinkStatus]
    AssetOfflineEvaluationErrorReasonsEnum: type[
        v16.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    ]
    AssetPerformanceLabelEnum: type[v16.AssetPerformanceLabelEnum.AssetPerformanceLabel]
    AssetSetAssetStatusEnum: type[v16.AssetSetAssetStatusEnum.AssetSetAssetStatus]
    AssetSetLinkStatusEnum: type[v16.AssetSetLinkStatusEnum.AssetSetLinkStatus]
    AssetSetStatusEnum: type[v16.AssetSetStatusEnum.AssetSetStatus]
    AssetSetTypeEnum: type[v16.AssetSetTypeEnum.AssetSetType]
    AssetSourceEnum: type[v16.AssetSourceEnum.AssetSource]
    AssetTypeEnum: type[v16.AssetTypeEnum.AssetType]
    AsyncActionStatusEnum: type[v16.AsyncActionStatusEnum.AsyncActionStatus]
    AttributionModelEnum: type[v16.AttributionModelEnum.AttributionModel]
    AudienceInsightsDimensionEnum: type[
        v16.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    ]
    AudienceScopeEnum: type[v16.AudienceScopeEnum.AudienceScope]
    AudienceStatusEnum: type[v16.AudienceStatusEnum.AudienceStatus]
    BatchJobStatusEnum: type[v16.BatchJobStatusEnum.BatchJobStatus]
    BidModifierSourceEnum: type[v16.BidModifierSourceEnum.BidModifierSource]
    BiddingSourceEnum: type[v16.BiddingSourceEnum.BiddingSource]
    BiddingStrategyStatusEnum: type[v16.BiddingStrategyStatusEnum.BiddingStrategyStatus]
    BiddingStrategySystemStatusEnum: type[
        v16.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ]
    BiddingStrategyTypeEnum: type[v16.BiddingStrategyTypeEnum.BiddingStrategyType]
    BillingSetupStatusEnum: type[v16.BillingSetupStatusEnum.BillingSetupStatus]
    BrandSafetySuitabilityEnum: type[
        v16.BrandSafetySuitabilityEnum.BrandSafetySuitability
    ]
    BrandStateEnum: type[v16.BrandStateEnum.BrandState]
    BudgetCampaignAssociationStatusEnum: type[
        v16.BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    ]
    BudgetDeliveryMethodEnum: type[v16.BudgetDeliveryMethodEnum.BudgetDeliveryMethod]
    BudgetPeriodEnum: type[v16.BudgetPeriodEnum.BudgetPeriod]
    BudgetStatusEnum: type[v16.BudgetStatusEnum.BudgetStatus]
    BudgetTypeEnum: type[v16.BudgetTypeEnum.BudgetType]
    CallConversionReportingStateEnum: type[
        v16.CallConversionReportingStateEnum.CallConversionReportingState
    ]
    CallPlaceholderFieldEnum: type[v16.CallPlaceholderFieldEnum.CallPlaceholderField]
    CallToActionTypeEnum: type[v16.CallToActionTypeEnum.CallToActionType]
    CallTrackingDisplayLocationEnum: type[
        v16.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    ]
    CallTypeEnum: type[v16.CallTypeEnum.CallType]
    CalloutPlaceholderFieldEnum: type[
        v16.CalloutPlaceholderFieldEnum.CalloutPlaceholderField
    ]
    CampaignCriterionStatusEnum: type[
        v16.CampaignCriterionStatusEnum.CampaignCriterionStatus
    ]
    CampaignDraftStatusEnum: type[v16.CampaignDraftStatusEnum.CampaignDraftStatus]
    CampaignExperimentTypeEnum: type[
        v16.CampaignExperimentTypeEnum.CampaignExperimentType
    ]
    CampaignGroupStatusEnum: type[v16.CampaignGroupStatusEnum.CampaignGroupStatus]
    CampaignPrimaryStatusEnum: type[v16.CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
    CampaignPrimaryStatusReasonEnum: type[
        v16.CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    ]
    CampaignServingStatusEnum: type[v16.CampaignServingStatusEnum.CampaignServingStatus]
    CampaignSharedSetStatusEnum: type[
        v16.CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    ]
    CampaignStatusEnum: type[v16.CampaignStatusEnum.CampaignStatus]
    ChainRelationshipTypeEnum: type[v16.ChainRelationshipTypeEnum.ChainRelationshipType]
    ChangeClientTypeEnum: type[v16.ChangeClientTypeEnum.ChangeClientType]
    ChangeEventResourceTypeEnum: type[
        v16.ChangeEventResourceTypeEnum.ChangeEventResourceType
    ]
    ChangeStatusOperationEnum: type[v16.ChangeStatusOperationEnum.ChangeStatusOperation]
    ChangeStatusResourceTypeEnum: type[
        v16.ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    ]
    ClickTypeEnum: type[v16.ClickTypeEnum.ClickType]
    CombinedAudienceStatusEnum: type[
        v16.CombinedAudienceStatusEnum.CombinedAudienceStatus
    ]
    ConsentStatusEnum: type[v16.ConsentStatusEnum.ConsentStatus]
    ContentLabelTypeEnum: type[v16.ContentLabelTypeEnum.ContentLabelType]
    ConversionActionCategoryEnum: type[
        v16.ConversionActionCategoryEnum.ConversionActionCategory
    ]
    ConversionActionCountingTypeEnum: type[
        v16.ConversionActionCountingTypeEnum.ConversionActionCountingType
    ]
    ConversionActionStatusEnum: type[
        v16.ConversionActionStatusEnum.ConversionActionStatus
    ]
    ConversionActionTypeEnum: type[v16.ConversionActionTypeEnum.ConversionActionType]
    ConversionAdjustmentTypeEnum: type[
        v16.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    ]
    ConversionAttributionEventTypeEnum: type[
        v16.ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    ]
    ConversionCustomVariableStatusEnum: type[
        v16.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    ]
    ConversionEnvironmentEnum: type[v16.ConversionEnvironmentEnum.ConversionEnvironment]
    ConversionLagBucketEnum: type[v16.ConversionLagBucketEnum.ConversionLagBucket]
    ConversionOrAdjustmentLagBucketEnum: type[
        v16.ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    ]
    ConversionOriginEnum: type[v16.ConversionOriginEnum.ConversionOrigin]
    ConversionTrackingStatusEnum: type[
        v16.ConversionTrackingStatusEnum.ConversionTrackingStatus
    ]
    ConversionValueRulePrimaryDimensionEnum: type[
        v16.ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    ]
    ConversionValueRuleSetStatusEnum: type[
        v16.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    ]
    ConversionValueRuleStatusEnum: type[
        v16.ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    ]
    ConvertingUserPriorEngagementTypeAndLtvBucketEnum: type[
        v16.ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket
    ]
    CriterionCategoryChannelAvailabilityModeEnum: type[
        v16.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    ]
    CriterionCategoryLocaleAvailabilityModeEnum: type[
        v16.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    ]
    CriterionSystemServingStatusEnum: type[
        v16.CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    ]
    CriterionTypeEnum: type[v16.CriterionTypeEnum.CriterionType]
    CustomAudienceMemberTypeEnum: type[
        v16.CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    ]
    CustomAudienceStatusEnum: type[v16.CustomAudienceStatusEnum.CustomAudienceStatus]
    CustomAudienceTypeEnum: type[v16.CustomAudienceTypeEnum.CustomAudienceType]
    CustomConversionGoalStatusEnum: type[
        v16.CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    ]
    CustomInterestMemberTypeEnum: type[
        v16.CustomInterestMemberTypeEnum.CustomInterestMemberType
    ]
    CustomInterestStatusEnum: type[v16.CustomInterestStatusEnum.CustomInterestStatus]
    CustomInterestTypeEnum: type[v16.CustomInterestTypeEnum.CustomInterestType]
    CustomPlaceholderFieldEnum: type[
        v16.CustomPlaceholderFieldEnum.CustomPlaceholderField
    ]
    CustomerAcquisitionOptimizationModeEnum: type[
        v16.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    ]
    CustomerMatchUploadKeyTypeEnum: type[
        v16.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    ]
    CustomerPayPerConversionEligibilityFailureReasonEnum: type[
        v16.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    ]
    CustomerStatusEnum: type[v16.CustomerStatusEnum.CustomerStatus]
    CustomizerAttributeStatusEnum: type[
        v16.CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    ]
    CustomizerAttributeTypeEnum: type[
        v16.CustomizerAttributeTypeEnum.CustomizerAttributeType
    ]
    CustomizerValueStatusEnum: type[v16.CustomizerValueStatusEnum.CustomizerValueStatus]
    DataDrivenModelStatusEnum: type[v16.DataDrivenModelStatusEnum.DataDrivenModelStatus]
    DayOfWeekEnum: type[v16.DayOfWeekEnum.DayOfWeek]
    DeviceEnum: type[v16.DeviceEnum.Device]
    DisplayAdFormatSettingEnum: type[
        v16.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    ]
    DisplayUploadProductTypeEnum: type[
        v16.DisplayUploadProductTypeEnum.DisplayUploadProductType
    ]
    DistanceBucketEnum: type[v16.DistanceBucketEnum.DistanceBucket]
    DsaPageFeedCriterionFieldEnum: type[
        v16.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    ]
    EducationPlaceholderFieldEnum: type[
        v16.EducationPlaceholderFieldEnum.EducationPlaceholderField
    ]
    ExperimentMetricDirectionEnum: type[
        v16.ExperimentMetricDirectionEnum.ExperimentMetricDirection
    ]
    ExperimentMetricEnum: type[v16.ExperimentMetricEnum.ExperimentMetric]
    ExperimentStatusEnum: type[v16.ExperimentStatusEnum.ExperimentStatus]
    ExperimentTypeEnum: type[v16.ExperimentTypeEnum.ExperimentType]
    ExtensionSettingDeviceEnum: type[
        v16.ExtensionSettingDeviceEnum.ExtensionSettingDevice
    ]
    ExtensionTypeEnum: type[v16.ExtensionTypeEnum.ExtensionType]
    ExternalConversionSourceEnum: type[
        v16.ExternalConversionSourceEnum.ExternalConversionSource
    ]
    FeedAttributeTypeEnum: type[v16.FeedAttributeTypeEnum.FeedAttributeType]
    FeedItemQualityApprovalStatusEnum: type[
        v16.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    ]
    FeedItemQualityDisapprovalReasonEnum: type[
        v16.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    ]
    FeedItemSetStatusEnum: type[v16.FeedItemSetStatusEnum.FeedItemSetStatus]
    FeedItemSetStringFilterTypeEnum: type[
        v16.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    ]
    FeedItemStatusEnum: type[v16.FeedItemStatusEnum.FeedItemStatus]
    FeedItemTargetDeviceEnum: type[v16.FeedItemTargetDeviceEnum.FeedItemTargetDevice]
    FeedItemTargetStatusEnum: type[v16.FeedItemTargetStatusEnum.FeedItemTargetStatus]
    FeedItemTargetTypeEnum: type[v16.FeedItemTargetTypeEnum.FeedItemTargetType]
    FeedItemValidationStatusEnum: type[
        v16.FeedItemValidationStatusEnum.FeedItemValidationStatus
    ]
    FeedLinkStatusEnum: type[v16.FeedLinkStatusEnum.FeedLinkStatus]
    FeedMappingCriterionTypeEnum: type[
        v16.FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    ]
    FeedMappingStatusEnum: type[v16.FeedMappingStatusEnum.FeedMappingStatus]
    FeedOriginEnum: type[v16.FeedOriginEnum.FeedOrigin]
    FeedStatusEnum: type[v16.FeedStatusEnum.FeedStatus]
    FlightPlaceholderFieldEnum: type[
        v16.FlightPlaceholderFieldEnum.FlightPlaceholderField
    ]
    FrequencyCapEventTypeEnum: type[v16.FrequencyCapEventTypeEnum.FrequencyCapEventType]
    FrequencyCapLevelEnum: type[v16.FrequencyCapLevelEnum.FrequencyCapLevel]
    FrequencyCapTimeUnitEnum: type[v16.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
    GenderTypeEnum: type[v16.GenderTypeEnum.GenderType]
    GeoTargetConstantStatusEnum: type[
        v16.GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    ]
    GeoTargetingRestrictionEnum: type[
        v16.GeoTargetingRestrictionEnum.GeoTargetingRestriction
    ]
    GeoTargetingTypeEnum: type[v16.GeoTargetingTypeEnum.GeoTargetingType]
    GoalConfigLevelEnum: type[v16.GoalConfigLevelEnum.GoalConfigLevel]
    GoogleAdsFieldCategoryEnum: type[
        v16.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    ]
    GoogleAdsFieldDataTypeEnum: type[
        v16.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    ]
    GoogleVoiceCallStatusEnum: type[v16.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus]
    HotelAssetSuggestionStatusEnum: type[
        v16.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    ]
    HotelDateSelectionTypeEnum: type[
        v16.HotelDateSelectionTypeEnum.HotelDateSelectionType
    ]
    HotelPlaceholderFieldEnum: type[v16.HotelPlaceholderFieldEnum.HotelPlaceholderField]
    HotelPriceBucketEnum: type[v16.HotelPriceBucketEnum.HotelPriceBucket]
    HotelRateTypeEnum: type[v16.HotelRateTypeEnum.HotelRateType]
    HotelReconciliationStatusEnum: type[
        v16.HotelReconciliationStatusEnum.HotelReconciliationStatus
    ]
    IdentityVerificationProgramEnum: type[
        v16.IdentityVerificationProgramEnum.IdentityVerificationProgram
    ]
    IdentityVerificationProgramStatusEnum: type[
        v16.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    ]
    ImagePlaceholderFieldEnum: type[v16.ImagePlaceholderFieldEnum.ImagePlaceholderField]
    IncomeRangeTypeEnum: type[v16.IncomeRangeTypeEnum.IncomeRangeType]
    InteractionEventTypeEnum: type[v16.InteractionEventTypeEnum.InteractionEventType]
    InteractionTypeEnum: type[v16.InteractionTypeEnum.InteractionType]
    InvoiceTypeEnum: type[v16.InvoiceTypeEnum.InvoiceType]
    JobPlaceholderFieldEnum: type[v16.JobPlaceholderFieldEnum.JobPlaceholderField]
    KeywordMatchTypeEnum: type[v16.KeywordMatchTypeEnum.KeywordMatchType]
    KeywordPlanAggregateMetricTypeEnum: type[
        v16.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    ]
    KeywordPlanCompetitionLevelEnum: type[
        v16.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    ]
    KeywordPlanConceptGroupTypeEnum: type[
        v16.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    ]
    KeywordPlanForecastIntervalEnum: type[
        v16.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    ]
    KeywordPlanKeywordAnnotationEnum: type[
        v16.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
    ]
    KeywordPlanNetworkEnum: type[v16.KeywordPlanNetworkEnum.KeywordPlanNetwork]
    LabelStatusEnum: type[v16.LabelStatusEnum.LabelStatus]
    LeadFormCallToActionTypeEnum: type[
        v16.LeadFormCallToActionTypeEnum.LeadFormCallToActionType
    ]
    LeadFormDesiredIntentEnum: type[v16.LeadFormDesiredIntentEnum.LeadFormDesiredIntent]
    LeadFormFieldUserInputTypeEnum: type[
        v16.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    ]
    LeadFormPostSubmitCallToActionTypeEnum: type[
        v16.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    ]
    LegacyAppInstallAdAppStoreEnum: type[
        v16.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    ]
    LinkedAccountTypeEnum: type[v16.LinkedAccountTypeEnum.LinkedAccountType]
    LinkedProductTypeEnum: type[v16.LinkedProductTypeEnum.LinkedProductType]
    ListingGroupFilterCustomAttributeIndexEnum: type[
        v16.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
    ]
    ListingGroupFilterListingSourceEnum: type[
        v16.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    ]
    ListingGroupFilterProductCategoryLevelEnum: type[
        v16.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    ]
    ListingGroupFilterProductChannelEnum: type[
        v16.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    ]
    ListingGroupFilterProductConditionEnum: type[
        v16.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    ]
    ListingGroupFilterProductTypeLevelEnum: type[
        v16.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    ]
    ListingGroupFilterTypeEnum: type[
        v16.ListingGroupFilterTypeEnum.ListingGroupFilterType
    ]
    ListingGroupTypeEnum: type[v16.ListingGroupTypeEnum.ListingGroupType]
    ListingTypeEnum: type[v16.ListingTypeEnum.ListingType]
    LocalPlaceholderFieldEnum: type[v16.LocalPlaceholderFieldEnum.LocalPlaceholderField]
    LocalServicesBusinessRegistrationCheckRejectionReasonEnum: type[
        v16.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReason
    ]
    LocalServicesBusinessRegistrationTypeEnum: type[
        v16.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    ]
    LocalServicesEmployeeStatusEnum: type[
        v16.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    ]
    LocalServicesEmployeeTypeEnum: type[
        v16.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    ]
    LocalServicesInsuranceRejectionReasonEnum: type[
        v16.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    ]
    LocalServicesLeadConversationTypeEnum: type[
        v16.LocalServicesLeadConversationTypeEnum.ConversationType
    ]
    LocalServicesLeadStatusEnum: type[v16.LocalServicesLeadStatusEnum.LeadStatus]
    LocalServicesLeadTypeEnum: type[v16.LocalServicesLeadTypeEnum.LeadType]
    LocalServicesLicenseRejectionReasonEnum: type[
        v16.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    ]
    LocalServicesParticipantTypeEnum: type[
        v16.LocalServicesParticipantTypeEnum.ParticipantType
    ]
    LocalServicesVerificationArtifactStatusEnum: type[
        v16.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    ]
    LocalServicesVerificationArtifactTypeEnum: type[
        v16.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    ]
    LocalServicesVerificationStatusEnum: type[
        v16.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    ]
    LocationExtensionTargetingCriterionFieldEnum: type[
        v16.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    ]
    LocationGroupRadiusUnitsEnum: type[
        v16.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    ]
    LocationOwnershipTypeEnum: type[v16.LocationOwnershipTypeEnum.LocationOwnershipType]
    LocationPlaceholderFieldEnum: type[
        v16.LocationPlaceholderFieldEnum.LocationPlaceholderField
    ]
    LocationSourceTypeEnum: type[v16.LocationSourceTypeEnum.LocationSourceType]
    LocationStringFilterTypeEnum: type[
        v16.LocationStringFilterTypeEnum.LocationStringFilterType
    ]
    LookalikeExpansionLevelEnum: type[
        v16.LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    ]
    ManagerLinkStatusEnum: type[v16.ManagerLinkStatusEnum.ManagerLinkStatus]
    MatchingFunctionContextTypeEnum: type[
        v16.MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    ]
    MatchingFunctionOperatorEnum: type[
        v16.MatchingFunctionOperatorEnum.MatchingFunctionOperator
    ]
    MediaTypeEnum: type[v16.MediaTypeEnum.MediaType]
    MessagePlaceholderFieldEnum: type[
        v16.MessagePlaceholderFieldEnum.MessagePlaceholderField
    ]
    MimeTypeEnum: type[v16.MimeTypeEnum.MimeType]
    MinuteOfHourEnum: type[v16.MinuteOfHourEnum.MinuteOfHour]
    MobileAppVendorEnum: type[v16.MobileAppVendorEnum.MobileAppVendor]
    MobileDeviceTypeEnum: type[v16.MobileDeviceTypeEnum.MobileDeviceType]
    MonthOfYearEnum: type[v16.MonthOfYearEnum.MonthOfYear]
    NegativeGeoTargetTypeEnum: type[v16.NegativeGeoTargetTypeEnum.NegativeGeoTargetType]
    OfflineConversionDiagnosticStatusEnum: type[
        v16.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    ]
    OfflineEventUploadClientEnum: type[
        v16.OfflineEventUploadClientEnum.OfflineEventUploadClient
    ]
    OfflineUserDataJobFailureReasonEnum: type[
        v16.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    ]
    OfflineUserDataJobMatchRateRangeEnum: type[
        v16.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
    ]
    OfflineUserDataJobStatusEnum: type[
        v16.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    ]
    OfflineUserDataJobTypeEnum: type[
        v16.OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    ]
    OperatingSystemVersionOperatorTypeEnum: type[
        v16.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    ]
    OptimizationGoalTypeEnum: type[v16.OptimizationGoalTypeEnum.OptimizationGoalType]
    ParentalStatusTypeEnum: type[v16.ParentalStatusTypeEnum.ParentalStatusType]
    PaymentModeEnum: type[v16.PaymentModeEnum.PaymentMode]
    PerformanceMaxUpgradeStatusEnum: type[
        v16.PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    ]
    PlaceholderTypeEnum: type[v16.PlaceholderTypeEnum.PlaceholderType]
    PlacementTypeEnum: type[v16.PlacementTypeEnum.PlacementType]
    PolicyApprovalStatusEnum: type[v16.PolicyApprovalStatusEnum.PolicyApprovalStatus]
    PolicyReviewStatusEnum: type[v16.PolicyReviewStatusEnum.PolicyReviewStatus]
    PolicyTopicEntryTypeEnum: type[v16.PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum: type[
        v16.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
    ]
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum: type[
        v16.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    ]
    PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum: type[
        v16.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
    ]
    PositiveGeoTargetTypeEnum: type[v16.PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
    PriceExtensionPriceQualifierEnum: type[
        v16.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    ]
    PriceExtensionPriceUnitEnum: type[
        v16.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    ]
    PriceExtensionTypeEnum: type[v16.PriceExtensionTypeEnum.PriceExtensionType]
    PricePlaceholderFieldEnum: type[v16.PricePlaceholderFieldEnum.PricePlaceholderField]
    ProductCategoryLevelEnum: type[v16.ProductCategoryLevelEnum.ProductCategoryLevel]
    ProductCategoryStateEnum: type[v16.ProductCategoryStateEnum.ProductCategoryState]
    ProductChannelEnum: type[v16.ProductChannelEnum.ProductChannel]
    ProductChannelExclusivityEnum: type[
        v16.ProductChannelExclusivityEnum.ProductChannelExclusivity
    ]
    ProductConditionEnum: type[v16.ProductConditionEnum.ProductCondition]
    ProductCustomAttributeIndexEnum: type[
        v16.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    ]
    ProductLinkInvitationStatusEnum: type[
        v16.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    ]
    ProductTypeLevelEnum: type[v16.ProductTypeLevelEnum.ProductTypeLevel]
    PromotionExtensionDiscountModifierEnum: type[
        v16.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    ]
    PromotionExtensionOccasionEnum: type[
        v16.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    ]
    PromotionPlaceholderFieldEnum: type[
        v16.PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    ]
    ProximityRadiusUnitsEnum: type[v16.ProximityRadiusUnitsEnum.ProximityRadiusUnits]
    QualityScoreBucketEnum: type[v16.QualityScoreBucketEnum.QualityScoreBucket]
    ReachPlanAgeRangeEnum: type[v16.ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    ReachPlanNetworkEnum: type[v16.ReachPlanNetworkEnum.ReachPlanNetwork]
    ReachPlanSurfaceEnum: type[v16.ReachPlanSurfaceEnum.ReachPlanSurface]
    RealEstatePlaceholderFieldEnum: type[
        v16.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField
    ]
    RecommendationSubscriptionStatusEnum: type[
        v16.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    ]
    RecommendationTypeEnum: type[v16.RecommendationTypeEnum.RecommendationType]
    ResourceChangeOperationEnum: type[
        v16.ResourceChangeOperationEnum.ResourceChangeOperation
    ]
    ResourceLimitTypeEnum: type[v16.ResourceLimitTypeEnum.ResourceLimitType]
    ResponseContentTypeEnum: type[v16.ResponseContentTypeEnum.ResponseContentType]
    SearchEngineResultsPageTypeEnum: type[
        v16.SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    ]
    SearchTermMatchTypeEnum: type[v16.SearchTermMatchTypeEnum.SearchTermMatchType]
    SearchTermTargetingStatusEnum: type[
        v16.SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    ]
    SeasonalityEventScopeEnum: type[v16.SeasonalityEventScopeEnum.SeasonalityEventScope]
    SeasonalityEventStatusEnum: type[
        v16.SeasonalityEventStatusEnum.SeasonalityEventStatus
    ]
    ServedAssetFieldTypeEnum: type[v16.ServedAssetFieldTypeEnum.ServedAssetFieldType]
    SharedSetStatusEnum: type[v16.SharedSetStatusEnum.SharedSetStatus]
    SharedSetTypeEnum: type[v16.SharedSetTypeEnum.SharedSetType]
    ShoppingAddProductsToCampaignRecommendationEnum: type[
        v16.ShoppingAddProductsToCampaignRecommendationEnum.Reason
    ]
    SimulationModificationMethodEnum: type[
        v16.SimulationModificationMethodEnum.SimulationModificationMethod
    ]
    SimulationTypeEnum: type[v16.SimulationTypeEnum.SimulationType]
    SitelinkPlaceholderFieldEnum: type[
        v16.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    ]
    SkAdNetworkAdEventTypeEnum: type[
        v16.SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    ]
    SkAdNetworkAttributionCreditEnum: type[
        v16.SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    ]
    SkAdNetworkCoarseConversionValueEnum: type[
        v16.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    ]
    SkAdNetworkSourceTypeEnum: type[v16.SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
    SkAdNetworkUserTypeEnum: type[v16.SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
    SlotEnum: type[v16.SlotEnum.Slot]
    SmartCampaignNotEligibleReasonEnum: type[
        v16.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    ]
    SmartCampaignStatusEnum: type[v16.SmartCampaignStatusEnum.SmartCampaignStatus]
    SpendingLimitTypeEnum: type[v16.SpendingLimitTypeEnum.SpendingLimitType]
    StructuredSnippetPlaceholderFieldEnum: type[
        v16.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    ]
    SummaryRowSettingEnum: type[v16.SummaryRowSettingEnum.SummaryRowSetting]
    SystemManagedResourceSourceEnum: type[
        v16.SystemManagedResourceSourceEnum.SystemManagedResourceSource
    ]
    TargetCpaOptInRecommendationGoalEnum: type[
        v16.TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    ]
    TargetFrequencyTimeUnitEnum: type[
        v16.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    ]
    TargetImpressionShareLocationEnum: type[
        v16.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    ]
    TargetingDimensionEnum: type[v16.TargetingDimensionEnum.TargetingDimension]
    TimeTypeEnum: type[v16.TimeTypeEnum.TimeType]
    TrackingCodePageFormatEnum: type[
        v16.TrackingCodePageFormatEnum.TrackingCodePageFormat
    ]
    TrackingCodeTypeEnum: type[v16.TrackingCodeTypeEnum.TrackingCodeType]
    TravelPlaceholderFieldEnum: type[
        v16.TravelPlaceholderFieldEnum.TravelPlaceholderField
    ]
    UserIdentifierSourceEnum: type[v16.UserIdentifierSourceEnum.UserIdentifierSource]
    UserInterestTaxonomyTypeEnum: type[
        v16.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    ]
    UserListAccessStatusEnum: type[v16.UserListAccessStatusEnum.UserListAccessStatus]
    UserListClosingReasonEnum: type[v16.UserListClosingReasonEnum.UserListClosingReason]
    UserListCrmDataSourceTypeEnum: type[
        v16.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    ]
    UserListDateRuleItemOperatorEnum: type[
        v16.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    ]
    UserListFlexibleRuleOperatorEnum: type[
        v16.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    ]
    UserListLogicalRuleOperatorEnum: type[
        v16.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    ]
    UserListMembershipStatusEnum: type[
        v16.UserListMembershipStatusEnum.UserListMembershipStatus
    ]
    UserListNumberRuleItemOperatorEnum: type[
        v16.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    ]
    UserListPrepopulationStatusEnum: type[
        v16.UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    ]
    UserListRuleTypeEnum: type[v16.UserListRuleTypeEnum.UserListRuleType]
    UserListSizeRangeEnum: type[v16.UserListSizeRangeEnum.UserListSizeRange]
    UserListStringRuleItemOperatorEnum: type[
        v16.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    ]
    UserListTypeEnum: type[v16.UserListTypeEnum.UserListType]
    ValueRuleDeviceTypeEnum: type[v16.ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
    ValueRuleGeoLocationMatchTypeEnum: type[
        v16.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    ]
    ValueRuleOperationEnum: type[v16.ValueRuleOperationEnum.ValueRuleOperation]
    ValueRuleSetAttachmentTypeEnum: type[
        v16.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    ]
    ValueRuleSetDimensionEnum: type[v16.ValueRuleSetDimensionEnum.ValueRuleSetDimension]
    VanityPharmaDisplayUrlModeEnum: type[
        v16.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
    ]
    VanityPharmaTextEnum: type[v16.VanityPharmaTextEnum.VanityPharmaText]
    VideoThumbnailEnum: type[v16.VideoThumbnailEnum.VideoThumbnail]
    WebpageConditionOperandEnum: type[
        v16.WebpageConditionOperandEnum.WebpageConditionOperand
    ]
    WebpageConditionOperatorEnum: type[
        v16.WebpageConditionOperatorEnum.WebpageConditionOperator
    ]

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
    def get_type(cls, name: str, version: _V = "v16") -> Any: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V14
    ) -> v14.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V14
    ) -> v14.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V14
    ) -> v14.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V14
    ) -> v14.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V14
    ) -> v14.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V14
    ) -> v14.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V14
    ) -> v14.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V14
    ) -> v14.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V14
    ) -> v14.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V14
    ) -> v14.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V14
    ) -> v14.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V14
    ) -> v14.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V14
    ) -> v14.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V14
    ) -> v14.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V14
    ) -> v14.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V14
    ) -> v14.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V14
    ) -> v14.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V14
    ) -> v14.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V14
    ) -> v14.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V14
    ) -> v14.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V14
    ) -> v14.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V14
    ) -> v14.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V14
    ) -> v14.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V14
    ) -> v14.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V14
    ) -> v14.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V14
    ) -> v14.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V14
    ) -> v14.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V14
    ) -> v14.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V14
    ) -> v14.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V14
    ) -> v14.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V14
    ) -> v14.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V14
    ) -> v14.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V14
    ) -> v14.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V14
    ) -> v14.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V14
    ) -> v14.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V14
    ) -> v14.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V14
    ) -> v14.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V14
    ) -> v14.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V14
    ) -> v14.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V14
    ) -> v14.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V14
    ) -> v14.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V14
    ) -> v14.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V14
    ) -> v14.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V14
    ) -> v14.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V14
    ) -> v14.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V14
    ) -> v14.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V14
    ) -> v14.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V14
    ) -> v14.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V14
    ) -> v14.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V14
    ) -> v14.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V14
    ) -> v14.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V14
    ) -> v14.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V14
    ) -> v14.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V14
    ) -> v14.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V14
    ) -> v14.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V14
    ) -> v14.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V14
    ) -> v14.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V14
    ) -> v14.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V14
    ) -> v14.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V14
    ) -> v14.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V14
    ) -> v14.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V14
    ) -> v14.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V14
    ) -> v14.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V14
    ) -> v14.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V14
    ) -> v14.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V14
    ) -> v14.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V14
    ) -> v14.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V14,
    ) -> v14.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V14
    ) -> v14.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V14
    ) -> v14.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V14
    ) -> v14.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V14
    ) -> v14.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V14
    ) -> v14.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V14
    ) -> v14.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V14
    ) -> v14.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V14
    ) -> v14.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V14
    ) -> v14.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V14
    ) -> v14.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V14
    ) -> v14.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V14
    ) -> v14.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V14
    ) -> v14.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V14
    ) -> v14.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V14
    ) -> v14.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V14
    ) -> v14.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V14
    ) -> v14.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V14
    ) -> v14.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V14
    ) -> v14.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V14
    ) -> v14.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V14
    ) -> v14.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V14
    ) -> v14.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V14
    ) -> v14.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V14
    ) -> v14.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MediaFileService"], version: _V14
    ) -> v14.MediaFileServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MerchantCenterLinkService"], version: _V14
    ) -> v14.MerchantCenterLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V14
    ) -> v14.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V14
    ) -> v14.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V14
    ) -> v14.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V14
    ) -> v14.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V14
    ) -> v14.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V14
    ) -> v14.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V14
    ) -> v14.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V14
    ) -> v14.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V14
    ) -> v14.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V14
    ) -> v14.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V14
    ) -> v14.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V14
    ) -> v14.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V14
    ) -> v14.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V14
    ) -> v14.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V15
    ) -> v15.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V15
    ) -> v15.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V15
    ) -> v15.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V15
    ) -> v15.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V15
    ) -> v15.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V15
    ) -> v15.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V15
    ) -> v15.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V15
    ) -> v15.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V15
    ) -> v15.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V15
    ) -> v15.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V15
    ) -> v15.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V15
    ) -> v15.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V15
    ) -> v15.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V15
    ) -> v15.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V15
    ) -> v15.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V15
    ) -> v15.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V15
    ) -> v15.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V15
    ) -> v15.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V15
    ) -> v15.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V15
    ) -> v15.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V15
    ) -> v15.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V15
    ) -> v15.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V15
    ) -> v15.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V15
    ) -> v15.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V15
    ) -> v15.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V15
    ) -> v15.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V15
    ) -> v15.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V15
    ) -> v15.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V15
    ) -> v15.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V15
    ) -> v15.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V15
    ) -> v15.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V15
    ) -> v15.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V15
    ) -> v15.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V15
    ) -> v15.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V15
    ) -> v15.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V15
    ) -> v15.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V15
    ) -> v15.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V15
    ) -> v15.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V15
    ) -> v15.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V15
    ) -> v15.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V15
    ) -> v15.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V15
    ) -> v15.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V15
    ) -> v15.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V15
    ) -> v15.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V15
    ) -> v15.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V15
    ) -> v15.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V15
    ) -> v15.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V15
    ) -> v15.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V15
    ) -> v15.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V15
    ) -> v15.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V15
    ) -> v15.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V15
    ) -> v15.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V15
    ) -> v15.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V15
    ) -> v15.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V15
    ) -> v15.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V15
    ) -> v15.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V15
    ) -> v15.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V15
    ) -> v15.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V15
    ) -> v15.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V15
    ) -> v15.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V15
    ) -> v15.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V15
    ) -> v15.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V15
    ) -> v15.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V15
    ) -> v15.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V15
    ) -> v15.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V15
    ) -> v15.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V15
    ) -> v15.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V15
    ) -> v15.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V15
    ) -> v15.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V15
    ) -> v15.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V15,
    ) -> v15.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V15
    ) -> v15.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V15
    ) -> v15.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V15
    ) -> v15.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V15
    ) -> v15.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V15
    ) -> v15.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V15
    ) -> v15.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V15
    ) -> v15.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V15
    ) -> v15.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V15
    ) -> v15.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V15
    ) -> v15.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V15
    ) -> v15.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V15
    ) -> v15.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V15
    ) -> v15.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V15
    ) -> v15.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V15
    ) -> v15.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V15
    ) -> v15.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V15
    ) -> v15.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V15
    ) -> v15.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V15
    ) -> v15.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V15
    ) -> v15.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V15
    ) -> v15.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V15
    ) -> v15.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V15
    ) -> v15.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V15
    ) -> v15.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V15
    ) -> v15.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V15
    ) -> v15.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V15
    ) -> v15.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V15
    ) -> v15.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V15
    ) -> v15.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V15
    ) -> v15.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V15
    ) -> v15.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V15
    ) -> v15.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V15
    ) -> v15.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V15
    ) -> v15.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V15
    ) -> v15.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V15
    ) -> v15.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V15
    ) -> v15.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V15
    ) -> v15.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V15
    ) -> v15.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V15
    ) -> v15.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V16
    ) -> v16.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"]
    ) -> v16.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V16
    ) -> v16.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"]
    ) -> v16.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V16
    ) -> v16.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"]
    ) -> v16.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V16
    ) -> v16.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"]
    ) -> v16.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V16
    ) -> v16.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"]
    ) -> v16.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V16
    ) -> v16.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"]
    ) -> v16.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V16
    ) -> v16.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"]
    ) -> v16.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V16
    ) -> v16.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"]
    ) -> v16.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V16
    ) -> v16.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"]
    ) -> v16.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V16
    ) -> v16.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"]
    ) -> v16.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V16
    ) -> v16.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"]
    ) -> v16.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V16
    ) -> v16.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"]
    ) -> v16.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V16
    ) -> v16.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"]
    ) -> v16.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V16
    ) -> v16.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"]
    ) -> v16.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V16
    ) -> v16.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"]
    ) -> v16.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V16
    ) -> v16.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"]
    ) -> v16.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V16
    ) -> v16.AdServiceClient: ...
    @overload
    def get_service(self, name: Literal["AdService"]) -> v16.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V16
    ) -> v16.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"]
    ) -> v16.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V16
    ) -> v16.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"]
    ) -> v16.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V16
    ) -> v16.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"]
    ) -> v16.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V16
    ) -> v16.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"]
    ) -> v16.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V16
    ) -> v16.AssetServiceClient: ...
    @overload
    def get_service(self, name: Literal["AssetService"]) -> v16.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V16
    ) -> v16.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"]
    ) -> v16.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V16
    ) -> v16.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"]
    ) -> v16.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V16
    ) -> v16.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"]
    ) -> v16.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V16
    ) -> v16.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"]
    ) -> v16.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V16
    ) -> v16.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"]
    ) -> v16.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V16
    ) -> v16.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"]
    ) -> v16.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V16
    ) -> v16.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"]
    ) -> v16.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V16
    ) -> v16.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"]
    ) -> v16.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V16
    ) -> v16.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"]
    ) -> v16.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V16
    ) -> v16.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"]
    ) -> v16.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V16
    ) -> v16.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"]
    ) -> v16.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V16
    ) -> v16.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"]
    ) -> v16.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V16
    ) -> v16.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"]
    ) -> v16.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V16
    ) -> v16.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"]
    ) -> v16.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V16
    ) -> v16.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"]
    ) -> v16.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V16
    ) -> v16.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"]
    ) -> v16.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V16
    ) -> v16.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"]
    ) -> v16.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V16
    ) -> v16.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"]
    ) -> v16.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V16
    ) -> v16.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"]
    ) -> v16.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V16
    ) -> v16.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"]
    ) -> v16.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V16
    ) -> v16.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"]
    ) -> v16.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V16
    ) -> v16.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"]
    ) -> v16.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V16
    ) -> v16.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"]
    ) -> v16.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V16
    ) -> v16.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"]
    ) -> v16.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V16
    ) -> v16.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"]
    ) -> v16.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V16
    ) -> v16.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"]
    ) -> v16.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V16
    ) -> v16.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"]
    ) -> v16.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V16
    ) -> v16.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"]
    ) -> v16.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V16
    ) -> v16.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"]
    ) -> v16.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V16
    ) -> v16.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"]
    ) -> v16.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V16
    ) -> v16.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"]
    ) -> v16.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V16
    ) -> v16.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"]
    ) -> v16.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V16
    ) -> v16.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"]
    ) -> v16.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V16
    ) -> v16.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"]
    ) -> v16.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V16
    ) -> v16.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"]
    ) -> v16.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V16
    ) -> v16.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"]
    ) -> v16.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V16
    ) -> v16.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"]
    ) -> v16.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V16
    ) -> v16.CustomerClient: ...
    @overload
    def get_service(self, name: Literal["Customer"]) -> v16.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V16
    ) -> v16.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"]
    ) -> v16.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V16
    ) -> v16.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"]
    ) -> v16.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V16
    ) -> v16.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"]
    ) -> v16.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V16
    ) -> v16.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"]
    ) -> v16.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V16
    ) -> v16.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"]
    ) -> v16.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V16
    ) -> v16.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"]
    ) -> v16.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V16
    ) -> v16.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"]
    ) -> v16.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V16
    ) -> v16.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"]
    ) -> v16.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V16
    ) -> v16.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"]
    ) -> v16.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V16
    ) -> v16.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"]
    ) -> v16.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V16,
    ) -> v16.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerSkAdNetworkConversionValueSchemaService"]
    ) -> v16.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V16
    ) -> v16.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"]
    ) -> v16.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V16
    ) -> v16.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"]
    ) -> v16.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V16
    ) -> v16.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"]
    ) -> v16.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V16
    ) -> v16.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"]
    ) -> v16.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V16
    ) -> v16.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"]
    ) -> v16.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V16
    ) -> v16.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"]
    ) -> v16.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V16
    ) -> v16.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"]
    ) -> v16.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V16
    ) -> v16.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"]
    ) -> v16.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V16
    ) -> v16.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"]
    ) -> v16.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V16
    ) -> v16.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"]
    ) -> v16.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V16
    ) -> v16.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"]
    ) -> v16.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V16
    ) -> v16.FeedServiceClient: ...
    @overload
    def get_service(self, name: Literal["FeedService"]) -> v16.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V16
    ) -> v16.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"]
    ) -> v16.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V16
    ) -> v16.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"]
    ) -> v16.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V16
    ) -> v16.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"]
    ) -> v16.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"], version: _V16
    ) -> v16.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"]
    ) -> v16.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V16
    ) -> v16.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"]
    ) -> v16.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V16
    ) -> v16.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"]
    ) -> v16.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V16
    ) -> v16.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"]
    ) -> v16.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V16
    ) -> v16.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"]
    ) -> v16.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V16
    ) -> v16.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"]
    ) -> v16.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V16
    ) -> v16.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"]
    ) -> v16.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V16
    ) -> v16.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"]
    ) -> v16.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V16
    ) -> v16.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"]
    ) -> v16.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V16
    ) -> v16.LabelServiceClient: ...
    @overload
    def get_service(self, name: Literal["LabelService"]) -> v16.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V16
    ) -> v16.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"]
    ) -> v16.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V16
    ) -> v16.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"]
    ) -> v16.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V16
    ) -> v16.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"]
    ) -> v16.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V16
    ) -> v16.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"]
    ) -> v16.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V16
    ) -> v16.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"]
    ) -> v16.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V16
    ) -> v16.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"]
    ) -> v16.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V16
    ) -> v16.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"]
    ) -> v16.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V16
    ) -> v16.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"]
    ) -> v16.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V16
    ) -> v16.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"]
    ) -> v16.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V16
    ) -> v16.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"]
    ) -> v16.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V16
    ) -> v16.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"]
    ) -> v16.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V16
    ) -> v16.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"]
    ) -> v16.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V16
    ) -> v16.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"]
    ) -> v16.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V16
    ) -> v16.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"]
    ) -> v16.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V16
    ) -> v16.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"]
    ) -> v16.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V16
    ) -> v16.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"]
    ) -> v16.UserListServiceClient: ...
    @overload
    def get_service(self, name: str, version: _V = "v16") -> Any: ...
