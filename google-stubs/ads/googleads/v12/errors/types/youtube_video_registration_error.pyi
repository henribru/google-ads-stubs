from typing import Any

import proto

class YoutubeVideoRegistrationErrorEnum(proto.Message):
    class YoutubeVideoRegistrationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        VIDEO_NOT_FOUND = 2
        VIDEO_NOT_ACCESSIBLE = 3
        VIDEO_NOT_ELIGIBLE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
