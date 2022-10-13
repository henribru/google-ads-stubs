from typing import Any

import proto

from google.ads.googleads.v11.common.types.criteria import (
    DeviceInfo,
    GenderInfo,
    UserInterestInfo,
)
from google.ads.googleads.v11.common.types.dates import DateRange
from google.ads.googleads.v11.enums.types.frequency_cap_time_unit import (
    FrequencyCapTimeUnitEnum,
)
from google.ads.googleads.v11.enums.types.reach_plan_ad_length import (
    ReachPlanAdLengthEnum,
)
from google.ads.googleads.v11.enums.types.reach_plan_age_range import (
    ReachPlanAgeRangeEnum,
)
from google.ads.googleads.v11.enums.types.reach_plan_network import ReachPlanNetworkEnum

class AdvancedProductTargeting(proto.Message):
    youtube_select_settings: YouTubeSelectSettings
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        youtube_select_settings: YouTubeSelectSettings = ...,
    ) -> None: ...

class AudienceTargeting(proto.Message):
    user_interest: list[UserInterestInfo]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_interest: list[UserInterestInfo] = ...,
    ) -> None: ...

class CampaignDuration(proto.Message):
    duration_in_days: int
    date_range: DateRange
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        duration_in_days: int = ...,
        date_range: DateRange = ...,
    ) -> None: ...

class EffectiveFrequencyBreakdown(proto.Message):
    effective_frequency: int
    on_target_reach: int
    total_reach: int
    effective_coview_reach: int
    on_target_effective_coview_reach: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        effective_frequency: int = ...,
        on_target_reach: int = ...,
        total_reach: int = ...,
        effective_coview_reach: int = ...,
        on_target_effective_coview_reach: int = ...,
    ) -> None: ...

class EffectiveFrequencyLimit(proto.Message):
    effective_frequency_breakdown_limit: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        effective_frequency_breakdown_limit: int = ...,
    ) -> None: ...

class Forecast(proto.Message):
    on_target_reach: int
    total_reach: int
    on_target_impressions: int
    total_impressions: int
    viewable_impressions: int
    effective_frequency_breakdowns: list[EffectiveFrequencyBreakdown]
    on_target_coview_reach: int
    total_coview_reach: int
    on_target_coview_impressions: int
    total_coview_impressions: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        on_target_reach: int = ...,
        total_reach: int = ...,
        on_target_impressions: int = ...,
        total_impressions: int = ...,
        viewable_impressions: int = ...,
        effective_frequency_breakdowns: list[EffectiveFrequencyBreakdown] = ...,
        on_target_coview_reach: int = ...,
        total_coview_reach: int = ...,
        on_target_coview_impressions: int = ...,
        total_coview_impressions: int = ...,
    ) -> None: ...

class ForecastMetricOptions(proto.Message):
    include_coview: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        include_coview: bool = ...,
    ) -> None: ...

class FrequencyCap(proto.Message):
    impressions: int
    time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        impressions: int = ...,
        time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit = ...,
    ) -> None: ...

class GenerateProductMixIdeasRequest(proto.Message):
    customer_id: str
    plannable_location_id: str
    currency_code: str
    budget_micros: int
    preferences: Preferences
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        plannable_location_id: str = ...,
        currency_code: str = ...,
        budget_micros: int = ...,
        preferences: Preferences = ...,
    ) -> None: ...

class GenerateProductMixIdeasResponse(proto.Message):
    product_allocation: list[ProductAllocation]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        product_allocation: list[ProductAllocation] = ...,
    ) -> None: ...

class GenerateReachForecastRequest(proto.Message):
    customer_id: str
    currency_code: str
    campaign_duration: CampaignDuration
    cookie_frequency_cap: int
    cookie_frequency_cap_setting: FrequencyCap
    min_effective_frequency: int
    effective_frequency_limit: EffectiveFrequencyLimit
    targeting: Targeting
    planned_products: list[PlannedProduct]
    forecast_metric_options: ForecastMetricOptions
    customer_reach_group: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        currency_code: str = ...,
        campaign_duration: CampaignDuration = ...,
        cookie_frequency_cap: int = ...,
        cookie_frequency_cap_setting: FrequencyCap = ...,
        min_effective_frequency: int = ...,
        effective_frequency_limit: EffectiveFrequencyLimit = ...,
        targeting: Targeting = ...,
        planned_products: list[PlannedProduct] = ...,
        forecast_metric_options: ForecastMetricOptions = ...,
        customer_reach_group: str = ...,
    ) -> None: ...

class GenerateReachForecastResponse(proto.Message):
    on_target_audience_metrics: OnTargetAudienceMetrics
    reach_curve: ReachCurve
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        on_target_audience_metrics: OnTargetAudienceMetrics = ...,
        reach_curve: ReachCurve = ...,
    ) -> None: ...

class ListPlannableLocationsRequest(proto.Message):
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
    ...

class ListPlannableLocationsResponse(proto.Message):
    plannable_locations: list[PlannableLocation]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_locations: list[PlannableLocation] = ...,
    ) -> None: ...

