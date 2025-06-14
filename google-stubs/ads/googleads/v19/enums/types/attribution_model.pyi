import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class AttributionModelEnum(proto.Message):
    class AttributionModel(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        EXTERNAL: int
        GOOGLE_ADS_LAST_CLICK: int
        GOOGLE_SEARCH_ATTRIBUTION_FIRST_CLICK: int
        GOOGLE_SEARCH_ATTRIBUTION_LINEAR: int
        GOOGLE_SEARCH_ATTRIBUTION_TIME_DECAY: int
        GOOGLE_SEARCH_ATTRIBUTION_POSITION_BASED: int
        GOOGLE_SEARCH_ATTRIBUTION_DATA_DRIVEN: int
