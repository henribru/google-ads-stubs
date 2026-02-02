import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BusinessMessageProviderEnum(proto.Message):
    class BusinessMessageProvider(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WHATSAPP = 2
        FACEBOOK_MESSENGER = 3
        ZALO = 4
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
