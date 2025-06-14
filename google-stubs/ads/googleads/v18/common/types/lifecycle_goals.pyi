import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LifecycleGoalValueSettings(proto.Message):
    value: float
    high_lifetime_value: float
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., value: float = ..., high_lifetime_value: float = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["value", "high_lifetime_value"]) -> bool: ...
