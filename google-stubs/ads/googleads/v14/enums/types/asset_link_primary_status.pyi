from typing import Any

import proto

class AssetLinkPrimaryStatusEnum(proto.Message):
    class AssetLinkPrimaryStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ELIGIBLE = 2
        PAUSED = 3
        REMOVED = 4
        PENDING = 5
        LIMITED = 6
        NOT_ELIGIBLE = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
