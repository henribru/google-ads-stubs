import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class Money(proto.Message):
    currency_code: str
    amount_micros: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, currency_code: str = ..., amount_micros: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["currency_code", "amount_micros"]) -> bool: ...
