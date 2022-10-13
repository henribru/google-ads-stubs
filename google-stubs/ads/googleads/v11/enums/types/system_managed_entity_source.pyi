from typing import Any

import proto

class SystemManagedResourceSourceEnum(proto.Message):
    class SystemManagedResourceSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_VARIATIONS = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
