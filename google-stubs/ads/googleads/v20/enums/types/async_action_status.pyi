import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AsyncActionStatusEnum(proto.Message):
    class AsyncActionStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NOT_STARTED = 2
        IN_PROGRESS = 3
        COMPLETED = 4
        FAILED = 5
        COMPLETED_WITH_WARNING = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
