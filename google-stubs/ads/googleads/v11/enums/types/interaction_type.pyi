from typing import Any

import proto

class InteractionTypeEnum(proto.Message):
    class InteractionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CALLS = 8000
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
