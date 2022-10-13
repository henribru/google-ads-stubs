from typing import Any

import proto

class ValueRuleGeoLocationMatchTypeEnum(proto.Message):
    class ValueRuleGeoLocationMatchType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ANY = 2
        LOCATION_OF_PRESENCE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
