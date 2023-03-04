from typing import Any

import proto

class LanguageCodeErrorEnum(proto.Message):
    class LanguageCodeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LANGUAGE_CODE_NOT_FOUND = 2
        INVALID_LANGUAGE_CODE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
