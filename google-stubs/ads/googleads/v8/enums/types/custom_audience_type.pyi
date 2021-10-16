from typing import Any

import proto

__protobuf__: Any

class CustomAudienceTypeEnum(proto.Message):
    class CustomAudienceType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AUTO: int
        INTEREST: int
        PURCHASE_INTENT: int
        SEARCH: int
