from typing import Any

import proto

__protobuf__: Any

class ProductChannelExclusivityEnum(proto.Message):
    class ProductChannelExclusivity(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SINGLE_CHANNEL: int
        MULTI_CHANNEL: int
