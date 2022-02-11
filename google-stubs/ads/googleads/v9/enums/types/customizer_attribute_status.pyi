from typing import Any

import proto

__protobuf__: Any

class CustomizerAttributeStatusEnum(proto.Message):
    class CustomizerAttributeStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
