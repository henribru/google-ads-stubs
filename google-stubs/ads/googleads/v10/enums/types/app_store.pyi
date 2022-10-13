from typing import Any

import proto

class AppStoreEnum(proto.Message):
    class AppStore(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        APPLE_ITUNES = 2
        GOOGLE_PLAY = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
