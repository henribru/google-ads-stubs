from typing import Any

import proto

class KeywordPlanNetworkEnum(proto.Message):
    class KeywordPlanNetwork(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        GOOGLE_SEARCH = 2
        GOOGLE_SEARCH_AND_PARTNERS = 3
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
