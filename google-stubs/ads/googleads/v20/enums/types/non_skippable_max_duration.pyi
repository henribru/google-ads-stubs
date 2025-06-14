import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class NonSkippableMaxDurationEnum(proto.Message):
    class NonSkippableMaxDuration(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        MAX_DURATION_FIFTEEN_SECONDS: int
        MAX_DURATION_THIRTY_SECONDS: int
        MAX_DURATION_SIXTY_SECONDS: int
