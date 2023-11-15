from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.criteria import (
    AgeRangeInfo,
    AppPaymentModelInfo,
    AudienceInfo,
    CombinedAudienceInfo,
    CustomAffinityInfo,
    CustomAudienceInfo,
    CustomIntentInfo,
    GenderInfo,
    IncomeRangeInfo,
    KeywordInfo,
    LanguageInfo,
    ListingGroupInfo,
    LocationInfo,
    MobileAppCategoryInfo,
    MobileApplicationInfo,
    ParentalStatusInfo,
    PlacementInfo,
    TopicInfo,
    UserInterestInfo,
    UserListInfo,
    WebpageInfo,
    YouTubeChannelInfo,
    YouTubeVideoInfo,
)
from google.ads.googleads.v15.common.types.custom_parameter import CustomParameter
from google.ads.googleads.v15.enums.types.ad_group_criterion_approval_status import (
    AdGroupCriterionApprovalStatusEnum,
)
from google.ads.googleads.v15.enums.types.ad_group_criterion_status import (
    AdGroupCriterionStatusEnum,
)
from google.ads.googleads.v15.enums.types.bidding_source import BiddingSourceEnum
from google.ads.googleads.v15.enums.types.criterion_system_serving_status import (
    CriterionSystemServingStatusEnum,
)
from google.ads.googleads.v15.enums.types.criterion_type import CriterionTypeEnum
from google.ads.googleads.v15.enums.types.quality_score_bucket import (
    QualityScoreBucketEnum,
)

_M = TypeVar("_M")

class AdGroupCriterion(proto.Message):
    class PositionEstimates(proto.Message):
        first_page_cpc_micros: int
        first_position_cpc_micros: int
        top_of_page_cpc_micros: int
        estimated_add_clicks_at_first_position_cpc: int
        estimated_add_cost_at_first_position_cpc: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            first_page_cpc_micros: int = ...,
            first_position_cpc_micros: int = ...,
            top_of_page_cpc_micros: int = ...,
            estimated_add_clicks_at_first_position_cpc: int = ...,
            estimated_add_cost_at_first_position_cpc: int = ...
        ) -> None: ...

    class QualityInfo(proto.Message):
        quality_score: int
        creative_quality_score: QualityScoreBucketEnum.QualityScoreBucket
        post_click_quality_score: QualityScoreBucketEnum.QualityScoreBucket
        search_predicted_ctr: QualityScoreBucketEnum.QualityScoreBucket
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            quality_score: int = ...,
            creative_quality_score: QualityScoreBucketEnum.QualityScoreBucket = ...,
            post_click_quality_score: QualityScoreBucketEnum.QualityScoreBucket = ...,
            search_predicted_ctr: QualityScoreBucketEnum.QualityScoreBucket = ...
        ) -> None: ...
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
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        criterion_id: int = ...,
        display_name: str = ...,
        status: AdGroupCriterionStatusEnum.AdGroupCriterionStatus = ...,
        quality_info: AdGroupCriterion.QualityInfo = ...,
        ad_group: str = ...,
        type_: CriterionTypeEnum.CriterionType = ...,
        negative: bool = ...,
        system_serving_status: CriterionSystemServingStatusEnum.CriterionSystemServingStatus = ...,
        approval_status: AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatus = ...,
        disapproval_reasons: MutableSequence[str] = ...,
        labels: MutableSequence[str] = ...,
        bid_modifier: float = ...,
        cpc_bid_micros: int = ...,
        cpm_bid_micros: int = ...,
        cpv_bid_micros: int = ...,
        percent_cpc_bid_micros: int = ...,
        effective_cpc_bid_micros: int = ...,
        effective_cpm_bid_micros: int = ...,
        effective_cpv_bid_micros: int = ...,
        effective_percent_cpc_bid_micros: int = ...,
        effective_cpc_bid_source: BiddingSourceEnum.BiddingSource = ...,
        effective_cpm_bid_source: BiddingSourceEnum.BiddingSource = ...,
        effective_cpv_bid_source: BiddingSourceEnum.BiddingSource = ...,
        effective_percent_cpc_bid_source: BiddingSourceEnum.BiddingSource = ...,
        position_estimates: AdGroupCriterion.PositionEstimates = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        final_url_suffix: str = ...,
        tracking_url_template: str = ...,
        url_custom_parameters: MutableSequence[CustomParameter] = ...,
        keyword: KeywordInfo = ...,
        placement: PlacementInfo = ...,
        mobile_app_category: MobileAppCategoryInfo = ...,
        mobile_application: MobileApplicationInfo = ...,
        listing_group: ListingGroupInfo = ...,
        age_range: AgeRangeInfo = ...,
        gender: GenderInfo = ...,
        income_range: IncomeRangeInfo = ...,
        parental_status: ParentalStatusInfo = ...,
        user_list: UserListInfo = ...,
        youtube_video: YouTubeVideoInfo = ...,
        youtube_channel: YouTubeChannelInfo = ...,
        topic: TopicInfo = ...,
        user_interest: UserInterestInfo = ...,
        webpage: WebpageInfo = ...,
        app_payment_model: AppPaymentModelInfo = ...,
        custom_affinity: CustomAffinityInfo = ...,
        custom_intent: CustomIntentInfo = ...,
        custom_audience: CustomAudienceInfo = ...,
        combined_audience: CombinedAudienceInfo = ...,
        audience: AudienceInfo = ...,
        location: LocationInfo = ...,
        language: LanguageInfo = ...
    ) -> None: ...
