from collections.abc import MutableSequence
from google.ads.googleads.v19.resources.types.payments_account import PaymentsAccount
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ListPaymentsAccountsRequest(proto.Message):
    customer_id: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id"]) -> bool: ...
class ListPaymentsAccountsResponse(proto.Message):
    payments_accounts: MutableSequence[PaymentsAccount]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, payments_accounts: MutableSequence[PaymentsAccount] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["payments_accounts"]) -> bool: ...
