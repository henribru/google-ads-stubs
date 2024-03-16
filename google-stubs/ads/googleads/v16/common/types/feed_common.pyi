from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class Money(proto.Message):
    currency_code: str
    amount_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        currency_code: str = ...,
        amount_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["currency_code", "amount_micros"]
    ) -> bool: ...
