from typing import Any

import proto

__protobuf__: Any

class MerchantCenterLinkStatusEnum(proto.Message):
    class MerchantCenterLinkStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        PENDING: int
