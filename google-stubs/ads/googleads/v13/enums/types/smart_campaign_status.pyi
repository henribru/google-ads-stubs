from typing import Any

import proto

class SmartCampaignStatusEnum(proto.Message):
    class SmartCampaignStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PAUSED = 2
        NOT_ELIGIBLE = 3
        PENDING = 4
        ELIGIBLE = 5
        REMOVED = 6
        ENDED = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
