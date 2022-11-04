from typing import Any

import proto

class CustomizerAttributeErrorEnum(proto.Message):
    class CustomizerAttributeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_CUSTOMIZER_ATTRIBUTE_NAME = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...