from typing import Any, Dict, Union, overload

import proto
from google.oauth2.credentials import Credentials
from google.protobuf.message import Message
from typing_extensions import Literal

from google.ads.googleads import v13, v14, v15
from google.ads.googleads.config import _ConfigDataUnparsed

_V13 = Literal["v13"]
_V14 = Literal["v14"]
_V15 = Literal["v15"]
_V = Union[_V13, _V14, _V15]

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
        use_cloud_org_for_api_access: bool = ...,
    ) -> None: ...
    def get_type(cls, name: str, version: _V = ...) -> Any: ...
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
        self, name: Literal["AccountBudgetProposalService"]
    ) -> v15.AccountBudgetProposalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"], version: _V15
    ) -> v15.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AccountLinkService"]
    ) -> v15.AccountLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"], version: _V15
    ) -> v15.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdLabelService"]
    ) -> v15.AdGroupAdLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"], version: _V15
    ) -> v15.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAdService"]
    ) -> v15.AdGroupAdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"], version: _V15
    ) -> v15.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetService"]
    ) -> v15.AdGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"], version: _V15
    ) -> v15.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupAssetSetService"]
    ) -> v15.AdGroupAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"], version: _V15
    ) -> v15.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupBidModifierService"]
    ) -> v15.AdGroupBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"], version: _V15
    ) -> v15.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionCustomizerService"]
    ) -> v15.AdGroupCriterionCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"], version: _V15
    ) -> v15.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionLabelService"]
    ) -> v15.AdGroupCriterionLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"], version: _V15
    ) -> v15.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCriterionService"]
    ) -> v15.AdGroupCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"], version: _V15
    ) -> v15.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupCustomizerService"]
    ) -> v15.AdGroupCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"], version: _V15
    ) -> v15.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupExtensionSettingService"]
    ) -> v15.AdGroupExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"], version: _V15
    ) -> v15.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupFeedService"]
    ) -> v15.AdGroupFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"], version: _V15
    ) -> v15.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupLabelService"]
    ) -> v15.AdGroupLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"], version: _V15
    ) -> v15.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdGroupService"]
    ) -> v15.AdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"], version: _V15
    ) -> v15.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdParameterService"]
    ) -> v15.AdParameterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AdService"], version: _V15
    ) -> v15.AdServiceClient: ...
    @overload
    def get_service(self, name: Literal["AdService"]) -> v15.AdServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"], version: _V15
    ) -> v15.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupAssetService"]
    ) -> v15.AssetGroupAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"], version: _V15
    ) -> v15.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupListingGroupFilterService"]
    ) -> v15.AssetGroupListingGroupFilterServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"], version: _V15
    ) -> v15.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupService"]
    ) -> v15.AssetGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"], version: _V15
    ) -> v15.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetGroupSignalService"]
    ) -> v15.AssetGroupSignalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetService"], version: _V15
    ) -> v15.AssetServiceClient: ...
    @overload
    def get_service(self, name: Literal["AssetService"]) -> v15.AssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"], version: _V15
    ) -> v15.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetAssetService"]
    ) -> v15.AssetSetAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"], version: _V15
    ) -> v15.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AssetSetService"]
    ) -> v15.AssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"], version: _V15
    ) -> v15.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceInsightsService"]
    ) -> v15.AudienceInsightsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"], version: _V15
    ) -> v15.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["AudienceService"]
    ) -> v15.AudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"], version: _V15
    ) -> v15.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BatchJobService"]
    ) -> v15.BatchJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"], version: _V15
    ) -> v15.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingDataExclusionService"]
    ) -> v15.BiddingDataExclusionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"], version: _V15
    ) -> v15.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingSeasonalityAdjustmentService"]
    ) -> v15.BiddingSeasonalityAdjustmentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"], version: _V15
    ) -> v15.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BiddingStrategyService"]
    ) -> v15.BiddingStrategyServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"], version: _V15
    ) -> v15.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BillingSetupService"]
    ) -> v15.BillingSetupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"], version: _V15
    ) -> v15.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["BrandSuggestionService"]
    ) -> v15.BrandSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"], version: _V15
    ) -> v15.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetService"]
    ) -> v15.CampaignAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"], version: _V15
    ) -> v15.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignAssetSetService"]
    ) -> v15.CampaignAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"], version: _V15
    ) -> v15.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBidModifierService"]
    ) -> v15.CampaignBidModifierServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"], version: _V15
    ) -> v15.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignBudgetService"]
    ) -> v15.CampaignBudgetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"], version: _V15
    ) -> v15.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignConversionGoalService"]
    ) -> v15.CampaignConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"], version: _V15
    ) -> v15.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCriterionService"]
    ) -> v15.CampaignCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"], version: _V15
    ) -> v15.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignCustomizerService"]
    ) -> v15.CampaignCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"], version: _V15
    ) -> v15.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignDraftService"]
    ) -> v15.CampaignDraftServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"], version: _V15
    ) -> v15.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignExtensionSettingService"]
    ) -> v15.CampaignExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"], version: _V15
    ) -> v15.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignFeedService"]
    ) -> v15.CampaignFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"], version: _V15
    ) -> v15.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignGroupService"]
    ) -> v15.CampaignGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"], version: _V15
    ) -> v15.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLabelService"]
    ) -> v15.CampaignLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"], version: _V15
    ) -> v15.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignLifecycleGoalService"]
    ) -> v15.CampaignLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"], version: _V15
    ) -> v15.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignService"]
    ) -> v15.CampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"], version: _V15
    ) -> v15.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CampaignSharedSetService"]
    ) -> v15.CampaignSharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"], version: _V15
    ) -> v15.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionActionService"]
    ) -> v15.ConversionActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"], version: _V15
    ) -> v15.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionAdjustmentUploadService"]
    ) -> v15.ConversionAdjustmentUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"], version: _V15
    ) -> v15.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionCustomVariableService"]
    ) -> v15.ConversionCustomVariableServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"], version: _V15
    ) -> v15.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionGoalCampaignConfigService"]
    ) -> v15.ConversionGoalCampaignConfigServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"], version: _V15
    ) -> v15.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionUploadService"]
    ) -> v15.ConversionUploadServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"], version: _V15
    ) -> v15.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleService"]
    ) -> v15.ConversionValueRuleServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"], version: _V15
    ) -> v15.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ConversionValueRuleSetService"]
    ) -> v15.ConversionValueRuleSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"], version: _V15
    ) -> v15.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomAudienceService"]
    ) -> v15.CustomAudienceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"], version: _V15
    ) -> v15.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomConversionGoalService"]
    ) -> v15.CustomConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"], version: _V15
    ) -> v15.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomInterestService"]
    ) -> v15.CustomInterestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"], version: _V15
    ) -> v15.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetService"]
    ) -> v15.CustomerAssetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"], version: _V15
    ) -> v15.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerAssetSetService"]
    ) -> v15.CustomerAssetSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["Customer"], version: _V15
    ) -> v15.CustomerClient: ...
    @overload
    def get_service(self, name: Literal["Customer"]) -> v15.CustomerClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"], version: _V15
    ) -> v15.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerClientLinkService"]
    ) -> v15.CustomerClientLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"], version: _V15
    ) -> v15.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerConversionGoalService"]
    ) -> v15.CustomerConversionGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"], version: _V15
    ) -> v15.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerCustomizerService"]
    ) -> v15.CustomerCustomizerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"], version: _V15
    ) -> v15.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerExtensionSettingService"]
    ) -> v15.CustomerExtensionSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"], version: _V15
    ) -> v15.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerFeedService"]
    ) -> v15.CustomerFeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"], version: _V15
    ) -> v15.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLabelService"]
    ) -> v15.CustomerLabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"], version: _V15
    ) -> v15.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerLifecycleGoalService"]
    ) -> v15.CustomerLifecycleGoalServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"], version: _V15
    ) -> v15.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerManagerLinkService"]
    ) -> v15.CustomerManagerLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"], version: _V15
    ) -> v15.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerNegativeCriterionService"]
    ) -> v15.CustomerNegativeCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"], version: _V15
    ) -> v15.CustomerServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerService"]
    ) -> v15.CustomerServiceClient: ...
    @overload
    def get_service(
        self,
        name: Literal["CustomerSkAdNetworkConversionValueSchemaService"],
        version: _V15,
    ) -> v15.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerSkAdNetworkConversionValueSchemaService"]
    ) -> v15.CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"], version: _V15
    ) -> v15.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessInvitationService"]
    ) -> v15.CustomerUserAccessInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"], version: _V15
    ) -> v15.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomerUserAccessService"]
    ) -> v15.CustomerUserAccessServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"], version: _V15
    ) -> v15.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["CustomizerAttributeService"]
    ) -> v15.CustomizerAttributeServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"], version: _V15
    ) -> v15.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentArmService"]
    ) -> v15.ExperimentArmServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"], version: _V15
    ) -> v15.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExperimentService"]
    ) -> v15.ExperimentServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"], version: _V15
    ) -> v15.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ExtensionFeedItemService"]
    ) -> v15.ExtensionFeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"], version: _V15
    ) -> v15.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemService"]
    ) -> v15.FeedItemServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"], version: _V15
    ) -> v15.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetLinkService"]
    ) -> v15.FeedItemSetLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"], version: _V15
    ) -> v15.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemSetService"]
    ) -> v15.FeedItemSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"], version: _V15
    ) -> v15.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedItemTargetService"]
    ) -> v15.FeedItemTargetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"], version: _V15
    ) -> v15.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedMappingService"]
    ) -> v15.FeedMappingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["FeedService"], version: _V15
    ) -> v15.FeedServiceClient: ...
    @overload
    def get_service(self, name: Literal["FeedService"]) -> v15.FeedServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"], version: _V15
    ) -> v15.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GeoTargetConstantService"]
    ) -> v15.GeoTargetConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"], version: _V15
    ) -> v15.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsFieldService"]
    ) -> v15.GoogleAdsFieldServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"], version: _V15
    ) -> v15.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["GoogleAdsService"]
    ) -> v15.GoogleAdsServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"], version: _V15
    ) -> v15.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["InvoiceService"]
    ) -> v15.InvoiceServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"], version: _V15
    ) -> v15.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupKeywordService"]
    ) -> v15.KeywordPlanAdGroupKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"], version: _V15
    ) -> v15.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanAdGroupService"]
    ) -> v15.KeywordPlanAdGroupServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"], version: _V15
    ) -> v15.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignKeywordService"]
    ) -> v15.KeywordPlanCampaignKeywordServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"], version: _V15
    ) -> v15.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanCampaignService"]
    ) -> v15.KeywordPlanCampaignServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"], version: _V15
    ) -> v15.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanIdeaService"]
    ) -> v15.KeywordPlanIdeaServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"], version: _V15
    ) -> v15.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordPlanService"]
    ) -> v15.KeywordPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"], version: _V15
    ) -> v15.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["KeywordThemeConstantService"]
    ) -> v15.KeywordThemeConstantServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["LabelService"], version: _V15
    ) -> v15.LabelServiceClient: ...
    @overload
    def get_service(self, name: Literal["LabelService"]) -> v15.LabelServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"], version: _V15
    ) -> v15.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["OfflineUserDataJobService"]
    ) -> v15.OfflineUserDataJobServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"], version: _V15
    ) -> v15.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["PaymentsAccountService"]
    ) -> v15.PaymentsAccountServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"], version: _V15
    ) -> v15.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkInvitationService"]
    ) -> v15.ProductLinkInvitationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"], version: _V15
    ) -> v15.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ProductLinkService"]
    ) -> v15.ProductLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"], version: _V15
    ) -> v15.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ReachPlanService"]
    ) -> v15.ReachPlanServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"], version: _V15
    ) -> v15.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationService"]
    ) -> v15.RecommendationServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"], version: _V15
    ) -> v15.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RecommendationSubscriptionService"]
    ) -> v15.RecommendationSubscriptionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"], version: _V15
    ) -> v15.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["RemarketingActionService"]
    ) -> v15.RemarketingActionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"], version: _V15
    ) -> v15.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedCriterionService"]
    ) -> v15.SharedCriterionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"], version: _V15
    ) -> v15.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SharedSetService"]
    ) -> v15.SharedSetServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"], version: _V15
    ) -> v15.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSettingService"]
    ) -> v15.SmartCampaignSettingServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"], version: _V15
    ) -> v15.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["SmartCampaignSuggestService"]
    ) -> v15.SmartCampaignSuggestServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"], version: _V15
    ) -> v15.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["ThirdPartyAppAnalyticsLinkService"]
    ) -> v15.ThirdPartyAppAnalyticsLinkServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"], version: _V15
    ) -> v15.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["TravelAssetSuggestionService"]
    ) -> v15.TravelAssetSuggestionServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"], version: _V15
    ) -> v15.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserDataService"]
    ) -> v15.UserDataServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"], version: _V15
    ) -> v15.UserListServiceClient: ...
    @overload
    def get_service(
        self, name: Literal["UserListService"]
    ) -> v15.UserListServiceClient: ...
    @overload
    def get_service(self, name: str, version: _V = ...) -> Any: ...
