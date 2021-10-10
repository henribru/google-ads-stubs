from typing import Any

import proto

from google.ads.googleads.v8.common.types import (
    criteria as criteria,
    custom_parameter as custom_parameter,
)
from google.ads.googleads.v8.enums.types import (
    ad_group_criterion_approval_status as ad_group_criterion_approval_status,
    ad_group_criterion_status as ad_group_criterion_status,
    bidding_source as bidding_source,
    criterion_system_serving_status as criterion_system_serving_status,
    criterion_type as criterion_type,
    quality_score_bucket as quality_score_bucket,
)

__protobuf__: Any

class AdGroupCriterion(proto.Message):
    class QualityInfo(proto.Message):
        quality_score: Any
        creative_quality_score: Any
        post_click_quality_score: Any
        search_predicted_ctr: Any
    class PositionEstimates(proto.Message):
        first_page_cpc_micros: Any
        first_position_cpc_micros: Any
        top_of_page_cpc_micros: Any
        estimated_add_clicks_at_first_position_cpc: Any
        estimated_add_cost_at_first_position_cpc: Any
    resource_name: Any
    criterion_id: Any
    display_name: Any
    status: Any
    quality_info: Any
    ad_group: Any
    type_: Any
    negative: Any
    system_serving_status: Any
    approval_status: Any
    disapproval_reasons: Any
    labels: Any
    bid_modifier: Any
    cpc_bid_micros: Any
    cpm_bid_micros: Any
    cpv_bid_micros: Any
    percent_cpc_bid_micros: Any
    effective_cpc_bid_micros: Any
    effective_cpm_bid_micros: Any
    effective_cpv_bid_micros: Any
    effective_percent_cpc_bid_micros: Any
    effective_cpc_bid_source: Any
    effective_cpm_bid_source: Any
    effective_cpv_bid_source: Any
    effective_percent_cpc_bid_source: Any
    position_estimates: Any
    final_urls: Any
    final_mobile_urls: Any
    final_url_suffix: Any
    tracking_url_template: Any
    url_custom_parameters: Any
    keyword: Any
    placement: Any
    mobile_app_category: Any
    mobile_application: Any
    listing_group: Any
    age_range: Any
    gender: Any
    income_range: Any
    parental_status: Any
    user_list: Any
    youtube_video: Any
    youtube_channel: Any
    topic: Any
    user_interest: Any
    webpage: Any
    app_payment_model: Any
    custom_affinity: Any
    custom_intent: Any
    custom_audience: Any
    combined_audience: Any
