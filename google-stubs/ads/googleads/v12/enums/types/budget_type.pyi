from typing import Any

import proto

class BudgetTypeEnum(proto.Message):
    class BudgetType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STANDARD = 2
        FIXED_CPA = 4
        SMART_CAMPAIGN = 5
        LOCAL_SERVICES = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
