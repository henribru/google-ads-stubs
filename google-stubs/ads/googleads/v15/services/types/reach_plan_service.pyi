from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.criteria import (
    DeviceInfo,
    GenderInfo,
    UserInterestInfo,
)
from google.ads.googleads.v15.common.types.dates import DateRange
from google.ads.googleads.v15.enums.types.frequency_cap_time_unit import (
    FrequencyCapTimeUnitEnum,
)
from google.ads.googleads.v15.enums.types.reach_plan_age_range import (
    ReachPlanAgeRangeEnum,
)
from google.ads.googleads.v15.enums.types.reach_plan_network import ReachPlanNetworkEnum
from google.ads.googleads.v15.enums.types.reach_plan_surface import ReachPlanSurfaceEnum
from google.ads.googleads.v15.enums.types.target_frequency_time_unit import (
    TargetFrequencyTimeUnitEnum,
)

_M = TypeVar("_M")

class AdvancedProductTargeting(proto.Message):
    surface_targeting_settings: SurfaceTargeting
    target_frequency_settings: TargetFrequencySettings
    youtube_select_settings: YouTubeSelectSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        surface_targeting_settings: SurfaceTargeting = ...,
        target_frequency_settings: TargetFrequencySettings = ...,
        youtube_select_settings: YouTubeSelectSettings = ...,
    ) -> None: ...

class AudienceTargeting(proto.Message):
    user_interest: MutableSequence[UserInterestInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_interest: MutableSequence[UserInterestInfo] = ...,
    ) -> None: ...

class CampaignDuration(proto.Message):
    duration_in_days: int
    date_range: DateRange
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        effective_frequency: int = ...,
        on_target_reach: int = ...,
        total_reach: int = ...,
        effective_coview_reach: int = ...,
        on_target_effective_coview_reach: int = ...,
    ) -> None: ...

class EffectiveFrequencyLimit(proto.Message):
    effective_frequency_breakdown_limit: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        effective_frequency_breakdown_limit: int = ...,
    ) -> None: ...

class Forecast(proto.Message):
    on_target_reach: int
    total_reach: int
    on_target_impressions: int
    total_impressions: int
    viewable_impressions: int
    effective_frequency_breakdowns: MutableSequence[EffectiveFrequencyBreakdown]
    on_target_coview_reach: int
    total_coview_reach: int
    on_target_coview_impressions: int
    total_coview_impressions: int
    views: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        on_target_reach: int = ...,
        total_reach: int = ...,
        on_target_impressions: int = ...,
        total_impressions: int = ...,
        viewable_impressions: int = ...,
        effective_frequency_breakdowns: MutableSequence[
            EffectiveFrequencyBreakdown
        ] = ...,
        on_target_coview_reach: int = ...,
        total_coview_reach: int = ...,
        on_target_coview_impressions: int = ...,
        total_coview_impressions: int = ...,
        views: int = ...,
    ) -> None: ...

class ForecastMetricOptions(proto.Message):
    include_coview: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        include_coview: bool = ...,
    ) -> None: ...

class FrequencyCap(proto.Message):
    impressions: int
    time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        impressions: int = ...,
        time_unit: FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit = ...,
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
    planned_products: MutableSequence[PlannedProduct]
    forecast_metric_options: ForecastMetricOptions
    customer_reach_group: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        currency_code: str = ...,
        campaign_duration: CampaignDuration = ...,
        cookie_frequency_cap: int = ...,
        cookie_frequency_cap_setting: FrequencyCap = ...,
        min_effective_frequency: int = ...,
        effective_frequency_limit: EffectiveFrequencyLimit = ...,
        targeting: Targeting = ...,
        planned_products: MutableSequence[PlannedProduct] = ...,
        forecast_metric_options: ForecastMetricOptions = ...,
        customer_reach_group: str = ...,
    ) -> None: ...

class GenerateReachForecastResponse(proto.Message):
    on_target_audience_metrics: OnTargetAudienceMetrics
    reach_curve: ReachCurve
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        on_target_audience_metrics: OnTargetAudienceMetrics = ...,
        reach_curve: ReachCurve = ...,
    ) -> None: ...

class ListPlannableLocationsRequest(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    ...

class ListPlannableLocationsResponse(proto.Message):
    plannable_locations: MutableSequence[PlannableLocation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_locations: MutableSequence[PlannableLocation] = ...,
    ) -> None: ...

class ListPlannableProductsRequest(proto.Message):
    plannable_location_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_location_id: str = ...,
    ) -> None: ...

class ListPlannableProductsResponse(proto.Message):
    product_metadata: MutableSequence[ProductMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        product_metadata: MutableSequence[ProductMetadata] = ...,
    ) -> None: ...

