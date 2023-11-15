from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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
        end_date: str = ...
    ) -> None: ...

class YearMonth(proto.Message):
    year: int
    month: MonthOfYearEnum.MonthOfYear
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        year: int = ...,
        month: MonthOfYearEnum.MonthOfYear = ...
    ) -> None: ...

class YearMonthRange(proto.Message):
    start: YearMonth
    end: YearMonth
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        start: YearMonth = ...,
        end: YearMonth = ...
    ) -> None: ...
