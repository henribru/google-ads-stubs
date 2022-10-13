from typing import Any

import proto

class CriterionCategoryChannelAvailabilityModeEnum(proto.Message):
    class CriterionCategoryChannelAvailabilityMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_CHANNELS = 2
        CHANNEL_TYPE_AND_ALL_SUBTYPES = 3
        CHANNEL_TYPE_AND_SUBSET_SUBTYPES = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
