from typing import Any

import proto

__protobuf__: Any

class CampaignExperimentStatusEnum(proto.Message):
    class CampaignExperimentStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INITIALIZING: int
        INITIALIZATION_FAILED: int
        ENABLED: int
        GRADUATED: int
        REMOVED: int
        PROMOTING: int
        PROMOTION_FAILED: int
        PROMOTED: int
        ENDED_MANUALLY: int
