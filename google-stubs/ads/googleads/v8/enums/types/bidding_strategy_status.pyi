from typing import Any

import proto

__protobuf__: Any

class BiddingStrategyStatusEnum(proto.Message):
    class BiddingStrategyStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
