from typing import Any

import proto

class SharedCriterionErrorEnum(proto.Message):
    class SharedCriterionError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CRITERION_TYPE_NOT_ALLOWED_FOR_SHARED_SET_TYPE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
