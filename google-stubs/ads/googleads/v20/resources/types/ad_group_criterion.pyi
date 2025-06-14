from google.ads.googleads.v20.common.types.criteria import LanguageInfo
from google.ads.googleads.v20.common.types.criteria import LocationInfo
from google.ads.googleads.v20.common.types.criteria import AudienceInfo
from google.ads.googleads.v20.common.types.criteria import CombinedAudienceInfo
from google.ads.googleads.v20.common.types.criteria import CustomAudienceInfo
from google.ads.googleads.v20.common.types.criteria import CustomIntentInfo
from google.ads.googleads.v20.common.types.criteria import CustomAffinityInfo
from google.ads.googleads.v20.common.types.criteria import AppPaymentModelInfo
from google.ads.googleads.v20.common.types.criteria import WebpageInfo
from google.ads.googleads.v20.common.types.criteria import UserInterestInfo
from google.ads.googleads.v20.common.types.criteria import TopicInfo
from google.ads.googleads.v20.common.types.criteria import YouTubeChannelInfo
from google.ads.googleads.v20.common.types.criteria import YouTubeVideoInfo
from google.ads.googleads.v20.common.types.criteria import UserListInfo
from google.ads.googleads.v20.common.types.criteria import ParentalStatusInfo
from google.ads.googleads.v20.common.types.criteria import IncomeRangeInfo
from google.ads.googleads.v20.common.types.criteria import GenderInfo
from google.ads.googleads.v20.common.types.criteria import AgeRangeInfo
from google.ads.googleads.v20.common.types.criteria import ListingGroupInfo
from google.ads.googleads.v20.common.types.criteria import MobileApplicationInfo
from google.ads.googleads.v20.common.types.criteria import MobileAppCategoryInfo
from google.ads.googleads.v20.common.types.criteria import PlacementInfo
from google.ads.googleads.v20.common.types.criteria import KeywordInfo
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.ad_group_criterion_primary_status_reason import AdGroupCriterionPrimaryStatusReasonEnum
from google.ads.googleads.v20.enums.types.ad_group_criterion_primary_status import AdGroupCriterionPrimaryStatusEnum
from collections.abc import MutableSequence
from google.ads.googleads.v20.common.types.custom_parameter import CustomParameter
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v20.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v20.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v20.enums.types.bidding_source import BiddingSourceEnum
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.ad_group_criterion_approval_status import AdGroupCriterionApprovalStatusEnum
from google.ads.googleads.v20.enums.types.criterion_system_serving_status import CriterionSystemServingStatusEnum
from google.ads.googleads.v20.enums.types.criterion_type import CriterionTypeEnum
from google.ads.googleads.v20.enums.types.ad_group_criterion_status import AdGroupCriterionStatusEnum
from google.ads.googleads.v20.enums.types.quality_score_bucket import QualityScoreBucketEnum
from google.ads.googleads.v20.enums.types.quality_score_bucket import QualityScoreBucketEnum
from google.ads.googleads.v20.enums.types.quality_score_bucket import QualityScoreBucketEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupCriterion(proto.Message):
    class PositionEstimates(proto.Message):
        first_page_cpc_micros: int
        first_position_cpc_micros: int
        top_of_page_cpc_micros: int
        estimated_add_clicks_at_first_position_cpc: int
        estimated_add_cost_at_first_position_cpc: int
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., first_page_cpc_micros: int = ..., first_position_cpc_micros: int = ..., top_of_page_cpc_micros: int = ..., estimated_add_clicks_at_first_position_cpc: int = ..., estimated_add_cost_at_first_position_cpc: int = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["first_page_cpc_micros", "first_position_cpc_micros", "top_of_page_cpc_micros", "estimated_add_clicks_at_first_position_cpc", "estimated_add_cost_at_first_position_cpc"]) -> bool: ...
    class QualityInfo(proto.Message):
        quality_score: int
        creative_quality_score: QualityScoreBucketEnum.QualityScoreBucket
        post_click_quality_score: QualityScoreBucketEnum.QualityScoreBucket
        search_predicted_ctr: QualityScoreBucketEnum.QualityScoreBucket
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., quality_score: int = ..., creative_quality_score: QualityScoreBucketEnum.QualityScoreBucket = ..., post_click_quality_score: QualityScoreBucketEnum.QualityScoreBucket = ..., search_predicted_ctr: QualityScoreBucketEnum.QualityScoreBucket = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["quality_score", "creative_quality_score", "post_click_quality_score", "search_predicted_ctr"]) -> bool: ...
    resource_name: str
    criterion_id: int
    display_name: str
    status: AdGroupCriterionStatusEnum.AdGroupCriterionStatus
    quality_info: AdGroupCriterion.QualityInfo
    ad_group: str
    type_: CriterionTypeEnum.CriterionType
    negative: bool
    system_serving_status: CriterionSystemServingStatusEnum.CriterionSystemServingStatus
    approval_status: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus
    disapproval_reasons: MutableSequence[str]
    labels: MutableSequence[str]
    bid_modifier: float
    cpc_bid_micros: int
    cpm_bid_micros: int
    cpv_bid_micros: int
    percent_cpc_bid_micros: int
    effective_cpc_bid_micros: int
    effective_cpm_bid_micros: int
    effective_cpv_bid_micros: int
    effective_percent_cpc_bid_micros: int
    effective_cpc_bid_source: BiddingSourceEnum.BiddingSource
    effective_cpm_bid_source: BiddingSourceEnum.BiddingSource
    effective_cpv_bid_source: BiddingSourceEnum.BiddingSource
    effective_percent_cpc_bid_source: BiddingSourceEnum.BiddingSource
    position_estimates: AdGroupCriterion.PositionEstimates
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    final_url_suffix: str
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    primary_status: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus
    primary_status_reasons: MutableSequence[AdGroupCriterionPrimaryStatusReasonEnum.AdGroupCriterionPrimaryStatusReason]
    keyword: KeywordInfo
    placement: PlacementInfo
    mobile_app_category: MobileAppCategoryInfo
    mobile_application: MobileApplicationInfo
    listing_group: ListingGroupInfo
    age_range: AgeRangeInfo
    gender: GenderInfo
    income_range: IncomeRangeInfo
    parental_status: ParentalStatusInfo
    user_list: UserListInfo
    youtube_video: YouTubeVideoInfo
    youtube_channel: YouTubeChannelInfo
    topic: TopicInfo
    user_interest: UserInterestInfo
    webpage: WebpageInfo
    app_payment_model: AppPaymentModelInfo
    custom_affinity: CustomAffinityInfo
    custom_intent: CustomIntentInfo
    custom_audience: CustomAudienceInfo
    combined_audience: CombinedAudienceInfo
    audience: AudienceInfo
    location: LocationInfo
    language: LanguageInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., criterion_id: int = ..., display_name: str = ..., status: AdGroupCriterionStatusEnum.AdGroupCriterionStatus = ..., quality_info: AdGroupCriterion.QualityInfo = ..., ad_group: str = ..., type_: CriterionTypeEnum.CriterionType = ..., negative: bool = ..., system_serving_status: CriterionSystemServingStatusEnum.CriterionSystemServingStatus = ..., approval_status: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus = ..., disapproval_reasons: MutableSequence[str] = ..., labels: MutableSequence[str] = ..., bid_modifier: float = ..., cpc_bid_micros: int = ..., cpm_bid_micros: int = ..., cpv_bid_micros: int = ..., percent_cpc_bid_micros: int = ..., effective_cpc_bid_micros: int = ..., effective_cpm_bid_micros: int = ..., effective_cpv_bid_micros: int = ..., effective_percent_cpc_bid_micros: int = ..., effective_cpc_bid_source: BiddingSourceEnum.BiddingSource = ..., effective_cpm_bid_source: BiddingSourceEnum.BiddingSource = ..., effective_cpv_bid_source: BiddingSourceEnum.BiddingSource = ..., effective_percent_cpc_bid_source: BiddingSourceEnum.BiddingSource = ..., position_estimates: AdGroupCriterion.PositionEstimates = ..., final_urls: MutableSequence[str] = ..., final_mobile_urls: MutableSequence[str] = ..., final_url_suffix: str = ..., tracking_url_template: str = ..., url_custom_parameters: MutableSequence[CustomParameter] = ..., primary_status: AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatus = ..., primary_status_reasons: MutableSequence[AdGroupCriterionPrimaryStatusReasonEnum.AdGroupCriterionPrimaryStatusReason] = ..., keyword: KeywordInfo = ..., placement: PlacementInfo = ..., mobile_app_category: MobileAppCategoryInfo = ..., mobile_application: MobileApplicationInfo = ..., listing_group: ListingGroupInfo = ..., age_range: AgeRangeInfo = ..., gender: GenderInfo = ..., income_range: IncomeRangeInfo = ..., parental_status: ParentalStatusInfo = ..., user_list: UserListInfo = ..., youtube_video: YouTubeVideoInfo = ..., youtube_channel: YouTubeChannelInfo = ..., topic: TopicInfo = ..., user_interest: UserInterestInfo = ..., webpage: WebpageInfo = ..., app_payment_model: AppPaymentModelInfo = ..., custom_affinity: CustomAffinityInfo = ..., custom_intent: CustomIntentInfo = ..., custom_audience: CustomAudienceInfo = ..., combined_audience: CombinedAudienceInfo = ..., audience: AudienceInfo = ..., location: LocationInfo = ..., language: LanguageInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "criterion_id", "display_name", "status", "quality_info", "ad_group", "type_", "negative", "system_serving_status", "approval_status", "disapproval_reasons", "labels", "bid_modifier", "cpc_bid_micros", "cpm_bid_micros", "cpv_bid_micros", "percent_cpc_bid_micros", "effective_cpc_bid_micros", "effective_cpm_bid_micros", "effective_cpv_bid_micros", "effective_percent_cpc_bid_micros", "effective_cpc_bid_source", "effective_cpm_bid_source", "effective_cpv_bid_source", "effective_percent_cpc_bid_source", "position_estimates", "final_urls", "final_mobile_urls", "final_url_suffix", "tracking_url_template", "url_custom_parameters", "primary_status", "primary_status_reasons", "keyword", "placement", "mobile_app_category", "mobile_application", "listing_group", "age_range", "gender", "income_range", "parental_status", "user_list", "youtube_video", "youtube_channel", "topic", "user_interest", "webpage", "app_payment_model", "custom_affinity", "custom_intent", "custom_audience", "combined_audience", "audience", "location", "language"]) -> bool: ...
