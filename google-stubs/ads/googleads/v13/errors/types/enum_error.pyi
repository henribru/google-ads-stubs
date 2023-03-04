from typing import Any

import proto

class EnumErrorEnum(proto.Message):
    class EnumError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENUM_VALUE_NOT_PERMITTED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
