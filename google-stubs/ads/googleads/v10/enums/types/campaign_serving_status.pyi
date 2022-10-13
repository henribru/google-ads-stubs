from typing import Any

import proto

class CampaignServingStatusEnum(proto.Message):
    class CampaignServingStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SERVING = 2
        NONE = 3
        ENDED = 4
        PENDING = 5
        SUSPENDED = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
