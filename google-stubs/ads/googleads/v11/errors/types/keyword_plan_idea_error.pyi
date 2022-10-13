from typing import Any

import proto

class KeywordPlanIdeaErrorEnum(proto.Message):
    class KeywordPlanIdeaError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        URL_CRAWL_ERROR = 2
        INVALID_VALUE = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
