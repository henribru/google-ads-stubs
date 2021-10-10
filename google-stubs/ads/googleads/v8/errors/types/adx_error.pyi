from typing import Any

import proto

__protobuf__: Any

class AdxErrorEnum(proto.Message):
    class AdxError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        UNSUPPORTED_FEATURE: int
