from typing import Any

import proto

class AndroidPrivacyNetworkTypeEnum(proto.Message):
    class AndroidPrivacyNetworkType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEARCH = 2
        DISPLAY = 3
        YOUTUBE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
