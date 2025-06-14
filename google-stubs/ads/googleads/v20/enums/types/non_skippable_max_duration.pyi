import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class NonSkippableMaxDurationEnum(proto.Message):
    class NonSkippableMaxDuration(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MAX_DURATION_FIFTEEN_SECONDS = 2
        MAX_DURATION_THIRTY_SECONDS = 3
        MAX_DURATION_SIXTY_SECONDS = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
