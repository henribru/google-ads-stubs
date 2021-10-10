from typing import Any

import proto

from google.ads.googleads.v7.common.types import criteria as criteria
from google.ads.googleads.v7.enums.types import (
    frequency_cap_time_unit as frequency_cap_time_unit,
    reach_plan_ad_length as reach_plan_ad_length,
    reach_plan_age_range as reach_plan_age_range,
    reach_plan_network as reach_plan_network,
)

__protobuf__: Any

class ListPlannableLocationsRequest(proto.Message): ...

class ListPlannableLocationsResponse(proto.Message):
    plannable_locations: Any

class PlannableLocation(proto.Message):
    id: Any
    name: Any
    parent_country_id: Any

class ListPlannableProductsRequest(proto.Message):
    plannable_location_id: Any

class ListPlannableProductsResponse(proto.Message):
    product_metadata: Any

class ProductMetadata(proto.Message):
    plannable_product_code: Any
    plannable_product_name: Any
    plannable_targeting: Any

class PlannableTargeting(proto.Message):
    age_ranges: Any
    genders: Any
    devices: Any
    networks: Any

class GenerateProductMixIdeasRequest(proto.Message):
    customer_id: Any
    plannable_location_id: Any
    currency_code: Any
    budget_micros: Any
    preferences: Any

class Preferences(proto.Message):
    is_skippable: Any
    starts_with_sound: Any
    ad_length: Any
    top_content_only: Any
    has_guaranteed_price: Any

class GenerateProductMixIdeasResponse(proto.Message):
    product_allocation: Any

class ProductAllocation(proto.Message):
    plannable_product_code: Any
    budget_micros: Any

class GenerateReachForecastRequest(proto.Message):
    customer_id: Any
    currency_code: Any
    campaign_duration: Any
    cookie_frequency_cap: Any
    cookie_frequency_cap_setting: Any
    min_effective_frequency: Any
    targeting: Any
    planned_products: Any

class FrequencyCap(proto.Message):
    impressions: Any
    time_unit: Any

class Targeting(proto.Message):
    plannable_location_id: Any
    age_range: Any
    genders: Any
    devices: Any
    network: Any

class CampaignDuration(proto.Message):
    duration_in_days: Any

class PlannedProduct(proto.Message):
    plannable_product_code: Any
    budget_micros: Any

class GenerateReachForecastResponse(proto.Message):
    on_target_audience_metrics: Any
    reach_curve: Any

class ReachCurve(proto.Message):
    reach_forecasts: Any

class ReachForecast(proto.Message):
    cost_micros: Any
    forecast: Any
    planned_product_reach_forecasts: Any

class Forecast(proto.Message):
    on_target_reach: Any
    total_reach: Any
    on_target_impressions: Any
    total_impressions: Any
    viewable_impressions: Any

class PlannedProductReachForecast(proto.Message):
    plannable_product_code: Any
    cost_micros: Any
    planned_product_forecast: Any

class PlannedProductForecast(proto.Message):
    on_target_reach: Any
    total_reach: Any
    on_target_impressions: Any
    total_impressions: Any
    viewable_impressions: Any

class OnTargetAudienceMetrics(proto.Message):
    youtube_audience_size: Any
    census_audience_size: Any
