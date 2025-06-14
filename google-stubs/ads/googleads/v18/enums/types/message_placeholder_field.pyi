import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class MessagePlaceholderFieldEnum(proto.Message):
    class MessagePlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME = 2
        COUNTRY_CODE = 3
        PHONE_NUMBER = 4
        MESSAGE_EXTENSION_TEXT = 5
        MESSAGE_TEXT = 6
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
