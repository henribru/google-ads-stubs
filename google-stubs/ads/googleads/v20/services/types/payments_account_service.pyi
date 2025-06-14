import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.resources.types import payments_account
from typing import MutableSequence

__protobuf__: Incomplete

class ListPaymentsAccountsRequest(proto.Message):
    customer_id: str

class ListPaymentsAccountsResponse(proto.Message):
    payments_accounts: MutableSequence[payments_account.PaymentsAccount]
