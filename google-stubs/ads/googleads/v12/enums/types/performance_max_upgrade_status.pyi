from typing import Any

import proto

class PerformanceMaxUpgradeStatusEnum(proto.Message):
    class PerformanceMaxUpgradeStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UPGRADE_ELIBIGLE = 2
        UPGRADE_IN_PROGRESS = 3
        UPGRADE_COMPLETE = 4
        UPGRADE_FAILED = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
