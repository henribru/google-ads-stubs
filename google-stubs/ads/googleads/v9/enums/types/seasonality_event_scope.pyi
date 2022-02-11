from typing import Any

import proto

__protobuf__: Any

class SeasonalityEventScopeEnum(proto.Message):
    class SeasonalityEventScope(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER: int
        CAMPAIGN: int
        CHANNEL: int