class ListPlannableProductsRequest(proto.Message):
    plannable_location_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_location_id: str = ...,
    ) -> None: ...

class ListPlannableProductsResponse(proto.Message):
    product_metadata: list[ProductMetadata]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        product_metadata: list[ProductMetadata] = ...,
    ) -> None: ...

class OnTargetAudienceMetrics(proto.Message):
    youtube_audience_size: int
    census_audience_size: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        youtube_audience_size: int = ...,
        census_audience_size: int = ...,
    ) -> None: ...

class PlannableLocation(proto.Message):
    id: str
    name: str
    parent_country_id: int
    country_code: str
    location_type: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        id: str = ...,
        name: str = ...,
        parent_country_id: int = ...,
        country_code: str = ...,
        location_type: str = ...,
    ) -> None: ...

class PlannableTargeting(proto.Message):
    age_ranges: list[ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    genders: list[GenderInfo]
    devices: list[DeviceInfo]
    networks: list[ReachPlanNetworkEnum.ReachPlanNetwork]
    youtube_select_lineups: list[YouTubeSelectLineUp]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        age_ranges: list[ReachPlanAgeRangeEnum.ReachPlanAgeRange] = ...,
        genders: list[GenderInfo] = ...,
        devices: list[DeviceInfo] = ...,
        networks: list[ReachPlanNetworkEnum.ReachPlanNetwork] = ...,
        youtube_select_lineups: list[YouTubeSelectLineUp] = ...,
    ) -> None: ...

class PlannedProduct(proto.Message):
    plannable_product_code: str
    budget_micros: int
    advanced_product_targeting: AdvancedProductTargeting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_product_code: str = ...,
        budget_micros: int = ...,
        advanced_product_targeting: AdvancedProductTargeting = ...,
    ) -> None: ...

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        on_target_reach: int = ...,
        total_reach: int = ...,
        on_target_impressions: int = ...,
        total_impressions: int = ...,
        viewable_impressions: int = ...,
        on_target_coview_reach: int = ...,
        total_coview_reach: int = ...,
        on_target_coview_impressions: int = ...,
        total_coview_impressions: int = ...,
    ) -> None: ...

class PlannedProductReachForecast(proto.Message):
    plannable_product_code: str
    cost_micros: int
    planned_product_forecast: PlannedProductForecast
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_product_code: str = ...,
        cost_micros: int = ...,
        planned_product_forecast: PlannedProductForecast = ...,
    ) -> None: ...

class Preferences(proto.Message):
    is_skippable: bool
    starts_with_sound: bool
    ad_length: ReachPlanAdLengthEnum.ReachPlanAdLength
    top_content_only: bool
    has_guaranteed_price: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        is_skippable: bool = ...,
        starts_with_sound: bool = ...,
        ad_length: ReachPlanAdLengthEnum.ReachPlanAdLength = ...,
        top_content_only: bool = ...,
        has_guaranteed_price: bool = ...,
    ) -> None: ...

class ProductAllocation(proto.Message):
    plannable_product_code: str
    budget_micros: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_product_code: str = ...,
        budget_micros: int = ...,
    ) -> None: ...

class ProductMetadata(proto.Message):
    plannable_product_code: str
    plannable_product_name: str
    plannable_targeting: PlannableTargeting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_product_code: str = ...,
        plannable_product_name: str = ...,
        plannable_targeting: PlannableTargeting = ...,
    ) -> None: ...

class ReachCurve(proto.Message):
    reach_forecasts: list[ReachForecast]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        reach_forecasts: list[ReachForecast] = ...,
    ) -> None: ...

class ReachForecast(proto.Message):
    cost_micros: int
    forecast: Forecast
    planned_product_reach_forecasts: list[PlannedProductReachForecast]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        cost_micros: int = ...,
        forecast: Forecast = ...,
        planned_product_reach_forecasts: list[PlannedProductReachForecast] = ...,
    ) -> None: ...

class Targeting(proto.Message):
    plannable_location_id: str
    age_range: ReachPlanAgeRangeEnum.ReachPlanAgeRange
    genders: list[GenderInfo]
    devices: list[DeviceInfo]
    network: ReachPlanNetworkEnum.ReachPlanNetwork
    audience_targeting: AudienceTargeting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        plannable_location_id: str = ...,
        age_range: ReachPlanAgeRangeEnum.ReachPlanAgeRange = ...,
        genders: list[GenderInfo] = ...,
        devices: list[DeviceInfo] = ...,
        network: ReachPlanNetworkEnum.ReachPlanNetwork = ...,
        audience_targeting: AudienceTargeting = ...,
    ) -> None: ...

class YouTubeSelectLineUp(proto.Message):
    lineup_id: int
    lineup_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        lineup_id: int = ...,
        lineup_name: str = ...,
    ) -> None: ...

class YouTubeSelectSettings(proto.Message):
    lineup_id: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        lineup_id: int = ...,
    ) -> None: ...
