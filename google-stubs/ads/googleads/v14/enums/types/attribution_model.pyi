from typing import Any

import proto

class AttributionModelEnum(proto.Message):
    class AttributionModel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        EXTERNAL = 100
        GOOGLE_ADS_LAST_CLICK = 101
        GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK = 102
        GOOGLE_SEARCH_ATTRIBUTION_LINEAR = 103
        GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY = 104
        GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED = 105
        GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN = 106
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
