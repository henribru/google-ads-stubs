from typing import Any

import proto

__protobuf__: Any

class DataDrivenModelStatusEnum(proto.Message):
    class DataDrivenModelStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AVAILABLE: int
        STALE: int
        EXPIRED: int
        NEVER_GENERATED: int
