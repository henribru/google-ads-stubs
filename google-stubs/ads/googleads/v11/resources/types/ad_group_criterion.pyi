import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    criteria as criteria,
    custom_parameter as custom_parameter,
)
from google.ads.googleads.v11.enums.types import (
    ad_group_criterion_approval_status as ad_group_criterion_approval_status,
    ad_group_criterion_status as ad_group_criterion_status,
    bidding_source as bidding_source,
    criterion_system_serving_status as criterion_system_serving_status,
    criterion_type as criterion_type,
    quality_score_bucket as quality_score_bucket,
)

__protobuf__: Incomplete

class AdGroupCriterion(proto.Message):
    class QualityInfo(proto.Message):
        quality_score: Incomplete
        creative_quality_score: Incomplete
        post_click_quality_score: Incomplete
        search_predicted_ctr: Incomplete

    class PositionEstimates(proto.Message):
        first_page_cpc_micros: Incomplete
        first_position_cpc_micros: Incomplete
        top_of_page_cpc_micros: Incomplete
        estimated_add_clicks_at_first_position_cpc: Incomplete
        estimated_add_cost_at_first_position_cpc: Incomplete
    resource_name: Incomplete
    criterion_id: Incomplete
    display_name: Incomplete
    status: Incomplete
    quality_info: Incomplete
    ad_group: Incomplete
    type_: Incomplete
    negative: Incomplete
    system_serving_status: Incomplete
    approval_status: Incomplete
    disapproval_reasons: Incomplete
    labels: Incomplete
    bid_modifier: Incomplete
    cpc_bid_micros: Incomplete
    cpm_bid_micros: Incomplete
    cpv_bid_micros: Incomplete
    percent_cpc_bid_micros: Incomplete
    effective_cpc_bid_micros: Incomplete
    effective_cpm_bid_micros: Incomplete
    effective_cpv_bid_micros: Incomplete
    effective_percent_cpc_bid_micros: Incomplete
    effective_cpc_bid_source: Incomplete
    effective_cpm_bid_source: Incomplete
    effective_cpv_bid_source: Incomplete
    effective_percent_cpc_bid_source: Incomplete
    position_estimates: Incomplete
    final_urls: Incomplete
    final_mobile_urls: Incomplete
    final_url_suffix: Incomplete
    tracking_url_template: Incomplete
    url_custom_parameters: Incomplete
    keyword: Incomplete
    placement: Incomplete
    mobile_app_category: Incomplete
    mobile_application: Incomplete
    listing_group: Incomplete
    age_range: Incomplete
    gender: Incomplete
    income_range: Incomplete
    parental_status: Incomplete
    user_list: Incomplete
    youtube_video: Incomplete
    youtube_channel: Incomplete
    topic: Incomplete
    user_interest: Incomplete
    webpage: Incomplete
    app_payment_model: Incomplete
    custom_affinity: Incomplete
    custom_intent: Incomplete
    custom_audience: Incomplete
    combined_audience: Incomplete
    audience: Incomplete
