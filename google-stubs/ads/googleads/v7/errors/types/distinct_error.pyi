from typing import Any

import proto

__protobuf__: Any

class DistinctErrorEnum(proto.Message):
    class DistinctError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DUPLICATE_ELEMENT: int
        DUPLICATE_TYPE: int
