import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdSubNetworkTypeEnum(proto.Message):
    class AdSubNetworkType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNSEGMENTED = 2
        YOUTUBE_INSTREAM = 3
        YOUTUBE_INFEED = 4
        YOUTUBE_SHORTS = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
