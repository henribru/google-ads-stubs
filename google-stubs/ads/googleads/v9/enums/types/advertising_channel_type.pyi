from typing import Any

import proto

__protobuf__: Any

class AdvertisingChannelTypeEnum(proto.Message):
    class AdvertisingChannelType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEARCH: int
        DISPLAY: int
        SHOPPING: int
        HOTEL: int
        VIDEO: int
        MULTI_CHANNEL: int
        LOCAL: int
        SMART: int
        PERFORMANCE_MAX: int
