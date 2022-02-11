from typing import Any

import proto

__protobuf__: Any

class CustomInterestStatusEnum(proto.Message):
    class CustomInterestStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
