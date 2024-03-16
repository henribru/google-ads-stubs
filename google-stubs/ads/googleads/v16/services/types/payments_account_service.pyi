from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.resources.types.payments_account import PaymentsAccount

_M = TypeVar("_M")

class ListPaymentsAccountsRequest(proto.Message):
    customer_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id"]
    ) -> bool: ...

class ListPaymentsAccountsResponse(proto.Message):
    payments_accounts: MutableSequence[PaymentsAccount]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        payments_accounts: MutableSequence[PaymentsAccount] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["payments_accounts"]
    ) -> bool: ...
