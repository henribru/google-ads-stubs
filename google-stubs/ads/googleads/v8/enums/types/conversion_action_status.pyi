from typing import Any

import proto

__protobuf__: Any

class ConversionActionStatusEnum(proto.Message):
    class ConversionActionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
        HIDDEN: int
