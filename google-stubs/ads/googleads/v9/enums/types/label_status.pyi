from typing import Any

import proto

__protobuf__: Any

class LabelStatusEnum(proto.Message):
    class LabelStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
