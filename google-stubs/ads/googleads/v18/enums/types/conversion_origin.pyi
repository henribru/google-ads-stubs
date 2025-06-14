import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ConversionOriginEnum(proto.Message):
    class ConversionOrigin(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        WEBSITE = 2
        GOOGLE_HOSTED = 3
        APP = 4
        CALL_FROM_ADS = 5
        STORE = 6
        YOUTUBE_HOSTED = 7
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
