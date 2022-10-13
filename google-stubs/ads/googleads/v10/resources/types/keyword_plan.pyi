from typing import Any

import proto

from google.ads.googleads.v10.common.types.dates import DateRange
from google.ads.googleads.v10.enums.types.keyword_plan_forecast_interval import (
    KeywordPlanForecastIntervalEnum,
)

class KeywordPlan(proto.Message):
    resource_name: str
    id: int
    name: str
    forecast_period: KeywordPlanForecastPeriod
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        forecast_period: KeywordPlanForecastPeriod = ...
    ) -> None: ...

class KeywordPlanForecastPeriod(proto.Message):
    date_interval: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    date_range: DateRange
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        date_interval: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval = ...,
        date_range: DateRange = ...
    ) -> None: ...
