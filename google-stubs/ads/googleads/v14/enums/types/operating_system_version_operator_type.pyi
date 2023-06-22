from typing import Any

import proto

class OperatingSystemVersionOperatorTypeEnum(proto.Message):
    class OperatingSystemVersionOperatorType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EQUALS_TO = 2
        GREATER_THAN_EQUALS_TO = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
