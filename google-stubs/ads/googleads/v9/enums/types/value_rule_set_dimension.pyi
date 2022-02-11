from typing import Any

import proto

__protobuf__: Any

class ValueRuleSetDimensionEnum(proto.Message):
    class ValueRuleSetDimension(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        GEO_LOCATION: int
        DEVICE: int
        AUDIENCE: int
