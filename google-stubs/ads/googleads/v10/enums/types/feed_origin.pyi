from typing import Any

import proto

class FeedOriginEnum(proto.Message):
    class FeedOrigin(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        USER = 2
        GOOGLE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
