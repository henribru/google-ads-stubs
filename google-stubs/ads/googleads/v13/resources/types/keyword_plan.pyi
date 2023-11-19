from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v13.common.types.dates import DateRange
from google.ads.googleads.v13.enums.types.keyword_plan_forecast_interval import (
    KeywordPlanForecastIntervalEnum,
)

_M = TypeVar("_M")

class KeywordPlan(proto.Message):
    resource_name: str
    id: int
    name: str
    forecast_period: KeywordPlanForecastPeriod
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        forecast_period: KeywordPlanForecastPeriod = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "id", "name", "forecast_period"]) -> bool: ...  # type: ignore[override]

class KeywordPlanForecastPeriod(proto.Message):
    date_interval: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    date_range: DateRange
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        date_interval: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval = ...,
        date_range: DateRange = ...
    ) -> None: ...
    def __contains__(self, key: Literal["date_interval", "date_range"]) -> bool: ...  # type: ignore[override]
