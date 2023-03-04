from typing import Any

import proto

class CurrencyErrorEnum(proto.Message):
    class CurrencyError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        VALUE_NOT_MULTIPLE_OF_BILLABLE_UNIT = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
