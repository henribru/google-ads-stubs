import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import month_of_year as month_of_year
from google.ads.googleads.v11.resources.types import invoice as invoice

__protobuf__: Incomplete

class ListInvoicesRequest(proto.Message):
    customer_id: Incomplete
    billing_setup: Incomplete
    issue_year: Incomplete
    issue_month: Incomplete

class ListInvoicesResponse(proto.Message):
    invoices: Incomplete
