import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import dates
from google.ads.googleads.v19.enums.types import keyword_plan_forecast_interval

__protobuf__: Incomplete

class KeywordPlan(proto.Message):
    resource_name: str
    id: int
    name: str
    forecast_period: KeywordPlanForecastPeriod

class KeywordPlanForecastPeriod(proto.Message):
    date_interval: keyword_plan_forecast_interval.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval
    date_range: dates.DateRange
