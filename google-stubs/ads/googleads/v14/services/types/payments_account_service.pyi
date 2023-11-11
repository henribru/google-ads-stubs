from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.resources.types.payments_account import PaymentsAccount

_M = TypeVar("_M")

class ListPaymentsAccountsRequest(proto.Message):
    customer_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...
    ) -> None: ...

class ListPaymentsAccountsResponse(proto.Message):
    payments_accounts: MutableSequence[PaymentsAccount]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        payments_accounts: MutableSequence[PaymentsAccount] = ...
    ) -> None: ...
