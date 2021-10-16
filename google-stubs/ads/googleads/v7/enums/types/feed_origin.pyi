from typing import Any

import proto

__protobuf__: Any

class FeedOriginEnum(proto.Message):
    class FeedOrigin(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        USER: int
        GOOGLE: int
