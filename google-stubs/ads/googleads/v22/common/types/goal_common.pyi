import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerLifecycleOptimizationValueSettings(proto.Message):
    additional_value: float
    additional_high_lifetime_value: float
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, additional_value: float = ..., additional_high_lifetime_value: float = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["additional_value", "additional_high_lifetime_value"]) -> bool: ...
