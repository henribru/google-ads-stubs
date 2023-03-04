from typing import Any

import proto

class SearchTermTargetingStatusEnum(proto.Message):
    class SearchTermTargetingStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADDED = 2
        EXCLUDED = 3
        ADDED_EXCLUDED = 4
        NONE = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
