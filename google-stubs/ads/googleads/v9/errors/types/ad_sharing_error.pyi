from typing import Any

import proto

__protobuf__: Any

class AdSharingErrorEnum(proto.Message):
    class AdSharingError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        AD_GROUP_ALREADY_CONTAINS_AD: int
        INCOMPATIBLE_AD_UNDER_AD_GROUP: int
        CANNOT_SHARE_INACTIVE_AD: int
