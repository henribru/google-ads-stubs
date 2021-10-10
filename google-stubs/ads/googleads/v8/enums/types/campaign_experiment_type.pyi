from typing import Any

import proto

__protobuf__: Any

class CampaignExperimentTypeEnum(proto.Message):
    class CampaignExperimentType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BASE: int
        DRAFT: int
        EXPERIMENT: int
