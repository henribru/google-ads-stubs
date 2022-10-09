import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class InteractionEventTypeEnum(proto.Message):
    class InteractionEventType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CLICK: int
        ENGAGEMENT: int
        VIDEO_VIEW: int
        NONE: int
