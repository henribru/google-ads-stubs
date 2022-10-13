from typing import Any

import proto

class LocationGroupRadiusUnitsEnum(proto.Message):
    class LocationGroupRadiusUnits(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        METERS = 2
        MILES = 3
        MILLI_MILES = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
