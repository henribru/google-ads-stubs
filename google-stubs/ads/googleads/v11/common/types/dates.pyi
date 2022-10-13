from typing import Any

import proto

from google.ads.googleads.v11.enums.types.month_of_year import MonthOfYearEnum

class DateRange(proto.Message):
    start_date: str
    end_date: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        start_date: str = ...,
        end_date: str = ...
    ) -> None: ...

class YearMonth(proto.Message):
    year: int
    month: MonthOfYearEnum.MonthOfYear
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        year: int = ...,
        month: MonthOfYearEnum.MonthOfYear = ...
    ) -> None: ...

class YearMonthRange(proto.Message):
    start: YearMonth
    end: YearMonth
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        start: YearMonth = ...,
        end: YearMonth = ...
    ) -> None: ...
