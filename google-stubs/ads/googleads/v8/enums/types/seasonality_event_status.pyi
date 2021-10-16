from typing import Any

import proto

__protobuf__: Any

class SeasonalityEventStatusEnum(proto.Message):
    class SeasonalityEventStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
