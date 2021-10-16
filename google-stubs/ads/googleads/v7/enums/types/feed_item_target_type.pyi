from typing import Any

import proto

__protobuf__: Any

class FeedItemTargetTypeEnum(proto.Message):
    class FeedItemTargetType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN: int
        AD_GROUP: int
        CRITERION: int
