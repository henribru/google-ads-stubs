from typing import Any

import proto

class CampaignSharedSetErrorEnum(proto.Message):
    class CampaignSharedSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SHARED_SET_ACCESS_DENIED = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
