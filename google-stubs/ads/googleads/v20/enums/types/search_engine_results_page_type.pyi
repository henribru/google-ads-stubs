import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SearchEngineResultsPageTypeEnum(proto.Message):
    class SearchEngineResultsPageType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ADS_ONLY: int
        ORGANIC_ONLY: int
        ADS_AND_ORGANIC: int
