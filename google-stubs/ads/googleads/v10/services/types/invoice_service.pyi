from typing import Any

import proto

from google.ads.googleads.v10.enums.types.month_of_year import MonthOfYearEnum
from google.ads.googleads.v10.resources.types.invoice import Invoice

class ListInvoicesRequest(proto.Message):
    customer_id: str
    billing_setup: str
    issue_year: str
    issue_month: MonthOfYearEnum.MonthOfYear
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        billing_setup: str = ...,
        issue_year: str = ...,
        issue_month: MonthOfYearEnum.MonthOfYear = ...
    ) -> None: ...

class ListInvoicesResponse(proto.Message):
    invoices: list[Invoice]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        invoices: list[Invoice] = ...
    ) -> None: ...
