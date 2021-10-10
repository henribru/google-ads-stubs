from typing import Any

import proto

__protobuf__: Any

class YoutubeVideoRegistrationErrorEnum(proto.Message):
    class YoutubeVideoRegistrationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        VIDEO_NOT_FOUND: int
        VIDEO_NOT_ACCESSIBLE: int
        VIDEO_NOT_ELIGIBLE: int
