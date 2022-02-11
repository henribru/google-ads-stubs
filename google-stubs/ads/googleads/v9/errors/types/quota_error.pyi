from typing import Any

import proto

__protobuf__: Any

class QuotaErrorEnum(proto.Message):
    class QuotaError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        RESOURCE_EXHAUSTED: int
        ACCESS_PROHIBITED: int
        RESOURCE_TEMPORARILY_EXHAUSTED: int
