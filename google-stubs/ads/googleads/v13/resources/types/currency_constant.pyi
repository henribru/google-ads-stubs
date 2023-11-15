from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CurrencyConstant(proto.Message):
    resource_name: str
    code: str
    name: str
    symbol: str
    billable_unit_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        code: str = ...,
        name: str = ...,
        symbol: str = ...,
        billable_unit_micros: int = ...
    ) -> None: ...
