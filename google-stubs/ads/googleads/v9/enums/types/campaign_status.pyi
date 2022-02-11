from typing import Any

import proto

__protobuf__: Any

class CampaignStatusEnum(proto.Message):
    class CampaignStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PAUSED: int
        REMOVED: int
