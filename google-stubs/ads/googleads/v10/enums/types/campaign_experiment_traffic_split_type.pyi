from typing import Any

import proto

class CampaignExperimentTrafficSplitTypeEnum(proto.Message):
    class CampaignExperimentTrafficSplitType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RANDOM_QUERY = 2
        COOKIE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
