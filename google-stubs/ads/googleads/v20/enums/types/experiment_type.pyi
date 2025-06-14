import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExperimentTypeEnum(proto.Message):
    class ExperimentType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DISPLAY_AND_VIDEO_360: int
        AD_VARIATION: int
        YOUTUBE_CUSTOM: int
        DISPLAY_CUSTOM: int
        SEARCH_CUSTOM: int
        DISPLAY_AUTOMATED_BIDDING_STRATEGY: int
        SEARCH_AUTOMATED_BIDDING_STRATEGY: int
        SHOPPING_AUTOMATED_BIDDING_STRATEGY: int
        SMART_MATCHING: int
        HOTEL_CUSTOM: int
