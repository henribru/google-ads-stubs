from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.resources.types.payments_account import PaymentsAccount

class ListPaymentsAccountsRequest(proto.Message):
    customer_id: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...
    ) -> None: ...

class ListPaymentsAccountsResponse(proto.Message):
    payments_accounts: MutableSequence[PaymentsAccount]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        payments_accounts: MutableSequence[PaymentsAccount] = ...
    ) -> None: ...
