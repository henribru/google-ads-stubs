from typing import Any

import proto

class PositiveGeoTargetTypeEnum(proto.Message):
    class PositiveGeoTargetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PRESENCE_OR_INTEREST = 5
        SEARCH_INTEREST = 6
        PRESENCE = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
