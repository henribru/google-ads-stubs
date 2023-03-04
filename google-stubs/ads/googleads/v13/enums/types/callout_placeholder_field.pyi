from typing import Any

import proto

class CalloutPlaceholderFieldEnum(proto.Message):
    class CalloutPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CALLOUT_TEXT = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
