import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class PaymentsAccount(proto.Message):
    resource_name: str
    payments_account_id: str
    name: str
    currency_code: str
    payments_profile_id: str
    secondary_payments_profile_id: str
    paying_manager_customer: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., payments_account_id: str = ..., name: str = ..., currency_code: str = ..., payments_profile_id: str = ..., secondary_payments_profile_id: str = ..., paying_manager_customer: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "payments_account_id", "name", "currency_code", "payments_profile_id", "secondary_payments_profile_id", "paying_manager_customer"]) -> bool: ...
