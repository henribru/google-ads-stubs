from typing import Any

import proto

class FrequencyCapEventTypeEnum(proto.Message):
    class FrequencyCapEventType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IMPRESSION = 2
        VIDEO_VIEW = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
