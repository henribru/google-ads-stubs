from typing import Any

import proto

class BudgetPeriodEnum(proto.Message):
    class BudgetPeriod(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DAILY = 2
        CUSTOM_PERIOD = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
