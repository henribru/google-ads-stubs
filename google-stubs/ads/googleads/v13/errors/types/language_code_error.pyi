from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class LanguageCodeErrorEnum(proto.Message):
    class LanguageCodeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LANGUAGE_CODE_NOT_FOUND = 2
        INVALID_LANGUAGE_CODE = 3
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
