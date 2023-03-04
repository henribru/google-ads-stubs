from typing import Any

import proto

class ResponseContentTypeEnum(proto.Message):
    class ResponseContentType(proto.Enum):
        UNSPECIFIED = 0
        RESOURCE_NAME_ONLY = 1
        MUTABLE_RESOURCE = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
