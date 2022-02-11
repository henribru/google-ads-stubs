from typing import Any

import proto

__protobuf__: Any

class PositiveGeoTargetTypeEnum(proto.Message):
    class PositiveGeoTargetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PRESENCE_OR_INTEREST: int
        SEARCH_INTEREST: int
        PRESENCE: int
