from typing import Any

import proto

class AssetSourceEnum(proto.Message):
    class AssetSource(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADVERTISER = 2
        AUTOMATICALLY_CREATED = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
