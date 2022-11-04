from typing import Any

import proto

class NotEmptyErrorEnum(proto.Message):
    class NotEmptyError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EMPTY_LIST = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
