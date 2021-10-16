from typing import Any

import proto

from google.ads.googleads.v7.resources.types import payments_account as payments_account

__protobuf__: Any

class ListPaymentsAccountsRequest(proto.Message):
    customer_id: Any

class ListPaymentsAccountsResponse(proto.Message):
    payments_accounts: Any
