from typing import Any

import proto

class AdCustomizerPlaceholderFieldEnum(proto.Message):
    class AdCustomizerPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INTEGER = 2
        PRICE = 3
        DATE = 4
        STRING = 5
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
