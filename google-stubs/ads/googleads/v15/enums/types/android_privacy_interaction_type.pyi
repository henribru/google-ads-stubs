from typing import Any

import proto

class AndroidPrivacyInteractionTypeEnum(proto.Message):
    class AndroidPrivacyInteractionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CLICK = 2
        ENGAGED_VIEW = 3
        VIEW = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
