from typing import Any

import proto

class TargetImpressionShareLocationEnum(proto.Message):
    class TargetImpressionShareLocation(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ANYWHERE_ON_PAGE = 2
        TOP_OF_PAGE = 3
        ABSOLUTE_TOP_OF_PAGE = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
