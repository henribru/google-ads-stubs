from typing import Any

import proto

from google.ads.googleads.v11.resources.types.payments_account import PaymentsAccount

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
    payments_accounts: list[PaymentsAccount]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        payments_accounts: list[PaymentsAccount] = ...
    ) -> None: ...
