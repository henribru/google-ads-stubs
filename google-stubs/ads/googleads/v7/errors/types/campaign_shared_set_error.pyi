from typing import Any

import proto

__protobuf__: Any

class CampaignSharedSetErrorEnum(proto.Message):
    class CampaignSharedSetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SHARED_SET_ACCESS_DENIED: int
