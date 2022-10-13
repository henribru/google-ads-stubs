from typing import Any

import proto

class KeywordPlanCampaignErrorEnum(proto.Message):
    class KeywordPlanCampaignError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_NAME = 2
        INVALID_LANGUAGES = 3
        INVALID_GEOS = 4
        DUPLICATE_NAME = 5
        MAX_GEOS_EXCEEDED = 6
        MAX_LANGUAGES_EXCEEDED = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
