import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import criteria as criteria, dates as dates
from google.ads.googleads.v10.enums.types import (
    frequency_cap_time_unit as frequency_cap_time_unit,
    reach_plan_ad_length as reach_plan_ad_length,
    reach_plan_age_range as reach_plan_age_range,
    reach_plan_network as reach_plan_network,
)

__protobuf__: Incomplete

class ListPlannableLocationsRequest(proto.Message): ...

class ListPlannableLocationsResponse(proto.Message):
    plannable_locations: Incomplete

class PlannableLocation(proto.Message):
    id: Incomplete
    name: Incomplete
    parent_country_id: Incomplete
    country_code: Incomplete
    location_type: Incomplete

class ListPlannableProductsRequest(proto.Message):
    plannable_location_id: Incomplete

class ListPlannableProductsResponse(proto.Message):
    product_metadata: Incomplete

class ProductMetadata(proto.Message):
    plannable_product_code: Incomplete
    plannable_product_name: Incomplete
    plannable_targeting: Incomplete

class PlannableTargeting(proto.Message):
    age_ranges: Incomplete
    genders: Incomplete
    devices: Incomplete
    networks: Incomplete

class GenerateProductMixIdeasRequest(proto.Message):
    customer_id: Incomplete
    plannable_location_id: Incomplete
    currency_code: Incomplete
    budget_micros: Incomplete
    preferences: Incomplete

class Preferences(proto.Message):
    is_skippable: Incomplete
    starts_with_sound: Incomplete
    ad_length: Incomplete
    top_content_only: Incomplete
    has_guaranteed_price: Incomplete

class GenerateProductMixIdeasResponse(proto.Message):
    product_allocation: Incomplete

class ProductAllocation(proto.Message):
    plannable_product_code: Incomplete
    budget_micros: Incomplete

class GenerateReachForecastRequest(proto.Message):
    customer_id: Incomplete
    currency_code: Incomplete
    campaign_duration: Incomplete
    cookie_frequency_cap: Incomplete
    cookie_frequency_cap_setting: Incomplete
    min_effective_frequency: Incomplete
    effective_frequency_limit: Incomplete
    targeting: Incomplete
    planned_products: Incomplete

class EffectiveFrequencyLimit(proto.Message):
    effective_frequency_breakdown_limit: Incomplete

class FrequencyCap(proto.Message):
    impressions: Incomplete
    time_unit: Incomplete

class Targeting(proto.Message):
    plannable_location_id: Incomplete
    age_range: Incomplete
    genders: Incomplete
    devices: Incomplete
    network: Incomplete

class CampaignDuration(proto.Message):
    duration_in_days: Incomplete
    date_range: Incomplete

class PlannedProduct(proto.Message):
    plannable_product_code: Incomplete
    budget_micros: Incomplete

class GenerateReachForecastResponse(proto.Message):
    on_target_audience_metrics: Incomplete
    reach_curve: Incomplete

class ReachCurve(proto.Message):
    reach_forecasts: Incomplete

class ReachForecast(proto.Message):
    cost_micros: Incomplete
    forecast: Incomplete
    planned_product_reach_forecasts: Incomplete

class Forecast(proto.Message):
    on_target_reach: Incomplete
    total_reach: Incomplete
    on_target_impressions: Incomplete
    total_impressions: Incomplete
    viewable_impressions: Incomplete
    effective_frequency_breakdowns: Incomplete

class PlannedProductReachForecast(proto.Message):
    plannable_product_code: Incomplete
    cost_micros: Incomplete
    planned_product_forecast: Incomplete

class PlannedProductForecast(proto.Message):
    on_target_reach: Incomplete
    total_reach: Incomplete
    on_target_impressions: Incomplete
    total_impressions: Incomplete
    viewable_impressions: Incomplete

class OnTargetAudienceMetrics(proto.Message):
    youtube_audience_size: Incomplete
    census_audience_size: Incomplete

class EffectiveFrequencyBreakdown(proto.Message):
    effective_frequency: Incomplete
    on_target_reach: Incomplete
    total_reach: Incomplete
