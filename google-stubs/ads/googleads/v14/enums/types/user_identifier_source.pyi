from typing import Any

import proto

class UserIdentifierSourceEnum(proto.Message):
    class UserIdentifierSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FIRST_PARTY = 2
        THIRD_PARTY = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
