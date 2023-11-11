from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.dates import DateRange
from google.ads.googleads.v15.enums.types.keyword_plan_forecast_interval import (
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
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        date_interval: KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval = ...,
        date_range: DateRange = ...
    ) -> None: ...