class OnTargetAudienceMetrics(proto.Message):
    youtube_audience_size: int
    census_audience_size: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        id: str = ...,
        name: str = ...,
        parent_country_id: int = ...,
        country_code: str = ...,
        location_type: str = ...,
    ) -> None: ...

class PlannableTargeting(proto.Message):
    age_ranges: MutableSequence[ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    genders: MutableSequence[GenderInfo]
    devices: MutableSequence[DeviceInfo]
    networks: MutableSequence[ReachPlanNetworkEnum.ReachPlanNetwork]
    youtube_select_lineups: MutableSequence[YouTubeSelectLineUp]
    surface_targeting: SurfaceTargetingCombinations
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        age_ranges: MutableSequence[ReachPlanAgeRangeEnum.ReachPlanAgeRange] = ...,
        genders: MutableSequence[GenderInfo] = ...,
        devices: MutableSequence[DeviceInfo] = ...,
        networks: MutableSequence[ReachPlanNetworkEnum.ReachPlanNetwork] = ...,
        youtube_select_lineups: MutableSequence[YouTubeSelectLineUp] = ...,
        surface_targeting: SurfaceTargetingCombinations = ...,
    ) -> None: ...

class PlannedProduct(proto.Message):
    plannable_product_code: str
    budget_micros: int
    advanced_product_targeting: AdvancedProductTargeting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
    average_frequency: float
    views: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        on_target_reach: int = ...,
        total_reach: int = ...,
        on_target_impressions: int = ...,
        total_impressions: int = ...,
        viewable_impressions: int = ...,
        on_target_coview_reach: int = ...,
        total_coview_reach: int = ...,
        on_target_coview_impressions: int = ...,
        total_coview_impressions: int = ...,
        average_frequency: float = ...,
        views: int = ...,
    ) -> None: ...

class PlannedProductReachForecast(proto.Message):
    plannable_product_code: str
    cost_micros: int
    planned_product_forecast: PlannedProductForecast
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_product_code: str = ...,
        cost_micros: int = ...,
        planned_product_forecast: PlannedProductForecast = ...,
    ) -> None: ...

class ProductMetadata(proto.Message):
    plannable_product_code: str
    plannable_product_name: str
    plannable_targeting: PlannableTargeting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_product_code: str = ...,
        plannable_product_name: str = ...,
        plannable_targeting: PlannableTargeting = ...,
    ) -> None: ...

class ReachCurve(proto.Message):
    reach_forecasts: MutableSequence[ReachForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        reach_forecasts: MutableSequence[ReachForecast] = ...,
    ) -> None: ...

class ReachForecast(proto.Message):
    cost_micros: int
    forecast: Forecast
    planned_product_reach_forecasts: MutableSequence[PlannedProductReachForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        cost_micros: int = ...,
        forecast: Forecast = ...,
        planned_product_reach_forecasts: MutableSequence[
            PlannedProductReachForecast
        ] = ...,
    ) -> None: ...

class SurfaceTargeting(proto.Message):
    surfaces: MutableSequence[ReachPlanSurfaceEnum.ReachPlanSurface]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        surfaces: MutableSequence[ReachPlanSurfaceEnum.ReachPlanSurface] = ...,
    ) -> None: ...

class SurfaceTargetingCombinations(proto.Message):
    default_targeting: SurfaceTargeting
    available_targeting_combinations: MutableSequence[SurfaceTargeting]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        default_targeting: SurfaceTargeting = ...,
        available_targeting_combinations: MutableSequence[SurfaceTargeting] = ...,
    ) -> None: ...

class TargetFrequencySettings(proto.Message):
    time_unit: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit
    target_frequency: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        time_unit: TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit = ...,
        target_frequency: int = ...,
    ) -> None: ...

class Targeting(proto.Message):
    plannable_location_id: str
    plannable_location_ids: MutableSequence[str]
    age_range: ReachPlanAgeRangeEnum.ReachPlanAgeRange
    genders: MutableSequence[GenderInfo]
    devices: MutableSequence[DeviceInfo]
    network: ReachPlanNetworkEnum.ReachPlanNetwork
    audience_targeting: AudienceTargeting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_location_id: str = ...,
        plannable_location_ids: MutableSequence[str] = ...,
        age_range: ReachPlanAgeRangeEnum.ReachPlanAgeRange = ...,
        genders: MutableSequence[GenderInfo] = ...,
        devices: MutableSequence[DeviceInfo] = ...,
        network: ReachPlanNetworkEnum.ReachPlanNetwork = ...,
        audience_targeting: AudienceTargeting = ...,
    ) -> None: ...

class YouTubeSelectLineUp(proto.Message):
    lineup_id: int
    lineup_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        lineup_id: int = ...,
        lineup_name: str = ...,
    ) -> None: ...

class YouTubeSelectSettings(proto.Message):
    lineup_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        lineup_id: int = ...,
    ) -> None: ...
