import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ReachPlanSurfaceEnum(proto.Message):
    class ReachPlanSurface(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DISCOVER_FEED: int
        GMAIL: int
        IN_FEED: int
        IN_STREAM_BUMPER: int
        IN_STREAM_NON_SKIPPABLE: int
        IN_STREAM_SKIPPABLE: int
        SHORTS: int
