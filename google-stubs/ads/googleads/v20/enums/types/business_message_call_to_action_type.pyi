import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BusinessMessageCallToActionTypeEnum(proto.Message):
    class BusinessMessageCallToActionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPLY_NOW = 2
        BOOK_NOW = 3
        CONTACT_US = 4
        GET_INFO = 5
        GET_OFFER = 6
        GET_QUOTE = 7
        GET_STARTED = 8
        LEARN_MORE = 9
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
