from typing import Any

import proto

__protobuf__: Any

class HotelPriceBucketEnum(proto.Message):
    class HotelPriceBucket(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LOWEST_UNIQUE: int
        LOWEST_TIED: int
        NOT_LOWEST: int
        ONLY_PARTNER_SHOWN: int
