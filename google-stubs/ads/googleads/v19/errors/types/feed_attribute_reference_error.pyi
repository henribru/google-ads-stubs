import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class FeedAttributeReferenceErrorEnum(proto.Message):
    class FeedAttributeReferenceError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_REFERENCE_REMOVED_FEED = 2
        INVALID_FEED_NAME = 3
        INVALID_FEED_ATTRIBUTE_NAME = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
