from typing import Any

import proto

class KeywordPlanCompetitionLevelEnum(proto.Message):
    class KeywordPlanCompetitionLevel(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        LOW = 2
        MEDIUM = 3
        HIGH = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
