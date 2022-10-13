from typing import Any

import proto

class AdParameterErrorEnum(proto.Message):
    class AdParameterError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AD_GROUP_CRITERION_MUST_BE_KEYWORD = 2
        INVALID_INSERTION_TEXT_FORMAT = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
