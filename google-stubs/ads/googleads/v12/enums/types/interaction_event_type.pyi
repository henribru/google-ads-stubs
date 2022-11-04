from typing import Any

import proto

class InteractionEventTypeEnum(proto.Message):
    class InteractionEventType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICK = 2
        ENGAGEMENT = 3
        VIDEO_VIEW = 4
        NONE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
