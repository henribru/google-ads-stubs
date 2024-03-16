from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.criteria import (
    DeviceInfo,
    GenderInfo,
    UserInterestInfo,
)
from google.ads.googleads.v14.common.types.dates import DateRange
from google.ads.googleads.v14.enums.types.frequency_cap_time_unit import (
    FrequencyCapTimeUnitEnum,
)
from google.ads.googleads.v14.enums.types.reach_plan_age_range import (
    ReachPlanAgeRangeEnum,
)
from google.ads.googleads.v14.enums.types.reach_plan_network import ReachPlanNetworkEnum

_M = TypeVar("_M")

class AdvancedProductTargeting(proto.Message):
    youtube_select_settings: YouTubeSelectSettings
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        youtube_select_settings: YouTubeSelectSettings = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["youtube_select_settings"]
    ) -> bool: ...

class AudienceTargeting(proto.Message):
    user_interest: MutableSequence[UserInterestInfo]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_interest: MutableSequence[UserInterestInfo] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_interest"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["duration_in_days", "date_range"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "effective_frequency",
            "on_target_reach",
            "total_reach",
            "effective_coview_reach",
            "on_target_effective_coview_reach",
        ],
    ) -> bool: ...

class EffectiveFrequencyLimit(proto.Message):
    effective_frequency_breakdown_limit: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        effective_frequency_breakdown_limit: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["effective_frequency_breakdown_limit"]
    ) -> bool: ...

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
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "on_target_reach",
            "total_reach",
            "on_target_impressions",
            "total_impressions",
            "viewable_impressions",
            "effective_frequency_breakdowns",
            "on_target_coview_reach",
            "total_coview_reach",
            "on_target_coview_impressions",
            "total_coview_impressions",
        ],
    ) -> bool: ...

class ForecastMetricOptions(proto.Message):
    include_coview: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        include_coview: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["include_coview"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["impressions", "time_unit"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "currency_code",
            "campaign_duration",
            "cookie_frequency_cap",
            "cookie_frequency_cap_setting",
            "min_effective_frequency",
            "effective_frequency_limit",
            "targeting",
            "planned_products",
            "forecast_metric_options",
            "customer_reach_group",
        ],
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["on_target_audience_metrics", "reach_curve"]
    ) -> bool: ...

class ListPlannableLocationsRequest(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...

class ListPlannableLocationsResponse(proto.Message):
    plannable_locations: MutableSequence[PlannableLocation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_locations: MutableSequence[PlannableLocation] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["plannable_locations"]
    ) -> bool: ...

class ListPlannableProductsRequest(proto.Message):
    plannable_location_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        plannable_location_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["plannable_location_id"]
    ) -> bool: ...

class ListPlannableProductsResponse(proto.Message):
    product_metadata: MutableSequence[ProductMetadata]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        product_metadata: MutableSequence[ProductMetadata] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["product_metadata"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["youtube_audience_size", "census_audience_size"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "id", "name", "parent_country_id", "country_code", "location_type"
        ],
    ) -> bool: ...

class PlannableTargeting(proto.Message):
    age_ranges: MutableSequence[ReachPlanAgeRangeEnum.ReachPlanAgeRange]
    genders: MutableSequence[GenderInfo]
    devices: MutableSequence[DeviceInfo]
    networks: MutableSequence[ReachPlanNetworkEnum.ReachPlanNetwork]
    youtube_select_lineups: MutableSequence[YouTubeSelectLineUp]
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
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "age_ranges", "genders", "devices", "networks", "youtube_select_lineups"
        ],
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "plannable_product_code", "budget_micros", "advanced_product_targeting"
        ],
    ) -> bool: ...

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
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "on_target_reach",
            "total_reach",
            "on_target_impressions",
            "total_impressions",
            "viewable_impressions",
            "on_target_coview_reach",
            "total_coview_reach",
            "on_target_coview_impressions",
            "total_coview_impressions",
        ],
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "plannable_product_code", "cost_micros", "planned_product_forecast"
        ],
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "plannable_product_code", "plannable_product_name", "plannable_targeting"
        ],
    ) -> bool: ...

class ReachCurve(proto.Message):
    reach_forecasts: MutableSequence[ReachForecast]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        reach_forecasts: MutableSequence[ReachForecast] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["reach_forecasts"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["cost_micros", "forecast", "planned_product_reach_forecasts"]
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "plannable_location_id",
            "plannable_location_ids",
            "age_range",
            "genders",
            "devices",
            "network",
            "audience_targeting",
        ],
    ) -> bool: ...

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
    def __contains__(  # type: ignore[override]
        self, key: Literal["lineup_id", "lineup_name"]
    ) -> bool: ...

class YouTubeSelectSettings(proto.Message):
    lineup_id: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        lineup_id: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["lineup_id"]
    ) -> bool: ...
