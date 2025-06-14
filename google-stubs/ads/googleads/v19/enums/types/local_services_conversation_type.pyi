import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LocalServicesLeadConversationTypeEnum(proto.Message):
    class ConversationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMAIL = 2
        MESSAGE = 3
        PHONE_CALL = 4
        SMS = 5
        BOOKING = 6
        WHATSAPP = 7
        ADS_API = 8
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
