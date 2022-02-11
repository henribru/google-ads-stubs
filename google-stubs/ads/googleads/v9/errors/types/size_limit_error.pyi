from typing import Any

import proto

__protobuf__: Any

class SizeLimitErrorEnum(proto.Message):
    class SizeLimitError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        REQUEST_SIZE_LIMIT_EXCEEDED: int
        RESPONSE_SIZE_LIMIT_EXCEEDED: int
