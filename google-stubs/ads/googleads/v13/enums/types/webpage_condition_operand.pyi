from typing import Any

import proto

class WebpageConditionOperandEnum(proto.Message):
    class WebpageConditionOperand(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        URL = 2
        CATEGORY = 3
        PAGE_TITLE = 4
        PAGE_CONTENT = 5
        CUSTOM_LABEL = 6
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
