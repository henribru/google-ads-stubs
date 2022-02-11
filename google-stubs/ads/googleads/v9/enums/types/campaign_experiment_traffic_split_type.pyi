from typing import Any

import proto

__protobuf__: Any

class CampaignExperimentTrafficSplitTypeEnum(proto.Message):
    class CampaignExperimentTrafficSplitType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        RANDOM_QUERY: int
        COOKIE: int
