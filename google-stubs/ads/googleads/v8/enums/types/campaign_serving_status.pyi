from typing import Any

import proto

__protobuf__: Any

class CampaignServingStatusEnum(proto.Message):
    class CampaignServingStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SERVING: int
        NONE: int
        ENDED: int
        PENDING: int
        SUSPENDED: int
