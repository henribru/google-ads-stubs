from typing import Any

import proto

__protobuf__: Any

class LanguageCodeErrorEnum(proto.Message):
    class LanguageCodeError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LANGUAGE_CODE_NOT_FOUND: int
        INVALID_LANGUAGE_CODE: int
