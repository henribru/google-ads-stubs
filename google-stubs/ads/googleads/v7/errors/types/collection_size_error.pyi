from typing import Any

import proto

__protobuf__: Any

class CollectionSizeErrorEnum(proto.Message):
    class CollectionSizeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        TOO_FEW: int
        TOO_MANY: int
