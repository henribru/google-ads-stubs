from typing import Any

import proto

class AssetGroupPrimaryStatusEnum(proto.Message):
    class AssetGroupPrimaryStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ELIGIBLE = 2
        PAUSED = 3
        REMOVED = 4
        NOT_ELIGIBLE = 5
        LIMITED = 6
        PENDING = 7
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
