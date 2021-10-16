from typing import Any

import proto

__protobuf__: Any

class ProductChannelEnum(proto.Message):
    class ProductChannel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ONLINE: int
        LOCAL: int
