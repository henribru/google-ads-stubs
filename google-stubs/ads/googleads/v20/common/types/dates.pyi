import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import month_of_year

__protobuf__: Incomplete

class DateRange(proto.Message):
    start_date: str
    end_date: str

class YearMonthRange(proto.Message):
    start: YearMonth
    end: YearMonth

class YearMonth(proto.Message):
    year: int
    month: month_of_year.MonthOfYearEnum.MonthOfYear
