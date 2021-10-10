from typing import Any

import proto

__protobuf__: Any

class SearchEngineResultsPageTypeEnum(proto.Message):
    class SearchEngineResultsPageType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADS_ONLY: int
        ORGANIC_ONLY: int
        ADS_AND_ORGANIC: int
