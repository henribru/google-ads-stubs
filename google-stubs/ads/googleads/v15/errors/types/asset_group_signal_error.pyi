from typing import Any

import proto

class AssetGroupSignalErrorEnum(proto.Message):
    class AssetGroupSignalError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TOO_MANY_WORDS = 2
        SEARCH_THEME_POLICY_VIOLATION = 3
        AUDIENCE_WITH_WRONG_ASSET_GROUP_ID = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
