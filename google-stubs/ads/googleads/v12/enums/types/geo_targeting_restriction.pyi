from typing import Any

import proto

class GeoTargetingRestrictionEnum(proto.Message):
    class GeoTargetingRestriction(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_OF_PRESENCE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
