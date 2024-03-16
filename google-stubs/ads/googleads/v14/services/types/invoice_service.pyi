from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.month_of_year import MonthOfYearEnum
from google.ads.googleads.v14.resources.types.invoice import Invoice

_M = TypeVar("_M")

class ListInvoicesRequest(proto.Message):
    customer_id: str
    billing_setup: str
    issue_year: str
    issue_month: MonthOfYearEnum.MonthOfYear
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        billing_setup: str = ...,
        issue_year: str = ...,
        issue_month: MonthOfYearEnum.MonthOfYear = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "billing_setup", "issue_year", "issue_month"]
    ) -> bool: ...

class ListInvoicesResponse(proto.Message):
    invoices: MutableSequence[Invoice]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        invoices: MutableSequence[Invoice] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["invoices"]
    ) -> bool: ...
