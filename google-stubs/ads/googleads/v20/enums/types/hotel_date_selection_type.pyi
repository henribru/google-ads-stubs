import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class HotelDateSelectionTypeEnum(proto.Message):
    class HotelDateSelectionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEFAULT_SELECTION = 50
        USER_SELECTED = 51
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
