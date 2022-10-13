from typing import Any

import proto

class ContextErrorEnum(proto.Message):
    class ContextError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPERATION_NOT_PERMITTED_FOR_CONTEXT = 2
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
