from typing import Any

import proto

class ProximityRadiusUnitsEnum(proto.Message):
    class ProximityRadiusUnits(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        MILES = 2
        KILOMETERS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
