from typing import Any

import proto

__protobuf__: Any

class LocationSourceTypeEnum(proto.Message):
    class LocationSourceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        GOOGLE_MY_BUSINESS: int
        AFFILIATE: int
