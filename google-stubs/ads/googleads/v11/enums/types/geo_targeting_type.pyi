from typing import Any

import proto

class GeoTargetingTypeEnum(proto.Message):
    class GeoTargetingType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AREA_OF_INTEREST = 2
        LOCATION_OF_PRESENCE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
