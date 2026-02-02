from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.month_of_year import MonthOfYearEnum
from google.ads.googleads.v23.resources.types.invoice import Invoice

_M = TypeVar("_M")

class ListInvoicesRequest(proto.Message):
    customer_id: str
    billing_setup: str
    issue_year: str
    issue_month: MonthOfYearEnum.MonthOfYear
    include_granular_level_invoice_details: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        billing_setup: str = ...,
        issue_year: str = ...,
        issue_month: MonthOfYearEnum.MonthOfYear = ...,
        include_granular_level_invoice_details: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "billing_setup",
            "issue_year",
            "issue_month",
            "include_granular_level_invoice_details",
        ],
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
