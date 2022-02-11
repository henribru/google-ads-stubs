from typing import Any

import proto

from google.ads.googleads.v9.enums.types import month_of_year as month_of_year
from google.ads.googleads.v9.resources.types import invoice as invoice

__protobuf__: Any

class ListInvoicesRequest(proto.Message):
    customer_id: Any
    billing_setup: Any
    issue_year: Any
    issue_month: Any

class ListInvoicesResponse(proto.Message):
    invoices: Any
