from typing import Any

import proto

class AssetSetErrorEnum(proto.Message):
    class AssetSetError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_ASSET_SET_NAME = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
