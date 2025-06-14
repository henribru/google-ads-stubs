import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class YoutubeVideoRegistrationErrorEnum(proto.Message):
    class YoutubeVideoRegistrationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        VIDEO_NOT_FOUND: int
        VIDEO_NOT_ACCESSIBLE: int
        VIDEO_NOT_ELIGIBLE: int
