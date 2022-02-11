from typing import Any

import proto

from google.ads.googleads.v9.enums.types import month_of_year as month_of_year

__protobuf__: Any

class DateRange(proto.Message):
    start_date: Any
    end_date: Any

class YearMonthRange(proto.Message):
    start: Any
    end: Any

class YearMonth(proto.Message):
    year: Any
    month: Any
