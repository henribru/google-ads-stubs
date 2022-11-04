from typing import Any

import proto

class OperatorErrorEnum(proto.Message):
    class OperatorError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OPERATOR_NOT_SUPPORTED = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
