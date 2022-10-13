from typing import Any

import proto

class BudgetDeliveryMethodEnum(proto.Message):
    class BudgetDeliveryMethod(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        STANDARD = 2
        ACCELERATED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
