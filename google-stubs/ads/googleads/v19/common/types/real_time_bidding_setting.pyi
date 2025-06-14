import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class RealTimeBiddingSetting(proto.Message):
    opt_in: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., opt_in: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["opt_in"]) -> bool: ...
