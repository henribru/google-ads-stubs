from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.month_of_year import MonthOfYearEnum
from google.ads.googleads.v15.resources.types.invoice import Invoice

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
        issue_month: MonthOfYearEnum.MonthOfYear = ...
    ) -> None: ...

class ListInvoicesResponse(proto.Message):
    invoices: MutableSequence[Invoice]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        invoices: MutableSequence[Invoice] = ...
    ) -> None: ...
