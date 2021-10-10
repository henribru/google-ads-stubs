from typing import Any

import proto

__protobuf__: Any

class AdServingOptimizationStatusEnum(proto.Message):
    class AdServingOptimizationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        OPTIMIZE: int
        CONVERSION_OPTIMIZE: int
        ROTATE: int
        ROTATE_INDEFINITELY: int
        UNAVAILABLE: int
