from typing import Any

import proto

__protobuf__: Any

class KeywordPlanCampaignErrorEnum(proto.Message):
    class KeywordPlanCampaignError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_NAME: int
        INVALID_LANGUAGES: int
        INVALID_GEOS: int
        DUPLICATE_NAME: int
        MAX_GEOS_EXCEEDED: int
        MAX_LANGUAGES_EXCEEDED: int
