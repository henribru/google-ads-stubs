from typing import Any

import proto

class KeywordPlanAggregateMetricTypeEnum(proto.Message):
    class KeywordPlanAggregateMetricType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DEVICE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
