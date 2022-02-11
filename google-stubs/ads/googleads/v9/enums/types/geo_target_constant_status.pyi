from typing import Any

import proto

__protobuf__: Any

class GeoTargetConstantStatusEnum(proto.Message):
    class GeoTargetConstantStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVAL_PLANNED: int
