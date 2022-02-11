from typing import Any

import proto

__protobuf__: Any

class HotelRateTypeEnum(proto.Message):
    class HotelRateType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        UNAVAILABLE: int
        PUBLIC_RATE: int
        QUALIFIED_RATE: int
        PRIVATE_RATE: int
