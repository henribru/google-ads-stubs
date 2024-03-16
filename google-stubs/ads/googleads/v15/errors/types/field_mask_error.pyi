from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class FieldMaskErrorEnum(proto.Message):
    class FieldMaskError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FIELD_MASK_MISSING = 5
        FIELD_MASK_NOT_ALLOWED = 4
        FIELD_NOT_FOUND = 2
        FIELD_HAS_SUBFIELDS = 3

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
