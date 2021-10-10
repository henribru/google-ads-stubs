from typing import Any

import proto

__protobuf__: Any

class InteractionEventTypeEnum(proto.Message):
    class InteractionEventType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CLICK: int
        ENGAGEMENT: int
        VIDEO_VIEW: int
        NONE: int
