from typing import Any

import proto

from google.ads.googleads.v8.common.types import dates as dates
from google.ads.googleads.v8.enums.types import (
    keyword_plan_forecast_interval as keyword_plan_forecast_interval,
)

__protobuf__: Any

class KeywordPlan(proto.Message):
    resource_name: Any
    id: Any
    name: Any
    forecast_period: Any

class KeywordPlanForecastPeriod(proto.Message):
    date_interval: Any
    date_range: Any
