from typing import Any

import proto

class FieldMaskErrorEnum(proto.Message):
    class FieldMaskError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        FIELD_MASK_MISSING = 5
        FIELD_MASK_NOT_ALLOWED = 4
        FIELD_NOT_FOUND = 2
        FIELD_HAS_SUBFIELDS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
