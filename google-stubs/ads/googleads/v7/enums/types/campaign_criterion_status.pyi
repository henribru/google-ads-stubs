from typing import Any

import proto

__protobuf__: Any

class CampaignCriterionStatusEnum(proto.Message):
    class CampaignCriterionStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
