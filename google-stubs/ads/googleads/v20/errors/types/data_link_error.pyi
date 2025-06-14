import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class DataLinkErrorEnum(proto.Message):
    class DataLinkError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        YOUTUBE_CHANNEL_ID_INVALID: int
        YOUTUBE_VIDEO_ID_INVALID: int
        YOUTUBE_VIDEO_FROM_DIFFERENT_CHANNEL: int
        PERMISSION_DENIED: int
        INVALID_STATUS: int
        INVALID_UPDATE_STATUS: int
        INVALID_RESOURCE_NAME: int
