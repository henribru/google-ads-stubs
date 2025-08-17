import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class VideoAdSequenceInteractionTypeEnum(proto.Message):
    class VideoAdSequenceInteractionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAID_VIEW = 2
        SKIP = 3
        IMPRESSION = 4
        ENGAGED_IMPRESSION = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
