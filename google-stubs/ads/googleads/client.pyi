import types
from typing import Any, overload

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

from google.ads.googleads import v16, v17
from google.ads.googleads.config import _ConfigDataUnparsed

_V16 = Literal["v16"]
_V17 = Literal["v17"]
_V = _V16 | _V17

class _EnumGetter:
    AccessInvitationStatusEnum: type[
        v17.AccessInvitationStatusEnum.AccessInvitationStatus
    ]
    AccessReasonEnum: type[v17.AccessReasonEnum.AccessReason]
    AccessRoleEnum: type[v17.AccessRoleEnum.AccessRole]
    AccountBudgetProposalStatusEnum: type[
        v17.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    ]
    AccountBudgetProposalTypeEnum: type[
        v17.AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    ]
    AccountBudgetStatusEnum: type[v17.AccountBudgetStatusEnum.AccountBudgetStatus]
    AccountLinkStatusEnum: type[v17.AccountLinkStatusEnum.AccountLinkStatus]
    AdCustomizerPlaceholderFieldEnum: type[
        v17.AdCustomizerPlaceholderFieldEnum.AdCustomizerPlaceholderField
    ]
    AdDestinationTypeEnum: type[v17.AdDestinationTypeEnum.AdDestinationType]
    AdFormatTypeEnum: type[v17.AdFormatTypeEnum.AdFormatType]
    AdGroupAdPrimaryStatusEnum: type[
        v17.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatus
    ]
    AdGroupAdPrimaryStatusReasonEnum: type[
        v17.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReason
    ]
    AdGroupAdRotationModeEnum: type[v17.AdGroupAdRotationModeEnum.AdGroupAdRotationMode]
    AdGroupAdStatusEnum: type[v17.AdGroupAdStatusEnum.AdGroupAdStatus]
    AdGroupCriterionApprovalStatusEnum: type[
        v17.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    ]
    AdGroupCriterionPrimaryStatusEnum: type[
        v17.AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    ]
    AdGroupCriterionPrimaryStatusReasonEnum: type[
        v17.AdGroupCriterionPrimaryStatusReasonEnum.AdGroupCriterionPrimaryStatusReason
    ]
    AdGroupCriterionStatusEnum: type[
        v17.AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    ]
    AdGroupPrimaryStatusEnum: type[v17.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatus]
    AdGroupPrimaryStatusReasonEnum: type[
        v17.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReason
    ]
    AdGroupStatusEnum: type[v17.AdGroupStatusEnum.AdGroupStatus]
    AdGroupTypeEnum: type[v17.AdGroupTypeEnum.AdGroupType]
    AdNetworkTypeEnum: type[v17.AdNetworkTypeEnum.AdNetworkType]
    AdServingOptimizationStatusEnum: type[
        v17.AdServingOptimizationStatusEnum.AdServingOptimizationStatus
    ]
    AdStrengthEnum: type[v17.AdStrengthEnum.AdStrength]
    AdTypeEnum: type[v17.AdTypeEnum.AdType]
    AdvertisingChannelSubTypeEnum: type[
        v17.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType
    ]
    AdvertisingChannelTypeEnum: type[
        v17.AdvertisingChannelTypeEnum.AdvertisingChannelType
    ]
    AffiliateLocationFeedRelationshipTypeEnum: type[
        v17.AffiliateLocationFeedRelationshipTypeEnum.AffiliateLocationFeedRelationshipType
    ]
    AffiliateLocationPlaceholderFieldEnum: type[
        v17.AffiliateLocationPlaceholderFieldEnum.AffiliateLocationPlaceholderField
    ]
    AgeRangeTypeEnum: type[v17.AgeRangeTypeEnum.AgeRangeType]
    AndroidPrivacyInteractionTypeEnum: type[
        v17.AndroidPrivacyInteractionTypeEnum.AndroidPrivacyInteractionType
    ]
    AndroidPrivacyNetworkTypeEnum: type[
        v17.AndroidPrivacyNetworkTypeEnum.AndroidPrivacyNetworkType
    ]
    AppBiddingGoalEnum: type[v17.AppBiddingGoalEnum.AppBiddingGoal]
    AppCampaignAppStoreEnum: type[v17.AppCampaignAppStoreEnum.AppCampaignAppStore]
    AppCampaignBiddingStrategyGoalTypeEnum: type[
        v17.AppCampaignBiddingStrategyGoalTypeEnum.AppCampaignBiddingStrategyGoalType
    ]
    AppPaymentModelTypeEnum: type[v17.AppPaymentModelTypeEnum.AppPaymentModelType]
    AppPlaceholderFieldEnum: type[v17.AppPlaceholderFieldEnum.AppPlaceholderField]
    AppStoreEnum: type[v17.AppStoreEnum.AppStore]
    AppUrlOperatingSystemTypeEnum: type[
        v17.AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    ]
    AssetAutomationStatusEnum: type[v17.AssetAutomationStatusEnum.AssetAutomationStatus]
    AssetAutomationTypeEnum: type[v17.AssetAutomationTypeEnum.AssetAutomationType]
    AssetFieldTypeEnum: type[v17.AssetFieldTypeEnum.AssetFieldType]
    AssetGroupPrimaryStatusEnum: type[
        v17.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    ]
    AssetGroupPrimaryStatusReasonEnum: type[
        v17.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason
    ]
    AssetGroupSignalApprovalStatusEnum: type[
        v17.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    ]
    AssetGroupStatusEnum: type[v17.AssetGroupStatusEnum.AssetGroupStatus]
    AssetLinkPrimaryStatusEnum: type[
        v17.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatus
    ]
    AssetLinkPrimaryStatusReasonEnum: type[
        v17.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReason
    ]
    AssetLinkStatusEnum: type[v17.AssetLinkStatusEnum.AssetLinkStatus]
    AssetOfflineEvaluationErrorReasonsEnum: type[
        v17.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasons
    ]
    AssetPerformanceLabelEnum: type[v17.AssetPerformanceLabelEnum.AssetPerformanceLabel]
    AssetSetAssetStatusEnum: type[v17.AssetSetAssetStatusEnum.AssetSetAssetStatus]
    AssetSetLinkStatusEnum: type[v17.AssetSetLinkStatusEnum.AssetSetLinkStatus]
    AssetSetStatusEnum: type[v17.AssetSetStatusEnum.AssetSetStatus]
    AssetSetTypeEnum: type[v17.AssetSetTypeEnum.AssetSetType]
    AssetSourceEnum: type[v17.AssetSourceEnum.AssetSource]
    AssetTypeEnum: type[v17.AssetTypeEnum.AssetType]
    AsyncActionStatusEnum: type[v17.AsyncActionStatusEnum.AsyncActionStatus]
    AttributionModelEnum: type[v17.AttributionModelEnum.AttributionModel]
    AudienceInsightsDimensionEnum: type[
        v17.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    ]
    AudienceScopeEnum: type[v17.AudienceScopeEnum.AudienceScope]
    AudienceStatusEnum: type[v17.AudienceStatusEnum.AudienceStatus]
    BatchJobStatusEnum: type[v17.BatchJobStatusEnum.BatchJobStatus]
    BidModifierSourceEnum: type[v17.BidModifierSourceEnum.BidModifierSource]
    BiddingSourceEnum: type[v17.BiddingSourceEnum.BiddingSource]
    BiddingStrategyStatusEnum: type[v17.BiddingStrategyStatusEnum.BiddingStrategyStatus]
    BiddingStrategySystemStatusEnum: type[
        v17.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatus
    ]
    BiddingStrategyTypeEnum: type[v17.BiddingStrategyTypeEnum.BiddingStrategyType]
    BillingSetupStatusEnum: type[v17.BillingSetupStatusEnum.BillingSetupStatus]
    BrandRequestRejectionReasonEnum: type[
        v17.BrandRequestRejectionReasonEnum.BrandRequestRejectionReason
    ]
    BrandSafetySuitabilityEnum: type[
        v17.BrandSafetySuitabilityEnum.BrandSafetySuitability
    ]
    BrandStateEnum: type[v17.BrandStateEnum.BrandState]
    BudgetCampaignAssociationStatusEnum: type[
        v17.BudgetCampaignAssociationStatusEnum.BudgetCampaignAssociationStatus
    ]
    BudgetDeliveryMethodEnum: type[v17.BudgetDeliveryMethodEnum.BudgetDeliveryMethod]
    BudgetPeriodEnum: type[v17.BudgetPeriodEnum.BudgetPeriod]
    BudgetStatusEnum: type[v17.BudgetStatusEnum.BudgetStatus]
    BudgetTypeEnum: type[v17.BudgetTypeEnum.BudgetType]
    CallConversionReportingStateEnum: type[
        v17.CallConversionReportingStateEnum.CallConversionReportingState
    ]
    CallPlaceholderFieldEnum: type[v17.CallPlaceholderFieldEnum.CallPlaceholderField]
    CallToActionTypeEnum: type[v17.CallToActionTypeEnum.CallToActionType]
    CallTrackingDisplayLocationEnum: type[
        v17.CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    ]
    CallTypeEnum: type[v17.CallTypeEnum.CallType]
    CalloutPlaceholderFieldEnum: type[
        v17.CalloutPlaceholderFieldEnum.CalloutPlaceholderField
    ]
    CampaignCriterionStatusEnum: type[
        v17.CampaignCriterionStatusEnum.CampaignCriterionStatus
    ]
    CampaignDraftStatusEnum: type[v17.CampaignDraftStatusEnum.CampaignDraftStatus]
    CampaignExperimentTypeEnum: type[
        v17.CampaignExperimentTypeEnum.CampaignExperimentType
    ]
    CampaignGroupStatusEnum: type[v17.CampaignGroupStatusEnum.CampaignGroupStatus]
    CampaignKeywordMatchTypeEnum: type[
        v17.CampaignKeywordMatchTypeEnum.CampaignKeywordMatchType
    ]
    CampaignPrimaryStatusEnum: type[v17.CampaignPrimaryStatusEnum.CampaignPrimaryStatus]
    CampaignPrimaryStatusReasonEnum: type[
        v17.CampaignPrimaryStatusReasonEnum.CampaignPrimaryStatusReason
    ]
    CampaignServingStatusEnum: type[v17.CampaignServingStatusEnum.CampaignServingStatus]
    CampaignSharedSetStatusEnum: type[
        v17.CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    ]
    CampaignStatusEnum: type[v17.CampaignStatusEnum.CampaignStatus]
    ChainRelationshipTypeEnum: type[v17.ChainRelationshipTypeEnum.ChainRelationshipType]
    ChangeClientTypeEnum: type[v17.ChangeClientTypeEnum.ChangeClientType]
    ChangeEventResourceTypeEnum: type[
        v17.ChangeEventResourceTypeEnum.ChangeEventResourceType
    ]
    ChangeStatusOperationEnum: type[v17.ChangeStatusOperationEnum.ChangeStatusOperation]
    ChangeStatusResourceTypeEnum: type[
        v17.ChangeStatusResourceTypeEnum.ChangeStatusResourceType
    ]
    ClickTypeEnum: type[v17.ClickTypeEnum.ClickType]
    CombinedAudienceStatusEnum: type[
        v17.CombinedAudienceStatusEnum.CombinedAudienceStatus
    ]
    ConsentStatusEnum: type[v17.ConsentStatusEnum.ConsentStatus]
    ContentLabelTypeEnum: type[v17.ContentLabelTypeEnum.ContentLabelType]
    ConversionActionCategoryEnum: type[
        v17.ConversionActionCategoryEnum.ConversionActionCategory
    ]
    ConversionActionCountingTypeEnum: type[
        v17.ConversionActionCountingTypeEnum.ConversionActionCountingType
    ]
    ConversionActionStatusEnum: type[
        v17.ConversionActionStatusEnum.ConversionActionStatus
    ]
    ConversionActionTypeEnum: type[v17.ConversionActionTypeEnum.ConversionActionType]
    ConversionAdjustmentTypeEnum: type[
        v17.ConversionAdjustmentTypeEnum.ConversionAdjustmentType
    ]
    ConversionAttributionEventTypeEnum: type[
        v17.ConversionAttributionEventTypeEnum.ConversionAttributionEventType
    ]
    ConversionCustomVariableStatusEnum: type[
        v17.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus
    ]
    ConversionEnvironmentEnum: type[v17.ConversionEnvironmentEnum.ConversionEnvironment]
    ConversionLagBucketEnum: type[v17.ConversionLagBucketEnum.ConversionLagBucket]
    ConversionOrAdjustmentLagBucketEnum: type[
        v17.ConversionOrAdjustmentLagBucketEnum.ConversionOrAdjustmentLagBucket
    ]
    ConversionOriginEnum: type[v17.ConversionOriginEnum.ConversionOrigin]
    ConversionTrackingStatusEnum: type[
        v17.ConversionTrackingStatusEnum.ConversionTrackingStatus
    ]
    ConversionValueRulePrimaryDimensionEnum: type[
        v17.ConversionValueRulePrimaryDimensionEnum.ConversionValueRulePrimaryDimension
    ]
    ConversionValueRuleSetStatusEnum: type[
        v17.ConversionValueRuleSetStatusEnum.ConversionValueRuleSetStatus
    ]
    ConversionValueRuleStatusEnum: type[
        v17.ConversionValueRuleStatusEnum.ConversionValueRuleStatus
    ]
    ConvertingUserPriorEngagementTypeAndLtvBucketEnum: type[
        v17.ConvertingUserPriorEngagementTypeAndLtvBucketEnum.ConvertingUserPriorEngagementTypeAndLtvBucket
    ]
    CriterionCategoryChannelAvailabilityModeEnum: type[
        v17.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode
    ]
    CriterionCategoryLocaleAvailabilityModeEnum: type[
        v17.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode
    ]
    CriterionSystemServingStatusEnum: type[
        v17.CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    ]
    CriterionTypeEnum: type[v17.CriterionTypeEnum.CriterionType]
    CustomAudienceMemberTypeEnum: type[
        v17.CustomAudienceMemberTypeEnum.CustomAudienceMemberType
    ]
    CustomAudienceStatusEnum: type[v17.CustomAudienceStatusEnum.CustomAudienceStatus]
    CustomAudienceTypeEnum: type[v17.CustomAudienceTypeEnum.CustomAudienceType]
    CustomConversionGoalStatusEnum: type[
        v17.CustomConversionGoalStatusEnum.CustomConversionGoalStatus
    ]
    CustomInterestMemberTypeEnum: type[
        v17.CustomInterestMemberTypeEnum.CustomInterestMemberType
    ]
    CustomInterestStatusEnum: type[v17.CustomInterestStatusEnum.CustomInterestStatus]
    CustomInterestTypeEnum: type[v17.CustomInterestTypeEnum.CustomInterestType]
    CustomPlaceholderFieldEnum: type[
        v17.CustomPlaceholderFieldEnum.CustomPlaceholderField
    ]
    CustomerAcquisitionOptimizationModeEnum: type[
        v17.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationMode
    ]
    CustomerMatchUploadKeyTypeEnum: type[
        v17.CustomerMatchUploadKeyTypeEnum.CustomerMatchUploadKeyType
    ]
    CustomerPayPerConversionEligibilityFailureReasonEnum: type[
        v17.CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
    ]
    CustomerStatusEnum: type[v17.CustomerStatusEnum.CustomerStatus]
    CustomizerAttributeStatusEnum: type[
        v17.CustomizerAttributeStatusEnum.CustomizerAttributeStatus
    ]
    CustomizerAttributeTypeEnum: type[
        v17.CustomizerAttributeTypeEnum.CustomizerAttributeType
    ]
    CustomizerValueStatusEnum: type[v17.CustomizerValueStatusEnum.CustomizerValueStatus]
    DataDrivenModelStatusEnum: type[v17.DataDrivenModelStatusEnum.DataDrivenModelStatus]
    DayOfWeekEnum: type[v17.DayOfWeekEnum.DayOfWeek]
    DeviceEnum: type[v17.DeviceEnum.Device]
    DisplayAdFormatSettingEnum: type[
        v17.DisplayAdFormatSettingEnum.DisplayAdFormatSetting
    ]
    DisplayUploadProductTypeEnum: type[
        v17.DisplayUploadProductTypeEnum.DisplayUploadProductType
    ]
    DistanceBucketEnum: type[v17.DistanceBucketEnum.DistanceBucket]
    DsaPageFeedCriterionFieldEnum: type[
        v17.DsaPageFeedCriterionFieldEnum.DsaPageFeedCriterionField
    ]
    EducationPlaceholderFieldEnum: type[
        v17.EducationPlaceholderFieldEnum.EducationPlaceholderField
    ]
    ExperimentMetricDirectionEnum: type[
        v17.ExperimentMetricDirectionEnum.ExperimentMetricDirection
    ]
    ExperimentMetricEnum: type[v17.ExperimentMetricEnum.ExperimentMetric]
    ExperimentStatusEnum: type[v17.ExperimentStatusEnum.ExperimentStatus]
    ExperimentTypeEnum: type[v17.ExperimentTypeEnum.ExperimentType]
    ExtensionSettingDeviceEnum: type[
        v17.ExtensionSettingDeviceEnum.ExtensionSettingDevice
    ]
    ExtensionTypeEnum: type[v17.ExtensionTypeEnum.ExtensionType]
    ExternalConversionSourceEnum: type[
        v17.ExternalConversionSourceEnum.ExternalConversionSource
    ]
    FeedAttributeTypeEnum: type[v17.FeedAttributeTypeEnum.FeedAttributeType]
    FeedItemQualityApprovalStatusEnum: type[
        v17.FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    ]
    FeedItemQualityDisapprovalReasonEnum: type[
        v17.FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
    ]
    FeedItemSetStatusEnum: type[v17.FeedItemSetStatusEnum.FeedItemSetStatus]
    FeedItemSetStringFilterTypeEnum: type[
        v17.FeedItemSetStringFilterTypeEnum.FeedItemSetStringFilterType
    ]
    FeedItemStatusEnum: type[v17.FeedItemStatusEnum.FeedItemStatus]
    FeedItemTargetDeviceEnum: type[v17.FeedItemTargetDeviceEnum.FeedItemTargetDevice]
    FeedItemTargetStatusEnum: type[v17.FeedItemTargetStatusEnum.FeedItemTargetStatus]
    FeedItemTargetTypeEnum: type[v17.FeedItemTargetTypeEnum.FeedItemTargetType]
    FeedItemValidationStatusEnum: type[
        v17.FeedItemValidationStatusEnum.FeedItemValidationStatus
    ]
    FeedLinkStatusEnum: type[v17.FeedLinkStatusEnum.FeedLinkStatus]
    FeedMappingCriterionTypeEnum: type[
        v17.FeedMappingCriterionTypeEnum.FeedMappingCriterionType
    ]
    FeedMappingStatusEnum: type[v17.FeedMappingStatusEnum.FeedMappingStatus]
    FeedOriginEnum: type[v17.FeedOriginEnum.FeedOrigin]
    FeedStatusEnum: type[v17.FeedStatusEnum.FeedStatus]
    FixedCpmGoalEnum: type[v17.FixedCpmGoalEnum.FixedCpmGoal]
    FixedCpmTargetFrequencyTimeUnitEnum: type[
        v17.FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit
    ]
    FlightPlaceholderFieldEnum: type[
        v17.FlightPlaceholderFieldEnum.FlightPlaceholderField
    ]
    FrequencyCapEventTypeEnum: type[v17.FrequencyCapEventTypeEnum.FrequencyCapEventType]
    FrequencyCapLevelEnum: type[v17.FrequencyCapLevelEnum.FrequencyCapLevel]
    FrequencyCapTimeUnitEnum: type[v17.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit]
    GenderTypeEnum: type[v17.GenderTypeEnum.GenderType]
    GeoTargetConstantStatusEnum: type[
        v17.GeoTargetConstantStatusEnum.GeoTargetConstantStatus
    ]
    GeoTargetingRestrictionEnum: type[
        v17.GeoTargetingRestrictionEnum.GeoTargetingRestriction
    ]
    GeoTargetingTypeEnum: type[v17.GeoTargetingTypeEnum.GeoTargetingType]
    GoalConfigLevelEnum: type[v17.GoalConfigLevelEnum.GoalConfigLevel]
    GoogleAdsFieldCategoryEnum: type[
        v17.GoogleAdsFieldCategoryEnum.GoogleAdsFieldCategory
    ]
    GoogleAdsFieldDataTypeEnum: type[
        v17.GoogleAdsFieldDataTypeEnum.GoogleAdsFieldDataType
    ]
    GoogleVoiceCallStatusEnum: type[v17.GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus]
    HotelAssetSuggestionStatusEnum: type[
        v17.HotelAssetSuggestionStatusEnum.HotelAssetSuggestionStatus
    ]
    HotelDateSelectionTypeEnum: type[
        v17.HotelDateSelectionTypeEnum.HotelDateSelectionType
    ]
    HotelPlaceholderFieldEnum: type[v17.HotelPlaceholderFieldEnum.HotelPlaceholderField]
    HotelPriceBucketEnum: type[v17.HotelPriceBucketEnum.HotelPriceBucket]
    HotelRateTypeEnum: type[v17.HotelRateTypeEnum.HotelRateType]
    HotelReconciliationStatusEnum: type[
        v17.HotelReconciliationStatusEnum.HotelReconciliationStatus
    ]
    IdentityVerificationProgramEnum: type[
        v17.IdentityVerificationProgramEnum.IdentityVerificationProgram
    ]
    IdentityVerificationProgramStatusEnum: type[
        v17.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    ]
    ImagePlaceholderFieldEnum: type[v17.ImagePlaceholderFieldEnum.ImagePlaceholderField]
    IncomeRangeTypeEnum: type[v17.IncomeRangeTypeEnum.IncomeRangeType]
    InteractionEventTypeEnum: type[v17.InteractionEventTypeEnum.InteractionEventType]
    InteractionTypeEnum: type[v17.InteractionTypeEnum.InteractionType]
    InvoiceTypeEnum: type[v17.InvoiceTypeEnum.InvoiceType]
    JobPlaceholderFieldEnum: type[v17.JobPlaceholderFieldEnum.JobPlaceholderField]
    KeywordMatchTypeEnum: type[v17.KeywordMatchTypeEnum.KeywordMatchType]
    KeywordPlanAggregateMetricTypeEnum: type[
        v17.KeywordPlanAggregateMetricTypeEnum.KeywordPlanAggregateMetricType
    ]
    KeywordPlanCompetitionLevelEnum: type[
        v17.KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    ]
    KeywordPlanConceptGroupTypeEnum: type[
        v17.KeywordPlanConceptGroupTypeEnum.KeywordPlanConceptGroupType
    ]
    KeywordPlanForecastIntervalEnum: type[
        v17.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    ]
    KeywordPlanKeywordAnnotationEnum: type[
        v17.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation
    ]
    KeywordPlanNetworkEnum: type[v17.KeywordPlanNetworkEnum.KeywordPlanNetwork]
    LabelStatusEnum: type[v17.LabelStatusEnum.LabelStatus]
    LeadFormCallToActionTypeEnum: type[
        v17.LeadFormCallToActionTypeEnum.LeadFormCallToActionType
    ]
    LeadFormDesiredIntentEnum: type[v17.LeadFormDesiredIntentEnum.LeadFormDesiredIntent]
    LeadFormFieldUserInputTypeEnum: type[
        v17.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType
    ]
    LeadFormPostSubmitCallToActionTypeEnum: type[
        v17.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType
    ]
    LegacyAppInstallAdAppStoreEnum: type[
        v17.LegacyAppInstallAdAppStoreEnum.LegacyAppInstallAdAppStore
    ]
    LinkedAccountTypeEnum: type[v17.LinkedAccountTypeEnum.LinkedAccountType]
    LinkedProductTypeEnum: type[v17.LinkedProductTypeEnum.LinkedProductType]
    ListingGroupFilterCustomAttributeIndexEnum: type[
        v17.ListingGroupFilterCustomAttributeIndexEnum.ListingGroupFilterCustomAttributeIndex
    ]
    ListingGroupFilterListingSourceEnum: type[
        v17.ListingGroupFilterListingSourceEnum.ListingGroupFilterListingSource
    ]
    ListingGroupFilterProductCategoryLevelEnum: type[
        v17.ListingGroupFilterProductCategoryLevelEnum.ListingGroupFilterProductCategoryLevel
    ]
    ListingGroupFilterProductChannelEnum: type[
        v17.ListingGroupFilterProductChannelEnum.ListingGroupFilterProductChannel
    ]
    ListingGroupFilterProductConditionEnum: type[
        v17.ListingGroupFilterProductConditionEnum.ListingGroupFilterProductCondition
    ]
    ListingGroupFilterProductTypeLevelEnum: type[
        v17.ListingGroupFilterProductTypeLevelEnum.ListingGroupFilterProductTypeLevel
    ]
    ListingGroupFilterTypeEnum: type[
        v17.ListingGroupFilterTypeEnum.ListingGroupFilterType
    ]
    ListingGroupTypeEnum: type[v17.ListingGroupTypeEnum.ListingGroupType]
    ListingTypeEnum: type[v17.ListingTypeEnum.ListingType]
    LocalPlaceholderFieldEnum: type[v17.LocalPlaceholderFieldEnum.LocalPlaceholderField]
    LocalServicesBusinessRegistrationCheckRejectionReasonEnum: type[
        v17.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReason
    ]
    LocalServicesBusinessRegistrationTypeEnum: type[
        v17.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    ]
    LocalServicesCreditStateEnum: type[v17.LocalServicesCreditStateEnum.CreditState]
    LocalServicesEmployeeStatusEnum: type[
        v17.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatus
    ]
    LocalServicesEmployeeTypeEnum: type[
        v17.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeType
    ]
    LocalServicesInsuranceRejectionReasonEnum: type[
        v17.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    ]
    LocalServicesLeadConversationTypeEnum: type[
        v17.LocalServicesLeadConversationTypeEnum.ConversationType
    ]
    LocalServicesLeadStatusEnum: type[v17.LocalServicesLeadStatusEnum.LeadStatus]
    LocalServicesLeadTypeEnum: type[v17.LocalServicesLeadTypeEnum.LeadType]
    LocalServicesLicenseRejectionReasonEnum: type[
        v17.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    ]
    LocalServicesParticipantTypeEnum: type[
        v17.LocalServicesParticipantTypeEnum.ParticipantType
    ]
    LocalServicesVerificationArtifactStatusEnum: type[
        v17.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    ]
    LocalServicesVerificationArtifactTypeEnum: type[
        v17.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    ]
    LocalServicesVerificationStatusEnum: type[
        v17.LocalServicesVerificationStatusEnum.LocalServicesVerificationStatus
    ]
    LocationExtensionTargetingCriterionFieldEnum: type[
        v17.LocationExtensionTargetingCriterionFieldEnum.LocationExtensionTargetingCriterionField
    ]
    LocationGroupRadiusUnitsEnum: type[
        v17.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits
    ]
    LocationOwnershipTypeEnum: type[v17.LocationOwnershipTypeEnum.LocationOwnershipType]
    LocationPlaceholderFieldEnum: type[
        v17.LocationPlaceholderFieldEnum.LocationPlaceholderField
    ]
    LocationSourceTypeEnum: type[v17.LocationSourceTypeEnum.LocationSourceType]
    LocationStringFilterTypeEnum: type[
        v17.LocationStringFilterTypeEnum.LocationStringFilterType
    ]
    LookalikeExpansionLevelEnum: type[
        v17.LookalikeExpansionLevelEnum.LookalikeExpansionLevel
    ]
    ManagerLinkStatusEnum: type[v17.ManagerLinkStatusEnum.ManagerLinkStatus]
    MatchingFunctionContextTypeEnum: type[
        v17.MatchingFunctionContextTypeEnum.MatchingFunctionContextType
    ]
    MatchingFunctionOperatorEnum: type[
        v17.MatchingFunctionOperatorEnum.MatchingFunctionOperator
    ]
    MediaTypeEnum: type[v17.MediaTypeEnum.MediaType]
    MessagePlaceholderFieldEnum: type[
        v17.MessagePlaceholderFieldEnum.MessagePlaceholderField
    ]
    MimeTypeEnum: type[v17.MimeTypeEnum.MimeType]
    MinuteOfHourEnum: type[v17.MinuteOfHourEnum.MinuteOfHour]
    MobileAppVendorEnum: type[v17.MobileAppVendorEnum.MobileAppVendor]
    MobileDeviceTypeEnum: type[v17.MobileDeviceTypeEnum.MobileDeviceType]
    MonthOfYearEnum: type[v17.MonthOfYearEnum.MonthOfYear]
    NegativeGeoTargetTypeEnum: type[v17.NegativeGeoTargetTypeEnum.NegativeGeoTargetType]
    OfflineConversionDiagnosticStatusEnum: type[
        v17.OfflineConversionDiagnosticStatusEnum.OfflineConversionDiagnosticStatus
    ]
    OfflineEventUploadClientEnum: type[
        v17.OfflineEventUploadClientEnum.OfflineEventUploadClient
    ]
    OfflineUserDataJobFailureReasonEnum: type[
        v17.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReason
    ]
    OfflineUserDataJobMatchRateRangeEnum: type[
        v17.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRange
    ]
    OfflineUserDataJobStatusEnum: type[
        v17.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatus
    ]
    OfflineUserDataJobTypeEnum: type[
        v17.OfflineUserDataJobTypeEnum.OfflineUserDataJobType
    ]
    OperatingSystemVersionOperatorTypeEnum: type[
        v17.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType
    ]
    OptimizationGoalTypeEnum: type[v17.OptimizationGoalTypeEnum.OptimizationGoalType]
    ParentalStatusTypeEnum: type[v17.ParentalStatusTypeEnum.ParentalStatusType]
    PaymentModeEnum: type[v17.PaymentModeEnum.PaymentMode]
    PerformanceMaxUpgradeStatusEnum: type[
        v17.PerformanceMaxUpgradeStatusEnum.PerformanceMaxUpgradeStatus
    ]
    PlaceholderTypeEnum: type[v17.PlaceholderTypeEnum.PlaceholderType]
    PlacementTypeEnum: type[v17.PlacementTypeEnum.PlacementType]
    PolicyApprovalStatusEnum: type[v17.PolicyApprovalStatusEnum.PolicyApprovalStatus]
    PolicyReviewStatusEnum: type[v17.PolicyReviewStatusEnum.PolicyReviewStatus]
    PolicyTopicEntryTypeEnum: type[v17.PolicyTopicEntryTypeEnum.PolicyTopicEntryType]
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum: type[
        v17.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
    ]
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum: type[
        v17.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
    ]
    PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum: type[
        v17.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
    ]
    PositiveGeoTargetTypeEnum: type[v17.PositiveGeoTargetTypeEnum.PositiveGeoTargetType]
    PriceExtensionPriceQualifierEnum: type[
        v17.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier
    ]
    PriceExtensionPriceUnitEnum: type[
        v17.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit
    ]
    PriceExtensionTypeEnum: type[v17.PriceExtensionTypeEnum.PriceExtensionType]
    PricePlaceholderFieldEnum: type[v17.PricePlaceholderFieldEnum.PricePlaceholderField]
    ProductAvailabilityEnum: type[v17.ProductAvailabilityEnum.ProductAvailability]
    ProductCategoryLevelEnum: type[v17.ProductCategoryLevelEnum.ProductCategoryLevel]
    ProductCategoryStateEnum: type[v17.ProductCategoryStateEnum.ProductCategoryState]
    ProductChannelEnum: type[v17.ProductChannelEnum.ProductChannel]
    ProductChannelExclusivityEnum: type[
        v17.ProductChannelExclusivityEnum.ProductChannelExclusivity
    ]
    ProductConditionEnum: type[v17.ProductConditionEnum.ProductCondition]
    ProductCustomAttributeIndexEnum: type[
        v17.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndex
    ]
    ProductIssueSeverityEnum: type[v17.ProductIssueSeverityEnum.ProductIssueSeverity]
    ProductLinkInvitationStatusEnum: type[
        v17.ProductLinkInvitationStatusEnum.ProductLinkInvitationStatus
    ]
    ProductStatusEnum: type[v17.ProductStatusEnum.ProductStatus]
    ProductTypeLevelEnum: type[v17.ProductTypeLevelEnum.ProductTypeLevel]
    PromotionExtensionDiscountModifierEnum: type[
        v17.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier
    ]
    PromotionExtensionOccasionEnum: type[
        v17.PromotionExtensionOccasionEnum.PromotionExtensionOccasion
    ]
    PromotionPlaceholderFieldEnum: type[
        v17.PromotionPlaceholderFieldEnum.PromotionPlaceholderField
    ]
    ProximityRadiusUnitsEnum: type[v17.ProximityRadiusUnitsEnum.ProximityRadiusUnits]
    QualityScoreBucketEnum: type[v17.QualityScoreBucketEnum.QualityScoreBucket]
    ReachPlanAgeRangeEnum: type[v17.ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    ReachPlanNetworkEnum: type[v17.ReachPlanNetworkEnum.ReachPlanNetwork]
    ReachPlanSurfaceEnum: type[v17.ReachPlanSurfaceEnum.ReachPlanSurface]
    RealEstatePlaceholderFieldEnum: type[
        v17.RealEstatePlaceholderFieldEnum.RealEstatePlaceholderField
    ]
    RecommendationSubscriptionStatusEnum: type[
        v17.RecommendationSubscriptionStatusEnum.RecommendationSubscriptionStatus
    ]
    RecommendationTypeEnum: type[v17.RecommendationTypeEnum.RecommendationType]
    ResourceChangeOperationEnum: type[
        v17.ResourceChangeOperationEnum.ResourceChangeOperation
    ]
    ResourceLimitTypeEnum: type[v17.ResourceLimitTypeEnum.ResourceLimitType]
    ResponseContentTypeEnum: type[v17.ResponseContentTypeEnum.ResponseContentType]
    SearchEngineResultsPageTypeEnum: type[
        v17.SearchEngineResultsPageTypeEnum.SearchEngineResultsPageType
    ]
    SearchTermMatchTypeEnum: type[v17.SearchTermMatchTypeEnum.SearchTermMatchType]
    SearchTermTargetingStatusEnum: type[
        v17.SearchTermTargetingStatusEnum.SearchTermTargetingStatus
    ]
    SeasonalityEventScopeEnum: type[v17.SeasonalityEventScopeEnum.SeasonalityEventScope]
    SeasonalityEventStatusEnum: type[
        v17.SeasonalityEventStatusEnum.SeasonalityEventStatus
    ]
    ServedAssetFieldTypeEnum: type[v17.ServedAssetFieldTypeEnum.ServedAssetFieldType]
    SharedSetStatusEnum: type[v17.SharedSetStatusEnum.SharedSetStatus]
    SharedSetTypeEnum: type[v17.SharedSetTypeEnum.SharedSetType]
    ShoppingAddProductsToCampaignRecommendationEnum: type[
        v17.ShoppingAddProductsToCampaignRecommendationEnum.Reason
    ]
    SimulationModificationMethodEnum: type[
        v17.SimulationModificationMethodEnum.SimulationModificationMethod
    ]
    SimulationTypeEnum: type[v17.SimulationTypeEnum.SimulationType]
    SitelinkPlaceholderFieldEnum: type[
        v17.SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField
    ]
    SkAdNetworkAdEventTypeEnum: type[
        v17.SkAdNetworkAdEventTypeEnum.SkAdNetworkAdEventType
    ]
    SkAdNetworkAttributionCreditEnum: type[
        v17.SkAdNetworkAttributionCreditEnum.SkAdNetworkAttributionCredit
    ]
    SkAdNetworkCoarseConversionValueEnum: type[
        v17.SkAdNetworkCoarseConversionValueEnum.SkAdNetworkCoarseConversionValue
    ]
    SkAdNetworkSourceTypeEnum: type[v17.SkAdNetworkSourceTypeEnum.SkAdNetworkSourceType]
    SkAdNetworkUserTypeEnum: type[v17.SkAdNetworkUserTypeEnum.SkAdNetworkUserType]
    SlotEnum: type[v17.SlotEnum.Slot]
    SmartCampaignNotEligibleReasonEnum: type[
        v17.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    ]
    SmartCampaignStatusEnum: type[v17.SmartCampaignStatusEnum.SmartCampaignStatus]
    SpendingLimitTypeEnum: type[v17.SpendingLimitTypeEnum.SpendingLimitType]
    StructuredSnippetPlaceholderFieldEnum: type[
        v17.StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderField
    ]
    SummaryRowSettingEnum: type[v17.SummaryRowSettingEnum.SummaryRowSetting]
    SystemManagedResourceSourceEnum: type[
        v17.SystemManagedResourceSourceEnum.SystemManagedResourceSource
    ]
    TargetCpaOptInRecommendationGoalEnum: type[
        v17.TargetCpaOptInRecommendationGoalEnum.TargetCpaOptInRecommendationGoal
    ]
    TargetFrequencyTimeUnitEnum: type[
        v17.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    ]
    TargetImpressionShareLocationEnum: type[
        v17.TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    ]
    TargetingDimensionEnum: type[v17.TargetingDimensionEnum.TargetingDimension]
    TimeTypeEnum: type[v17.TimeTypeEnum.TimeType]
    TrackingCodePageFormatEnum: type[
        v17.TrackingCodePageFormatEnum.TrackingCodePageFormat
    ]
    TrackingCodeTypeEnum: type[v17.TrackingCodeTypeEnum.TrackingCodeType]
    TravelPlaceholderFieldEnum: type[
        v17.TravelPlaceholderFieldEnum.TravelPlaceholderField
    ]
    UserIdentifierSourceEnum: type[v17.UserIdentifierSourceEnum.UserIdentifierSource]
    UserInterestTaxonomyTypeEnum: type[
        v17.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType
    ]
    UserListAccessStatusEnum: type[v17.UserListAccessStatusEnum.UserListAccessStatus]
    UserListClosingReasonEnum: type[v17.UserListClosingReasonEnum.UserListClosingReason]
    UserListCrmDataSourceTypeEnum: type[
        v17.UserListCrmDataSourceTypeEnum.UserListCrmDataSourceType
    ]
    UserListCustomerTypeCategoryEnum: type[
        v17.UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory
    ]
    UserListDateRuleItemOperatorEnum: type[
        v17.UserListDateRuleItemOperatorEnum.UserListDateRuleItemOperator
    ]
    UserListFlexibleRuleOperatorEnum: type[
        v17.UserListFlexibleRuleOperatorEnum.UserListFlexibleRuleOperator
    ]
    UserListLogicalRuleOperatorEnum: type[
        v17.UserListLogicalRuleOperatorEnum.UserListLogicalRuleOperator
    ]
    UserListMembershipStatusEnum: type[
        v17.UserListMembershipStatusEnum.UserListMembershipStatus
    ]
    UserListNumberRuleItemOperatorEnum: type[
        v17.UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator
    ]
    UserListPrepopulationStatusEnum: type[
        v17.UserListPrepopulationStatusEnum.UserListPrepopulationStatus
    ]
    UserListRuleTypeEnum: type[v17.UserListRuleTypeEnum.UserListRuleType]
    UserListSizeRangeEnum: type[v17.UserListSizeRangeEnum.UserListSizeRange]
    UserListStringRuleItemOperatorEnum: type[
        v17.UserListStringRuleItemOperatorEnum.UserListStringRuleItemOperator
    ]
    UserListTypeEnum: type[v17.UserListTypeEnum.UserListType]
    ValueRuleDeviceTypeEnum: type[v17.ValueRuleDeviceTypeEnum.ValueRuleDeviceType]
    ValueRuleGeoLocationMatchTypeEnum: type[
        v17.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchType
    ]
    ValueRuleOperationEnum: type[v17.ValueRuleOperationEnum.ValueRuleOperation]
    ValueRuleSetAttachmentTypeEnum: type[
        v17.ValueRuleSetAttachmentTypeEnum.ValueRuleSetAttachmentType
    ]
    ValueRuleSetDimensionEnum: type[v17.ValueRuleSetDimensionEnum.ValueRuleSetDimension]
    VanityPharmaDisplayUrlModeEnum: type[
        v17.VanityPharmaDisplayUrlModeEnum.VanityPharmaDisplayUrlMode
    ]
    VanityPharmaTextEnum: type[v17.VanityPharmaTextEnum.VanityPharmaText]
    VideoThumbnailEnum: type[v17.VideoThumbnailEnum.VideoThumbnail]
    WebpageConditionOperandEnum: type[
        v17.WebpageConditionOperandEnum.WebpageConditionOperand
    ]
    WebpageConditionOperatorEnum: type[
        v17.WebpageConditionOperatorEnum.WebpageConditionOperator
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
    def get_type(cls, name: str, version: _V = "v17") -> Any: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V16
    ) -> v16.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V16
    ) -> v16.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V16
    ) -> v16.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V16
    ) -> v16.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V16
    ) -> v16.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V16
    ) -> v16.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V16
    ) -> v16.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V16
    ) -> v16.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V16
    ) -> v16.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V16
    ) -> v16.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V16
    ) -> v16.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V16
    ) -> v16.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V16
    ) -> v16.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V16
    ) -> v16.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V16
    ) -> v16.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V16
    ) -> v16.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V16
    ) -> v16.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V16
    ) -> v16.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V16
    ) -> v16.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V16
    ) -> v16.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V16
    ) -> v16.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V16
    ) -> v16.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V16
    ) -> v16.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V16
    ) -> v16.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V16
    ) -> v16.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V16
    ) -> v16.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V16
    ) -> v16.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V16
    ) -> v16.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V16
    ) -> v16.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V16
    ) -> v16.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V16
    ) -> v16.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V16
    ) -> v16.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V16
    ) -> v16.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V16
    ) -> v16.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V16
    ) -> v16.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V16
    ) -> v16.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V16
    ) -> v16.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V16
    ) -> v16.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V16
    ) -> v16.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V16
    ) -> v16.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V16
    ) -> v16.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V16
    ) -> v16.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V16
    ) -> v16.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V16
    ) -> v16.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V16
    ) -> v16.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V16
    ) -> v16.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V16
    ) -> v16.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V16
    ) -> v16.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V16
    ) -> v16.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V16
    ) -> v16.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V16
    ) -> v16.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V16
    ) -> v16.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V16
    ) -> v16.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V16
    ) -> v16.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V16
    ) -> v16.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V16
    ) -> v16.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V16
    ) -> v16.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V16
    ) -> v16.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V16
    ) -> v16.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V16
    ) -> v16.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V16
    ) -> v16.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V16
    ) -> v16.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V16
    ) -> v16.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V16
    ) -> v16.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V16
    ) -> v16.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V16
    ) -> v16.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V16
    ) -> v16.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V16
    ) -> v16.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V16
    ) -> v16.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V16
    ) -> v16.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V16,
    ) -> v16.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V16
    ) -> v16.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V16
    ) -> v16.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V16
    ) -> v16.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V16
    ) -> v16.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V16
    ) -> v16.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V16
    ) -> v16.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V16
    ) -> v16.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V16
    ) -> v16.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V16
    ) -> v16.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V16
    ) -> v16.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V16
    ) -> v16.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V16
    ) -> v16.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V16
    ) -> v16.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V16
    ) -> v16.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V16
    ) -> v16.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"], version: _V16
    ) -> v16.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V16
    ) -> v16.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V16
    ) -> v16.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V16
    ) -> v16.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V16
    ) -> v16.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V16
    ) -> v16.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V16
    ) -> v16.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V16
    ) -> v16.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V16
    ) -> v16.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V16
    ) -> v16.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V16
    ) -> v16.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V16
    ) -> v16.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V16
    ) -> v16.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V16
    ) -> v16.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V16
    ) -> v16.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V16
    ) -> v16.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V16
    ) -> v16.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V16
    ) -> v16.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V16
    ) -> v16.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V16
    ) -> v16.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V16
    ) -> v16.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V16
    ) -> v16.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V16
    ) -> v16.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V16
    ) -> v16.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V16
    ) -> v16.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V16
    ) -> v16.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V17
    ) -> v17.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"]
    ) -> v17.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V17
    ) -> v17.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"]
    ) -> v17.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V17
    ) -> v17.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"]
    ) -> v17.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V17
    ) -> v17.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"]
    ) -> v17.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V17
    ) -> v17.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"]
    ) -> v17.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V17
    ) -> v17.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"]
    ) -> v17.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V17
    ) -> v17.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"]
    ) -> v17.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V17
    ) -> v17.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"]
    ) -> v17.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V17
    ) -> v17.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"]
    ) -> v17.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V17
    ) -> v17.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"]
    ) -> v17.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V17
    ) -> v17.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"]
    ) -> v17.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V17
    ) -> v17.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"]
    ) -> v17.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V17
    ) -> v17.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"]
    ) -> v17.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V17
    ) -> v17.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"]
    ) -> v17.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V17
    ) -> v17.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"]
    ) -> v17.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V17
    ) -> v17.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"]
    ) -> v17.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V17
    ) -> v17.AdServiceClient: ...
    @overload
    def get_service(self, name: Literal["AdService"]) -> v17.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V17
    ) -> v17.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"]
    ) -> v17.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V17
    ) -> v17.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"]
    ) -> v17.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V17
    ) -> v17.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"]
    ) -> v17.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V17
    ) -> v17.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"]
    ) -> v17.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V17
    ) -> v17.AssetServiceClient: ...
    @overload
    def get_service(self, name: Literal["AssetService"]) -> v17.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V17
    ) -> v17.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"]
    ) -> v17.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V17
    ) -> v17.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"]
    ) -> v17.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V17
    ) -> v17.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"]
    ) -> v17.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V17
    ) -> v17.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"]
    ) -> v17.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V17
    ) -> v17.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"]
    ) -> v17.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V17
    ) -> v17.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"]
    ) -> v17.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V17
    ) -> v17.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"]
    ) -> v17.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V17
    ) -> v17.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"]
    ) -> v17.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V17
    ) -> v17.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"]
    ) -> v17.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V17
    ) -> v17.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"]
    ) -> v17.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V17
    ) -> v17.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"]
    ) -> v17.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V17
    ) -> v17.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"]
    ) -> v17.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V17
    ) -> v17.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"]
    ) -> v17.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V17
    ) -> v17.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"]
    ) -> v17.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V17
    ) -> v17.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"]
    ) -> v17.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V17
    ) -> v17.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"]
    ) -> v17.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V17
    ) -> v17.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"]
    ) -> v17.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V17
    ) -> v17.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"]
    ) -> v17.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V17
    ) -> v17.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"]
    ) -> v17.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V17
    ) -> v17.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"]
    ) -> v17.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V17
    ) -> v17.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"]
    ) -> v17.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V17
    ) -> v17.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"]
    ) -> v17.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V17
    ) -> v17.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"]
    ) -> v17.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V17
    ) -> v17.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"]
    ) -> v17.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V17
    ) -> v17.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"]
    ) -> v17.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V17
    ) -> v17.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"]
    ) -> v17.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V17
    ) -> v17.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"]
    ) -> v17.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V17
    ) -> v17.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"]
    ) -> v17.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V17
    ) -> v17.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"]
    ) -> v17.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V17
    ) -> v17.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"]
    ) -> v17.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V17
    ) -> v17.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"]
    ) -> v17.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V17
    ) -> v17.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"]
    ) -> v17.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V17
    ) -> v17.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"]
    ) -> v17.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V17
    ) -> v17.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"]
    ) -> v17.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V17
    ) -> v17.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"]
    ) -> v17.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V17
    ) -> v17.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"]
    ) -> v17.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V17
    ) -> v17.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"]
    ) -> v17.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V17
    ) -> v17.CustomerClient: ...
    @overload
    def get_service(self, name: Literal["Customer"]) -> v17.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V17
    ) -> v17.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"]
    ) -> v17.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V17
    ) -> v17.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"]
    ) -> v17.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V17
    ) -> v17.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"]
    ) -> v17.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V17
    ) -> v17.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"]
    ) -> v17.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V17
    ) -> v17.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"]
    ) -> v17.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V17
    ) -> v17.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"]
    ) -> v17.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V17
    ) -> v17.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"]
    ) -> v17.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V17
    ) -> v17.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"]
    ) -> v17.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V17
    ) -> v17.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"]
    ) -> v17.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V17
    ) -> v17.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"]
    ) -> v17.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V17,
    ) -> v17.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerSkAdNetworkConversionValueSchemaService"]
    ) -> v17.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V17
    ) -> v17.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"]
    ) -> v17.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V17
    ) -> v17.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"]
    ) -> v17.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V17
    ) -> v17.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"]
    ) -> v17.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V17
    ) -> v17.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"]
    ) -> v17.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V17
    ) -> v17.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"]
    ) -> v17.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V17
    ) -> v17.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"]
    ) -> v17.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V17
    ) -> v17.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"]
    ) -> v17.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V17
    ) -> v17.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"]
    ) -> v17.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V17
    ) -> v17.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"]
    ) -> v17.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V17
    ) -> v17.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"]
    ) -> v17.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V17
    ) -> v17.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"]
    ) -> v17.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V17
    ) -> v17.FeedServiceClient: ...
    @overload
    def get_service(self, name: Literal["FeedService"]) -> v17.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V17
    ) -> v17.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"]
    ) -> v17.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V17
    ) -> v17.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"]
    ) -> v17.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V17
    ) -> v17.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"]
    ) -> v17.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"], version: _V17
    ) -> v17.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["IdentityVerificationService"]
    ) -> v17.IdentityVerificationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V17
    ) -> v17.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"]
    ) -> v17.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V17
    ) -> v17.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"]
    ) -> v17.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V17
    ) -> v17.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"]
    ) -> v17.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V17
    ) -> v17.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"]
    ) -> v17.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V17
    ) -> v17.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"]
    ) -> v17.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V17
    ) -> v17.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"]
    ) -> v17.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V17
    ) -> v17.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"]
    ) -> v17.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V17
    ) -> v17.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"]
    ) -> v17.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V17
    ) -> v17.LabelServiceClient: ...
    @overload
    def get_service(self, name: Literal["LabelService"]) -> v17.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadService"], version: _V17
    ) -> v17.LocalServicesLeadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LocalServicesLeadService"]
    ) -> v17.LocalServicesLeadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V17
    ) -> v17.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"]
    ) -> v17.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V17
    ) -> v17.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"]
    ) -> v17.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V17
    ) -> v17.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"]
    ) -> v17.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V17
    ) -> v17.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"]
    ) -> v17.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V17
    ) -> v17.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"]
    ) -> v17.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V17
    ) -> v17.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"]
    ) -> v17.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V17
    ) -> v17.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"]
    ) -> v17.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V17
    ) -> v17.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"]
    ) -> v17.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewService"], version: _V17
    ) -> v17.ShareablePreviewServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ShareablePreviewService"]
    ) -> v17.ShareablePreviewServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V17
    ) -> v17.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"]
    ) -> v17.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V17
    ) -> v17.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"]
    ) -> v17.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V17
    ) -> v17.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"]
    ) -> v17.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V17
    ) -> v17.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"]
    ) -> v17.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V17
    ) -> v17.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"]
    ) -> v17.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V17
    ) -> v17.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"]
    ) -> v17.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V17
    ) -> v17.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"]
    ) -> v17.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeService"], version: _V17
    ) -> v17.UserListCustomerTypeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListCustomerTypeService"]
    ) -> v17.UserListCustomerTypeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V17
    ) -> v17.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"]
    ) -> v17.UserListServiceClient: ...
    @overload
    def get_service(self, name: str, version: _V = "v17") -> Any: ...
