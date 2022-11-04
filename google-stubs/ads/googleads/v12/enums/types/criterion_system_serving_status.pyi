from typing import Any

import proto

class CriterionSystemServingStatusEnum(proto.Message):
    class CriterionSystemServingStatus(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ELIGIBLE = 2
        RARELY_SERVED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
