from typing import Any

import proto

__protobuf__: Any

class BidModifierSourceEnum(proto.Message):
    class BidModifierSource(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN: int
        AD_GROUP: int
