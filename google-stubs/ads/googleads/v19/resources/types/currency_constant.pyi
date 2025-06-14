import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CurrencyConstant(proto.Message):
    resource_name: str
    code: str
    name: str
    symbol: str
    billable_unit_micros: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., code: str = ..., name: str = ..., symbol: str = ..., billable_unit_micros: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "code", "name", "symbol", "billable_unit_micros"]) -> bool: ...
