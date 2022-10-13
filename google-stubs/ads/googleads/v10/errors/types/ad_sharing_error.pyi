from typing import Any

import proto

class AdSharingErrorEnum(proto.Message):
    class AdSharingError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_ALREADY_CONTAINS_AD = 2
        INCOMPATIBLE_AD_UNDER_AD_GROUP = 3
        CANNOT_SHARE_INACTIVE_AD = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
