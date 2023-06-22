from typing import Any

import proto

class FeedMappingCriterionTypeEnum(proto.Message):
    class FeedMappingCriterionType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOCATION_EXTENSION_TARGETING = 4
        DSA_PAGE_FEED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
