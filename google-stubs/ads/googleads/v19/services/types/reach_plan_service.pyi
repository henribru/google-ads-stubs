import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import criteria, dates
from google.ads.googleads.v19.enums.types import frequency_cap_time_unit, reach_plan_age_range, reach_plan_conversion_rate_model, reach_plan_network, reach_plan_surface, target_frequency_time_unit
from typing import MutableSequence

__protobuf__: Incomplete

class GenerateConversionRatesRequest(proto.Message):
    customer_id: str
    customer_reach_group: str

class GenerateConversionRatesResponse(proto.Message):
    conversion_rate_suggestions: MutableSequence['ConversionRateSuggestion']

class ConversionRateSuggestion(proto.Message):
    conversion_rate_model: reach_plan_conversion_rate_model.ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    plannable_product_code: str
    conversion_rate: float

class ListPlannableLocationsRequest(proto.Message): ...

class ListPlannableLocationsResponse(proto.Message):
    plannable_locations: MutableSequence['PlannableLocation']

class PlannableLocation(proto.Message):
    id: str
    name: str
    parent_country_id: int
    country_code: str
    location_type: str

class ListPlannableProductsRequest(proto.Message):
    plannable_location_id: str

class ListPlannableProductsResponse(proto.Message):
    product_metadata: MutableSequence['ProductMetadata']

class ProductMetadata(proto.Message):
    plannable_product_code: str
    plannable_product_name: str
    plannable_targeting: PlannableTargeting

class PlannableTargeting(proto.Message):
    age_ranges: MutableSequence[reach_plan_age_range.ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    genders: MutableSequence[criteria.GenderInfo]
    devices: MutableSequence[criteria.DeviceInfo]
    networks: MutableSequence[reach_plan_network.ReachPlanNetworkEnum.ReachPlanNetwork]
    youtube_select_lineups: MutableSequence['YouTubeSelectLineUp']
    surface_targeting: SurfaceTargetingCombinations

class GenerateReachForecastRequest(proto.Message):
    customer_id: str
    currency_code: str
    campaign_duration: CampaignDuration
    cookie_frequency_cap: int
    cookie_frequency_cap_setting: FrequencyCap
    min_effective_frequency: int
    effective_frequency_limit: EffectiveFrequencyLimit
    targeting: Targeting
    planned_products: MutableSequence['PlannedProduct']
    forecast_metric_options: ForecastMetricOptions
    customer_reach_group: str

class EffectiveFrequencyLimit(proto.Message):
    effective_frequency_breakdown_limit: int

class FrequencyCap(proto.Message):
    impressions: int
    time_unit: frequency_cap_time_unit.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit

class Targeting(proto.Message):
    plannable_location_id: str
    plannable_location_ids: MutableSequence[str]
    age_range: reach_plan_age_range.ReachPlanAgeRangeEnum.ReachPlanAgeRange
    genders: MutableSequence[criteria.GenderInfo]
    devices: MutableSequence[criteria.DeviceInfo]
    network: reach_plan_network.ReachPlanNetworkEnum.ReachPlanNetwork
    audience_targeting: AudienceTargeting

class CampaignDuration(proto.Message):
    duration_in_days: int
    date_range: dates.DateRange

class PlannedProduct(proto.Message):
    plannable_product_code: str
    budget_micros: int
    conversion_rate: float
    advanced_product_targeting: AdvancedProductTargeting

class GenerateReachForecastResponse(proto.Message):
    on_target_audience_metrics: OnTargetAudienceMetrics
    reach_curve: ReachCurve

class ReachCurve(proto.Message):
    reach_forecasts: MutableSequence['ReachForecast']

class ReachForecast(proto.Message):
    cost_micros: int
    forecast: Forecast
    planned_product_reach_forecasts: MutableSequence['PlannedProductReachForecast']

class Forecast(proto.Message):
    on_target_reach: int
    total_reach: int
    on_target_impressions: int
    total_impressions: int
    viewable_impressions: int
    effective_frequency_breakdowns: MutableSequence['EffectiveFrequencyBreakdown']
    on_target_coview_reach: int
    total_coview_reach: int
    on_target_coview_impressions: int
    total_coview_impressions: int
    views: int
    conversions: float

class PlannedProductReachForecast(proto.Message):
    plannable_product_code: str
    cost_micros: int
    planned_product_forecast: PlannedProductForecast

class PlannedProductForecast(proto.Message):
    on_target_reach: int
    total_reach: int
    on_target_impressions: int
    total_impressions: int
    viewable_impressions: int
    on_target_coview_reach: int
    total_coview_reach: int
    on_target_coview_impressions: int
    total_coview_impressions: int
    average_frequency: float
    views: int
    conversions: float

class OnTargetAudienceMetrics(proto.Message):
    youtube_audience_size: int
    census_audience_size: int

class EffectiveFrequencyBreakdown(proto.Message):
    effective_frequency: int
    on_target_reach: int
    total_reach: int
    effective_coview_reach: int
    on_target_effective_coview_reach: int

class ForecastMetricOptions(proto.Message):
    include_coview: bool

class AudienceTargeting(proto.Message):
    user_interest: MutableSequence[criteria.UserInterestInfo]

class AdvancedProductTargeting(proto.Message):
    surface_targeting_settings: SurfaceTargeting
    target_frequency_settings: TargetFrequencySettings
    youtube_select_settings: YouTubeSelectSettings

class YouTubeSelectSettings(proto.Message):
    lineup_id: int

class YouTubeSelectLineUp(proto.Message):
    lineup_id: int
    lineup_name: str

class SurfaceTargetingCombinations(proto.Message):
    default_targeting: SurfaceTargeting
    available_targeting_combinations: MutableSequence['SurfaceTargeting']

class SurfaceTargeting(proto.Message):
    surfaces: MutableSequence[reach_plan_surface.ReachPlanSurfaceEnum.ReachPlanSurface]

class TargetFrequencySettings(proto.Message):
    time_unit: target_frequency_time_unit.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    target_frequency: int
