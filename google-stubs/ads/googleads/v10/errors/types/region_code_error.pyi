from typing import Any

import proto

class RegionCodeErrorEnum(proto.Message):
    class RegionCodeError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        INVALID_REGION_CODE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
