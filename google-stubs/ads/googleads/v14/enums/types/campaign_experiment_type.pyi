from typing import Any

import proto

class CampaignExperimentTypeEnum(proto.Message):
    class CampaignExperimentType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BASE = 2
        DRAFT = 3
        EXPERIMENT = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
