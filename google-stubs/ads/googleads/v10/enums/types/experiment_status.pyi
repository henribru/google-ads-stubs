from typing import Any

import proto

class ExperimentStatusEnum(proto.Message):
    class ExperimentStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        REMOVED = 3
        HALTED = 4
        PROMOTED = 5
        SETUP = 6
        INITIATED = 7
        GRADUATED = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
