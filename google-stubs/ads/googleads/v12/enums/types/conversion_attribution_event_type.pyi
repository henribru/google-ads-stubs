from typing import Any

import proto

class ConversionAttributionEventTypeEnum(proto.Message):
    class ConversionAttributionEventType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        IMPRESSION = 2
        INTERACTION = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
