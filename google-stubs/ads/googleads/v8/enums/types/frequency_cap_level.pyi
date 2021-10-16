from typing import Any

import proto

__protobuf__: Any

class FrequencyCapLevelEnum(proto.Message):
    class FrequencyCapLevel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP_AD: int
        AD_GROUP: int
        CAMPAIGN: int
