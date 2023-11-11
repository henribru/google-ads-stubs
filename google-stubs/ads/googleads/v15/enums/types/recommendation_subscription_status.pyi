from typing import Any

import proto

class RecommendationSubscriptionStatusEnum(proto.Message):
    class RecommendationSubscriptionStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ENABLED = 2
        PAUSED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
