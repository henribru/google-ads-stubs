from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class AdvertisingChannelTypeEnum(proto.Message):
    class AdvertisingChannelType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH = 2
        DISPLAY = 3
        SHOPPING = 4
        HOTEL = 5
        VIDEO = 6
        MULTI_CHANNEL = 7
        LOCAL = 8
        SMART = 9
        PERFORMANCE_MAX = 10
        LOCAL_SERVICES = 11
        DISCOVERY = 12
        TRAVEL = 13

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
