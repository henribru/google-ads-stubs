from typing import Any

import proto

from google.ads.googleads.v11.enums.types.interaction_event_type import (
    InteractionEventTypeEnum,
)
from google.ads.googleads.v11.enums.types.quality_score_bucket import (
    QualityScoreBucketEnum,
)

class Metrics(proto.Message):
    absolute_top_impression_percentage: float
    active_view_cpm: float
    active_view_ctr: float
    active_view_impressions: int
    active_view_measurability: float
    active_view_measurable_cost_micros: int
    active_view_measurable_impressions: int
    active_view_viewability: float
    all_conversions_from_interactions_rate: float
    all_conversions_value: float
    all_conversions_value_by_conversion_date: float
    all_conversions: float
    all_conversions_by_conversion_date: float
    all_conversions_value_per_cost: float
    all_conversions_from_click_to_call: float
    all_conversions_from_directions: float
    all_conversions_from_interactions_value_per_interaction: float
    all_conversions_from_menu: float
    all_conversions_from_order: float
    all_conversions_from_other_engagement: float
    all_conversions_from_store_visit: float
    all_conversions_from_store_website: float
    auction_insight_search_absolute_top_impression_percentage: float
    auction_insight_search_impression_share: float
    auction_insight_search_outranking_share: float
    auction_insight_search_overlap_rate: float
    auction_insight_search_position_above_rate: float
    auction_insight_search_top_impression_percentage: float
    average_cost: float
    average_cpc: float
    average_cpe: float
    average_cpm: float
    average_cpv: float
    average_page_views: float
    average_time_on_site: float
    benchmark_average_max_cpc: float
    biddable_app_install_conversions: float
    biddable_app_post_install_conversions: float
    benchmark_ctr: float
    bounce_rate: float
    clicks: int
    combined_clicks: int
    combined_clicks_per_query: float
    combined_queries: int
    content_budget_lost_impression_share: float
    content_impression_share: float
    conversion_last_received_request_date_time: str
    conversion_last_conversion_date: str
    content_rank_lost_impression_share: float
    conversions_from_interactions_rate: float
    conversions_value: float
    conversions_value_by_conversion_date: float
    conversions_value_per_cost: float
    conversions_from_interactions_value_per_interaction: float
    conversions: float
    conversions_by_conversion_date: float
    cost_micros: int
    cost_per_all_conversions: float
    cost_per_conversion: float
    cost_per_current_model_attributed_conversion: float
    cross_device_conversions: float
    ctr: float
    current_model_attributed_conversions: float
    current_model_attributed_conversions_from_interactions_rate: float
    current_model_attributed_conversions_from_interactions_value_per_interaction: float
    current_model_attributed_conversions_value: float
    current_model_attributed_conversions_value_per_cost: float
    engagement_rate: float
    engagements: int
    hotel_average_lead_value_micros: float
    hotel_commission_rate_micros: int
    hotel_expected_commission_cost: float
    hotel_price_difference_percentage: float
    hotel_eligible_impressions: int
    historical_creative_quality_score: QualityScoreBucketEnum.QualityScoreBucket
    historical_landing_page_quality_score: QualityScoreBucketEnum.QualityScoreBucket
    historical_quality_score: int
    historical_search_predicted_ctr: QualityScoreBucketEnum.QualityScoreBucket
    gmail_forwards: int
    gmail_saves: int
    gmail_secondary_clicks: int
    impressions_from_store_reach: int
    impressions: int
    interaction_rate: float
    interactions: int
    interaction_event_types: list[InteractionEventTypeEnum.InteractionEventType]
    invalid_click_rate: float
    invalid_clicks: int
    message_chats: int
    message_impressions: int
    message_chat_rate: float
    mobile_friendly_clicks_percentage: float
    optimization_score_uplift: float
    optimization_score_url: str
    organic_clicks: int
    organic_clicks_per_query: float
    organic_impressions: int
    organic_impressions_per_query: float
    organic_queries: int
    percent_new_visitors: float
    phone_calls: int
    phone_impressions: int
    phone_through_rate: float
    relative_ctr: float
    search_absolute_top_impression_share: float
    search_budget_lost_absolute_top_impression_share: float
    search_budget_lost_impression_share: float
    search_budget_lost_top_impression_share: float
    search_click_share: float
    search_exact_match_impression_share: float
    search_impression_share: float
    search_rank_lost_absolute_top_impression_share: float
    search_rank_lost_impression_share: float
    search_rank_lost_top_impression_share: float
    search_top_impression_share: float
    speed_score: int
    top_impression_percentage: float
    valid_accelerated_mobile_pages_clicks_percentage: float
    value_per_all_conversions: float
    value_per_all_conversions_by_conversion_date: float
    value_per_conversion: float
    value_per_conversions_by_conversion_date: float
    value_per_current_model_attributed_conversion: float
    video_quartile_p100_rate: float
    video_quartile_p25_rate: float
    video_quartile_p50_rate: float
    video_quartile_p75_rate: float
    video_view_rate: float
    video_views: int
    view_through_conversions: int
    sk_ad_network_conversions: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        absolute_top_impression_percentage: float = ...,
        active_view_cpm: float = ...,
        active_view_ctr: float = ...,
        active_view_impressions: int = ...,
        active_view_measurability: float = ...,
        active_view_measurable_cost_micros: int = ...,
        active_view_measurable_impressions: int = ...,
        active_view_viewability: float = ...,
        all_conversions_from_interactions_rate: float = ...,
        all_conversions_value: float = ...,
        all_conversions_value_by_conversion_date: float = ...,
        all_conversions: float = ...,
        all_conversions_by_conversion_date: float = ...,
        all_conversions_value_per_cost: float = ...,
        all_conversions_from_click_to_call: float = ...,
        all_conversions_from_directions: float = ...,
        all_conversions_from_interactions_value_per_interaction: float = ...,
        all_conversions_from_menu: float = ...,
        all_conversions_from_order: float = ...,
        all_conversions_from_other_engagement: float = ...,
        all_conversions_from_store_visit: float = ...,
        all_conversions_from_store_website: float = ...,
        auction_insight_search_absolute_top_impression_percentage: float = ...,
        auction_insight_search_impression_share: float = ...,
        auction_insight_search_outranking_share: float = ...,
        auction_insight_search_overlap_rate: float = ...,
        auction_insight_search_position_above_rate: float = ...,
        auction_insight_search_top_impression_percentage: float = ...,
        average_cost: float = ...,
        average_cpc: float = ...,
        average_cpe: float = ...,
        average_cpm: float = ...,
        average_cpv: float = ...,
        average_page_views: float = ...,
        average_time_on_site: float = ...,
        benchmark_average_max_cpc: float = ...,
        biddable_app_install_conversions: float = ...,
        biddable_app_post_install_conversions: float = ...,
        benchmark_ctr: float = ...,
        bounce_rate: float = ...,
        clicks: int = ...,
        combined_clicks: int = ...,
        combined_clicks_per_query: float = ...,
        combined_queries: int = ...,
        content_budget_lost_impression_share: float = ...,
        content_impression_share: float = ...,
        conversion_last_received_request_date_time: str = ...,
        conversion_last_conversion_date: str = ...,
        content_rank_lost_impression_share: float = ...,
        conversions_from_interactions_rate: float = ...,
        conversions_value: float = ...,
        conversions_value_by_conversion_date: float = ...,
        conversions_value_per_cost: float = ...,
        conversions_from_interactions_value_per_interaction: float = ...,
        conversions: float = ...,
        conversions_by_conversion_date: float = ...,
        cost_micros: int = ...,
        cost_per_all_conversions: float = ...,
        cost_per_conversion: float = ...,
        cost_per_current_model_attributed_conversion: float = ...,
        cross_device_conversions: float = ...,
        ctr: float = ...,
        current_model_attributed_conversions: float = ...,
        current_model_attributed_conversions_from_interactions_rate: float = ...,
        current_model_attributed_conversions_from_interactions_value_per_interaction: float = ...,
        current_model_attributed_conversions_value: float = ...,
        current_model_attributed_conversions_value_per_cost: float = ...,
        engagement_rate: float = ...,
        engagements: int = ...,
        hotel_average_lead_value_micros: float = ...,
        hotel_commission_rate_micros: int = ...,
        hotel_expected_commission_cost: float = ...,
        hotel_price_difference_percentage: float = ...,
        hotel_eligible_impressions: int = ...,
        historical_creative_quality_score: QualityScoreBucketEnum.QualityScoreBucket = ...,
        historical_landing_page_quality_score: QualityScoreBucketEnum.QualityScoreBucket = ...,
        historical_quality_score: int = ...,
        historical_search_predicted_ctr: QualityScoreBucketEnum.QualityScoreBucket = ...,
        gmail_forwards: int = ...,
        gmail_saves: int = ...,
        gmail_secondary_clicks: int = ...,
        impressions_from_store_reach: int = ...,
        impressions: int = ...,
        interaction_rate: float = ...,
        interactions: int = ...,
        interaction_event_types: list[
            InteractionEventTypeEnum.InteractionEventType
        ] = ...,
        invalid_click_rate: float = ...,
        invalid_clicks: int = ...,
        message_chats: int = ...,
        message_impressions: int = ...,
        message_chat_rate: float = ...,
        mobile_friendly_clicks_percentage: float = ...,
        optimization_score_uplift: float = ...,
        optimization_score_url: str = ...,
        organic_clicks: int = ...,
        organic_clicks_per_query: float = ...,
        organic_impressions: int = ...,
        organic_impressions_per_query: float = ...,
        organic_queries: int = ...,
        percent_new_visitors: float = ...,
        phone_calls: int = ...,
        phone_impressions: int = ...,
        phone_through_rate: float = ...,
        relative_ctr: float = ...,
        search_absolute_top_impression_share: float = ...,
        search_budget_lost_absolute_top_impression_share: float = ...,
        search_budget_lost_impression_share: float = ...,
        search_budget_lost_top_impression_share: float = ...,
        search_click_share: float = ...,
        search_exact_match_impression_share: float = ...,
        search_impression_share: float = ...,
        search_rank_lost_absolute_top_impression_share: float = ...,
        search_rank_lost_impression_share: float = ...,
        search_rank_lost_top_impression_share: float = ...,
        search_top_impression_share: float = ...,
        speed_score: int = ...,
        top_impression_percentage: float = ...,
        valid_accelerated_mobile_pages_clicks_percentage: float = ...,
        value_per_all_conversions: float = ...,
        value_per_all_conversions_by_conversion_date: float = ...,
        value_per_conversion: float = ...,
        value_per_conversions_by_conversion_date: float = ...,
        value_per_current_model_attributed_conversion: float = ...,
        video_quartile_p100_rate: float = ...,
        video_quartile_p25_rate: float = ...,
        video_quartile_p50_rate: float = ...,
        video_quartile_p75_rate: float = ...,
        video_view_rate: float = ...,
        video_views: int = ...,
        view_through_conversions: int = ...,
        sk_ad_network_conversions: int = ...
    ) -> None: ...
