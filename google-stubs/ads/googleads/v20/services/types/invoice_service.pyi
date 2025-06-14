import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import month_of_year
from google.ads.googleads.v20.resources.types import invoice
from typing import MutableSequence

__protobuf__: Incomplete

class ListInvoicesRequest(proto.Message):
    customer_id: str
    billing_setup: str
    issue_year: str
    issue_month: month_of_year.MonthOfYearEnum.MonthOfYear

class ListInvoicesResponse(proto.Message):
    invoices: MutableSequence[invoice.Invoice]
