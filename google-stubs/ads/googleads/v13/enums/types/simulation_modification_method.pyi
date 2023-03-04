from typing import Any

import proto

class SimulationModificationMethodEnum(proto.Message):
    class SimulationModificationMethod(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UNIFORM = 2
        DEFAULT = 3
        SCALING = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
