from typing import Any

import proto

class ReachPlanAdLengthEnum(proto.Message):
    class ReachPlanAdLength(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SIX_SECONDS = 2
        FIFTEEN_OR_TWENTY_SECONDS = 3
        TWENTY_SECONDS_OR_MORE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
