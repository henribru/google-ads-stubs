from typing import Any

import proto

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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
