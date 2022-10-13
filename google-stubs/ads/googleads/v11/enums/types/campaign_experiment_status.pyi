from typing import Any

import proto

class CampaignExperimentStatusEnum(proto.Message):
    class CampaignExperimentStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INITIALIZING = 2
        INITIALIZATION_FAILED = 8
        ENABLED = 3
        GRADUATED = 4
        REMOVED = 5
        PROMOTING = 6
        PROMOTION_FAILED = 9
        PROMOTED = 7
        ENDED_MANUALLY = 10
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
