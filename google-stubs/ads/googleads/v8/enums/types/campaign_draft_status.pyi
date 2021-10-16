from typing import Any

import proto

__protobuf__: Any

class CampaignDraftStatusEnum(proto.Message):
    class CampaignDraftStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        PROPOSED: int
        REMOVED: int
        PROMOTING: int
        PROMOTED: int
        PROMOTE_FAILED: int
