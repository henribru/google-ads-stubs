from typing import Any

import proto

class NewResourceCreationErrorEnum(proto.Message):
    class NewResourceCreationError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_SET_ID_FOR_CREATE = 2
        DUPLICATE_TEMP_IDS = 3
        TEMP_ID_RESOURCE_HAD_ERRORS = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
