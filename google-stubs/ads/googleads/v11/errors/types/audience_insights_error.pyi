from typing import Any

import proto

class AudienceInsightsErrorEnum(proto.Message):
    class AudienceInsightsError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DIMENSION_INCOMPATIBLE_WITH_TOPIC_AUDIENCE_COMBINATIONS = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
