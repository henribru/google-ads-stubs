from typing import Any

import proto

__protobuf__: Any

class NegativeGeoTargetTypeEnum(proto.Message):
    class NegativeGeoTargetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PRESENCE_OR_INTEREST: int
        PRESENCE: int
