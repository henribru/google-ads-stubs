from typing import Any

import proto

class CampaignPrimaryStatusEnum(proto.Message):
    class CampaignPrimaryStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ELIGIBLE = 2
        PAUSED = 3
        REMOVED = 4
        ENDED = 5
        PENDING = 6
        MISCONFIGURED = 7
        LIMITED = 8
        LEARNING = 9
        NOT_ELIGIBLE = 10
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
