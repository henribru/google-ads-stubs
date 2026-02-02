from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdSubNetworkTypeEnum(proto.Message):
    class AdSubNetworkType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNSEGMENTED = 2
        YOUTUBE_INSTREAM = 3
        YOUTUBE_INFEED = 4
        YOUTUBE_SHORTS = 5

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
