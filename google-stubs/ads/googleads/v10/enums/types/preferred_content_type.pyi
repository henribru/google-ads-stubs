from typing import Any

import proto

class PreferredContentTypeEnum(proto.Message):
    class PreferredContentType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        YOUTUBE_TOP_CONTENT = 400
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
