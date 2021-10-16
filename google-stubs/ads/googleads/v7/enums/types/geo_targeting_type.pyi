from typing import Any

import proto

__protobuf__: Any

class GeoTargetingTypeEnum(proto.Message):
    class GeoTargetingType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AREA_OF_INTEREST: int
        LOCATION_OF_PRESENCE: int
