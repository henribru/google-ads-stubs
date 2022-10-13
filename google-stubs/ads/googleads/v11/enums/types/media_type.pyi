from typing import Any

import proto

class MediaTypeEnum(proto.Message):
    class MediaType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IMAGE = 2
        ICON = 3
        MEDIA_BUNDLE = 4
        AUDIO = 5
        VIDEO = 6
        DYNAMIC_IMAGE = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
