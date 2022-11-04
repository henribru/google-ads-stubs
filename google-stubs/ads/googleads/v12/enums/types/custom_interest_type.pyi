from typing import Any

import proto

class CustomInterestTypeEnum(proto.Message):
    class CustomInterestType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CUSTOM_AFFINITY = 2
        CUSTOM_INTENT = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
