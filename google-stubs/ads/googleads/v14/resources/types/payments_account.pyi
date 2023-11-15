from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class PaymentsAccount(proto.Message):
    resource_name: str
    payments_account_id: str
    name: str
    currency_code: str
    payments_profile_id: str
    secondary_payments_profile_id: str
    paying_manager_customer: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        payments_account_id: str = ...,
        name: str = ...,
        currency_code: str = ...,
        payments_profile_id: str = ...,
        secondary_payments_profile_id: str = ...,
        paying_manager_customer: str = ...
    ) -> None: ...
