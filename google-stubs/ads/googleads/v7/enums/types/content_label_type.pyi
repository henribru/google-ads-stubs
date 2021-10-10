from typing import Any

import proto

__protobuf__: Any

class ContentLabelTypeEnum(proto.Message):
    class ContentLabelType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEXUALLY_SUGGESTIVE: int
        BELOW_THE_FOLD: int
        PARKED_DOMAIN: int
        JUVENILE: int
        PROFANITY: int
        TRAGEDY: int
        VIDEO: int
        VIDEO_RATING_DV_G: int
        VIDEO_RATING_DV_PG: int
        VIDEO_RATING_DV_T: int
        VIDEO_RATING_DV_MA: int
        VIDEO_NOT_YET_RATED: int
        EMBEDDED_VIDEO: int
        LIVE_STREAMING_VIDEO: int
        SOCIAL_ISSUES: int
