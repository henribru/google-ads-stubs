from typing import Any

import proto

class SearchEngineResultsPageTypeEnum(proto.Message):
    class SearchEngineResultsPageType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ADS_ONLY = 2
        ORGANIC_ONLY = 3
        ADS_AND_ORGANIC = 4
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
