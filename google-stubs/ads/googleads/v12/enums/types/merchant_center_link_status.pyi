from typing import Any

import proto

class MerchantCenterLinkStatusEnum(proto.Message):
    class MerchantCenterLinkStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        PENDING = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
