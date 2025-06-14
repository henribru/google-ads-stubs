import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class HeaderErrorEnum(proto.Message):
    class HeaderError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_LOGIN_CUSTOMER_ID = 3
        INVALID_LINKED_CUSTOMER_ID = 7
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
