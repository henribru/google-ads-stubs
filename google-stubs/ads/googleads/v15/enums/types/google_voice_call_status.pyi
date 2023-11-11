from typing import Any

import proto

class GoogleVoiceCallStatusEnum(proto.Message):
    class GoogleVoiceCallStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MISSED = 2
        RECEIVED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
