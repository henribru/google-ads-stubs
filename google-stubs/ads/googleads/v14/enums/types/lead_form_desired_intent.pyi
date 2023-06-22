from typing import Any

import proto

class LeadFormDesiredIntentEnum(proto.Message):
    class LeadFormDesiredIntent(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOW_INTENT = 2
        HIGH_INTENT = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
