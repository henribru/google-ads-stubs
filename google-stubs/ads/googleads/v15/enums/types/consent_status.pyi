from typing import Any

import proto

class ConsentStatusEnum(proto.Message):
    class ConsentStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GRANTED = 2
        DENIED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
