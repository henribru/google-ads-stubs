from typing import Any

import proto

class FrequencyCapLevelEnum(proto.Message):
    class FrequencyCapLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_AD = 2
        AD_GROUP = 3
        CAMPAIGN = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
