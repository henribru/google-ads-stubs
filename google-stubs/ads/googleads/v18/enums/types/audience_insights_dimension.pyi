import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AudienceInsightsDimensionEnum(proto.Message):
    class AudienceInsightsDimension(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CATEGORY: int
        KNOWLEDGE_GRAPH: int
        GEO_TARGET_COUNTRY: int
        SUB_COUNTRY_LOCATION: int
        YOUTUBE_CHANNEL: int
        YOUTUBE_DYNAMIC_LINEUP: int
        AFFINITY_USER_INTEREST: int
        IN_MARKET_USER_INTEREST: int
        PARENTAL_STATUS: int
        INCOME_RANGE: int
        AGE_RANGE: int
        GENDER: int
