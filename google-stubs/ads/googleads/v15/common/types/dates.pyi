from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.month_of_year import MonthOfYearEnum

_M = TypeVar("_M")

class DateRange(proto.Message):
    start_date: str
    end_date: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        start_date: str = ...,
        end_date: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["start_date", "end_date"]
    ) -> bool: ...

class YearMonth(proto.Message):
    year: int
    month: MonthOfYearEnum.MonthOfYear
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        year: int = ...,
        month: MonthOfYearEnum.MonthOfYear = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["year", "month"]
    ) -> bool: ...

class YearMonthRange(proto.Message):
    start: YearMonth
    end: YearMonth
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        start: YearMonth = ...,
        end: YearMonth = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["start", "end"]
    ) -> bool: ...
