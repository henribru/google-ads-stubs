from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
    def __contains__(self, key: Literal["resource_name", "code", "name", "symbol", "billable_unit_micros"]) -> bool: ...  # type: ignore[override]
