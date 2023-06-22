from typing import Any, Dict, Union, overload

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

from google.ads.googleads import v12, v13, v14
from google.ads.googleads.config import _ConfigDataUnparsed

_V12 = Literal["v12"]
_V13 = Literal["v13"]
_V14 = Literal["v14"]
_V = Union[_V12, _V13, _V14]

class GoogleAdsClient:
    credentials: Credentials
    developer_token: str
    endpoint: str | None
    login_customer_id: str | None
    linked_customer_id: str | None
    version: str | None
    http_proxy: str | None
    use_proto_plus: bool
    enums: Any  # TODO
    @classmethod
    def copy_from(
        cls,
        destination: Union[proto.Message, Message],
        origin: Union[proto.Message, Message],
    ) -> None: ...
    @classmethod
    def load_from_env(cls, version: str | None = ...) -> GoogleAdsClient: ...
    @classmethod
    def load_from_string(
        cls, yaml_str: str, version: str | None = ...
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_storage(
        cls, path: str | None = ..., version: str | None = ...
    ) -> GoogleAdsClient: ...
    @classmethod
    def load_from_dict(
        cls, config_dict: _ConfigDataUnparsed, version: str | None = ...
    ) -> GoogleAdsClient: ...
    def __init__(
        self,
        credentials: Credentials,
        developer_token: str,
        endpoint: str | None = ...,
        login_customer_id: str | None = ...,
        logging_config: Dict[Any, Any] | None = ...,
        linked_customer_id: str | None = ...,
        version: str | None = ...,
        http_proxy: str | None = ...,
        use_proto_plus: bool = ...,
    ) -> None: ...
    def get_type(cls, name: str, version: _V = ...) -> Any: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V12
    ) -> v12.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V12
    ) -> v12.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V12
    ) -> v12.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V12
    ) -> v12.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V12
    ) -> v12.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V12
    ) -> v12.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V12
    ) -> v12.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V12
    ) -> v12.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V12
    ) -> v12.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V12
    ) -> v12.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V12
    ) -> v12.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V12
    ) -> v12.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V12
    ) -> v12.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V12
    ) -> v12.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V12
    ) -> v12.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V12
    ) -> v12.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V12
    ) -> v12.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V12
    ) -> v12.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V12
    ) -> v12.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V12
    ) -> v12.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V12
    ) -> v12.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V12
    ) -> v12.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V12
    ) -> v12.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V12
    ) -> v12.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V12
    ) -> v12.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V12
    ) -> v12.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V12
    ) -> v12.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V12
    ) -> v12.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V12
    ) -> v12.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V12
    ) -> v12.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V12
    ) -> v12.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V12
    ) -> v12.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V12
    ) -> v12.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V12
    ) -> v12.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V12
    ) -> v12.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V12
    ) -> v12.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V12
    ) -> v12.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V12
    ) -> v12.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V12
    ) -> v12.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V12
    ) -> v12.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V12
    ) -> v12.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V12
    ) -> v12.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V12
    ) -> v12.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V12
    ) -> v12.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V12
    ) -> v12.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V12
    ) -> v12.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V12
    ) -> v12.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V12
    ) -> v12.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V12
    ) -> v12.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V12
    ) -> v12.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V12
    ) -> v12.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V12
    ) -> v12.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V12
    ) -> v12.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V12
    ) -> v12.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V12
    ) -> v12.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V12
    ) -> v12.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V12
    ) -> v12.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V12
    ) -> v12.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V12
    ) -> v12.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V12
    ) -> v12.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V12
    ) -> v12.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V12
    ) -> v12.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V12
    ) -> v12.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V12
    ) -> v12.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V12
    ) -> v12.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V12
    ) -> v12.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V12
    ) -> v12.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V12
    ) -> v12.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V12
    ) -> v12.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V12
    ) -> v12.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V12
    ) -> v12.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V12
    ) -> v12.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V12
    ) -> v12.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V12
    ) -> v12.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V12
    ) -> v12.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V12
    ) -> v12.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V12
    ) -> v12.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V12
    ) -> v12.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V12
    ) -> v12.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V12
    ) -> v12.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V12
    ) -> v12.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V12
    ) -> v12.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V12
    ) -> v12.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V12
    ) -> v12.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V12
    ) -> v12.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V12
    ) -> v12.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V12
    ) -> v12.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V12
    ) -> v12.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V12
    ) -> v12.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V12
    ) -> v12.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V12
    ) -> v12.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MediaFileService"], version: _V12
    ) -> v12.MediaFileServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MerchantCenterLinkService"], version: _V12
    ) -> v12.MerchantCenterLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V12
    ) -> v12.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V12
    ) -> v12.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V12
    ) -> v12.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V12
    ) -> v12.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V12
    ) -> v12.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V12
    ) -> v12.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V12
    ) -> v12.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V12
    ) -> v12.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V12
    ) -> v12.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V12
    ) -> v12.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V12
    ) -> v12.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V12
    ) -> v12.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V13
    ) -> v13.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V13
    ) -> v13.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V13
    ) -> v13.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V13
    ) -> v13.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V13
    ) -> v13.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V13
    ) -> v13.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V13
    ) -> v13.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V13
    ) -> v13.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V13
    ) -> v13.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V13
    ) -> v13.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V13
    ) -> v13.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V13
    ) -> v13.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V13
    ) -> v13.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V13
    ) -> v13.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V13
    ) -> v13.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V13
    ) -> v13.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V13
    ) -> v13.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V13
    ) -> v13.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V13
    ) -> v13.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V13
    ) -> v13.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V13
    ) -> v13.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V13
    ) -> v13.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V13
    ) -> v13.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V13
    ) -> v13.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V13
    ) -> v13.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V13
    ) -> v13.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V13
    ) -> v13.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V13
    ) -> v13.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V13
    ) -> v13.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V13
    ) -> v13.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V13
    ) -> v13.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V13
    ) -> v13.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V13
    ) -> v13.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V13
    ) -> v13.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V13
    ) -> v13.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V13
    ) -> v13.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V13
    ) -> v13.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V13
    ) -> v13.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V13
    ) -> v13.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V13
    ) -> v13.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V13
    ) -> v13.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V13
    ) -> v13.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V13
    ) -> v13.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V13
    ) -> v13.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V13
    ) -> v13.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V13
    ) -> v13.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V13
    ) -> v13.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V13
    ) -> v13.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V13
    ) -> v13.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V13
    ) -> v13.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V13
    ) -> v13.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V13
    ) -> v13.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V13
    ) -> v13.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V13
    ) -> v13.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V13
    ) -> v13.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V13
    ) -> v13.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V13
    ) -> v13.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V13
    ) -> v13.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V13
    ) -> v13.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V13
    ) -> v13.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V13
    ) -> v13.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V13
    ) -> v13.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V13
    ) -> v13.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V13
    ) -> v13.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V13
    ) -> v13.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V13
    ) -> v13.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V13
    ) -> v13.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V13,
    ) -> v13.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V13
    ) -> v13.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V13
    ) -> v13.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V13
    ) -> v13.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V13
    ) -> v13.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V13
    ) -> v13.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V13
    ) -> v13.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V13
    ) -> v13.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V13
    ) -> v13.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V13
    ) -> v13.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V13
    ) -> v13.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V13
    ) -> v13.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V13
    ) -> v13.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V13
    ) -> v13.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V13
    ) -> v13.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V13
    ) -> v13.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V13
    ) -> v13.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V13
    ) -> v13.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V13
    ) -> v13.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V13
    ) -> v13.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V13
    ) -> v13.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V13
    ) -> v13.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V13
    ) -> v13.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V13
    ) -> v13.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V13
    ) -> v13.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MediaFileService"], version: _V13
    ) -> v13.MediaFileServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MerchantCenterLinkService"], version: _V13
    ) -> v13.MerchantCenterLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V13
    ) -> v13.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V13
    ) -> v13.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V13
    ) -> v13.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V13
    ) -> v13.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V13
    ) -> v13.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V13
    ) -> v13.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V13
    ) -> v13.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V13
    ) -> v13.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V13
    ) -> v13.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V13
    ) -> v13.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V13
    ) -> v13.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V13
    ) -> v13.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V13
    ) -> v13.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V13
    ) -> v13.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"], version: _V14
    ) -> v14.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountBudgetProposalService"]
    ) -> v14.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V14
    ) -> v14.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"]
    ) -> v14.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V14
    ) -> v14.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"]
    ) -> v14.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V14
    ) -> v14.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"]
    ) -> v14.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V14
    ) -> v14.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"]
    ) -> v14.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V14
    ) -> v14.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"]
    ) -> v14.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V14
    ) -> v14.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"]
    ) -> v14.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V14
    ) -> v14.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"]
    ) -> v14.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V14
    ) -> v14.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"]
    ) -> v14.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V14
    ) -> v14.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"]
    ) -> v14.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V14
    ) -> v14.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"]
    ) -> v14.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V14
    ) -> v14.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"]
    ) -> v14.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V14
    ) -> v14.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"]
    ) -> v14.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V14
    ) -> v14.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"]
    ) -> v14.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V14
    ) -> v14.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"]
    ) -> v14.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V14
    ) -> v14.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"]
    ) -> v14.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V14
    ) -> v14.AdServiceClient: ...
    @overload
    def get_service(self, name: Literal["AdService"]) -> v14.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V14
    ) -> v14.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"]
    ) -> v14.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V14
    ) -> v14.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"]
    ) -> v14.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V14
    ) -> v14.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"]
    ) -> v14.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V14
    ) -> v14.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"]
    ) -> v14.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V14
    ) -> v14.AssetServiceClient: ...
    @overload
    def get_service(self, name: Literal["AssetService"]) -> v14.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V14
    ) -> v14.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"]
    ) -> v14.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V14
    ) -> v14.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"]
    ) -> v14.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V14
    ) -> v14.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"]
    ) -> v14.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V14
    ) -> v14.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"]
    ) -> v14.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V14
    ) -> v14.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"]
    ) -> v14.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V14
    ) -> v14.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"]
    ) -> v14.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V14
    ) -> v14.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"]
    ) -> v14.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V14
    ) -> v14.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"]
    ) -> v14.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V14
    ) -> v14.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"]
    ) -> v14.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V14
    ) -> v14.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"]
    ) -> v14.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V14
    ) -> v14.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"]
    ) -> v14.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V14
    ) -> v14.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"]
    ) -> v14.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V14
    ) -> v14.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"]
    ) -> v14.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V14
    ) -> v14.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"]
    ) -> v14.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V14
    ) -> v14.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"]
    ) -> v14.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V14
    ) -> v14.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"]
    ) -> v14.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V14
    ) -> v14.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"]
    ) -> v14.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V14
    ) -> v14.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"]
    ) -> v14.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V14
    ) -> v14.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"]
    ) -> v14.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V14
    ) -> v14.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"]
    ) -> v14.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V14
    ) -> v14.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"]
    ) -> v14.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V14
    ) -> v14.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"]
    ) -> v14.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V14
    ) -> v14.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"]
    ) -> v14.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V14
    ) -> v14.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"]
    ) -> v14.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V14
    ) -> v14.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"]
    ) -> v14.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V14
    ) -> v14.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"]
    ) -> v14.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V14
    ) -> v14.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"]
    ) -> v14.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V14
    ) -> v14.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"]
    ) -> v14.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V14
    ) -> v14.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"]
    ) -> v14.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V14
    ) -> v14.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"]
    ) -> v14.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V14
    ) -> v14.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"]
    ) -> v14.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V14
    ) -> v14.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"]
    ) -> v14.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V14
    ) -> v14.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"]
    ) -> v14.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V14
    ) -> v14.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"]
    ) -> v14.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V14
    ) -> v14.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"]
    ) -> v14.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V14
    ) -> v14.CustomerClient: ...
    @overload
    def get_service(self, name: Literal["Customer"]) -> v14.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V14
    ) -> v14.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"]
    ) -> v14.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V14
    ) -> v14.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"]
    ) -> v14.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V14
    ) -> v14.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"]
    ) -> v14.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V14
    ) -> v14.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"]
    ) -> v14.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V14
    ) -> v14.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"]
    ) -> v14.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V14
    ) -> v14.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"]
    ) -> v14.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V14
    ) -> v14.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"]
    ) -> v14.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V14
    ) -> v14.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"]
    ) -> v14.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V14
    ) -> v14.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"]
    ) -> v14.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V14,
    ) -> v14.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerSkAdNetworkConversionValueSchemaService"]
    ) -> v14.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V14
    ) -> v14.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"]
    ) -> v14.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V14
    ) -> v14.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"]
    ) -> v14.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V14
    ) -> v14.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"]
    ) -> v14.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V14
    ) -> v14.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"]
    ) -> v14.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V14
    ) -> v14.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"]
    ) -> v14.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V14
    ) -> v14.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"]
    ) -> v14.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V14
    ) -> v14.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"]
    ) -> v14.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V14
    ) -> v14.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"]
    ) -> v14.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V14
    ) -> v14.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"]
    ) -> v14.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V14
    ) -> v14.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"]
    ) -> v14.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V14
    ) -> v14.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"]
    ) -> v14.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V14
    ) -> v14.FeedServiceClient: ...
    @overload
    def get_service(self, name: Literal["FeedService"]) -> v14.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V14
    ) -> v14.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"]
    ) -> v14.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V14
    ) -> v14.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"]
    ) -> v14.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V14
    ) -> v14.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"]
    ) -> v14.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V14
    ) -> v14.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"]
    ) -> v14.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V14
    ) -> v14.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"]
    ) -> v14.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V14
    ) -> v14.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"]
    ) -> v14.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V14
    ) -> v14.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"]
    ) -> v14.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V14
    ) -> v14.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"]
    ) -> v14.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V14
    ) -> v14.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"]
    ) -> v14.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V14
    ) -> v14.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"]
    ) -> v14.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V14
    ) -> v14.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"]
    ) -> v14.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V14
    ) -> v14.LabelServiceClient: ...
    @overload
    def get_service(self, name: Literal["LabelService"]) -> v14.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MediaFileService"], version: _V14
    ) -> v14.MediaFileServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MediaFileService"]
    ) -> v14.MediaFileServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MerchantCenterLinkService"], version: _V14
    ) -> v14.MerchantCenterLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["MerchantCenterLinkService"]
    ) -> v14.MerchantCenterLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V14
    ) -> v14.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"]
    ) -> v14.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V14
    ) -> v14.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"]
    ) -> v14.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V14
    ) -> v14.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"]
    ) -> v14.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V14
    ) -> v14.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"]
    ) -> v14.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V14
    ) -> v14.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"]
    ) -> v14.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V14
    ) -> v14.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"]
    ) -> v14.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V14
    ) -> v14.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"]
    ) -> v14.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V14
    ) -> v14.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"]
    ) -> v14.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V14
    ) -> v14.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"]
    ) -> v14.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V14
    ) -> v14.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"]
    ) -> v14.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V14
    ) -> v14.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"]
    ) -> v14.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V14
    ) -> v14.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"]
    ) -> v14.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V14
    ) -> v14.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"]
    ) -> v14.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V14
    ) -> v14.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"]
    ) -> v14.UserListServiceClient: ...
    @overload
    def get_service(self, name: str, version: _V = ...) -> Any: ...
