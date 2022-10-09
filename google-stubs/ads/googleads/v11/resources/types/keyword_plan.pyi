import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import dates as dates
from google.ads.googleads.v11.enums.types import (
    keyword_plan_forecast_interval as keyword_plan_forecast_interval,
)

__protobuf__: Incomplete

class KeywordPlan(proto.Message):
    resource_name: Incomplete
    id: Incomplete
    name: Incomplete
    forecast_period: Incomplete

class KeywordPlanForecastPeriod(proto.Message):
    date_interval: Incomplete
    date_range: Incomplete
