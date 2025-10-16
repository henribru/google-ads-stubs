import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdFormatTypeEnum(proto.Message):
    class AdFormatType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OTHER = 2
        UNSEGMENTED = 3
        INSTREAM_SKIPPABLE = 4
        INSTREAM_NON_SKIPPABLE = 5
        INFEED = 6
        BUMPER = 7
        OUTSTREAM = 8
        MASTHEAD = 9
        AUDIO = 10
        SHORTS = 11
        PAUSE = 12
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
