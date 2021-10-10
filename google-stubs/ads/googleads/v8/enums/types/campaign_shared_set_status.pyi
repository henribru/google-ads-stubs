from typing import Any

import proto

__protobuf__: Any

class CampaignSharedSetStatusEnum(proto.Message):
    class CampaignSharedSetStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
