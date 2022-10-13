from typing import Any

import proto

class FeedItemTargetTypeEnum(proto.Message):
    class FeedItemTargetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN = 2
        AD_GROUP = 3
        CRITERION = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
