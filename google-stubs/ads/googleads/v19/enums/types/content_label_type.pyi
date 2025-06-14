import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ContentLabelTypeEnum(proto.Message):
    class ContentLabelType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEXUALLY_SUGGESTIVE: int
        BELOW_THE_FOLD: int
        PARKED_DOMAIN: int
        JUVENILE: int
        PROFANITY: int
        TRAGEDY: int
        VIDEO: int
        VIDEO_RATING_DV_G: int
        VIDEO_RATING_DV_PG: int
        VIDEO_RATING_DV_T: int
        VIDEO_RATING_DV_MA: int
        VIDEO_NOT_YET_RATED: int
        EMBEDDED_VIDEO: int
        LIVE_STREAMING_VIDEO: int
        SOCIAL_ISSUES: int
        BRAND_SUITABILITY_CONTENT_FOR_FAMILIES: int
        BRAND_SUITABILITY_GAMES_FIGHTING: int
        BRAND_SUITABILITY_GAMES_MATURE: int
        BRAND_SUITABILITY_HEALTH_SENSITIVE: int
        BRAND_SUITABILITY_HEALTH_SOURCE_UNDETERMINED: int
        BRAND_SUITABILITY_NEWS_RECENT: int
        BRAND_SUITABILITY_NEWS_SENSITIVE: int
        BRAND_SUITABILITY_NEWS_SOURCE_NOT_FEATURED: int
        BRAND_SUITABILITY_POLITICS: int
        BRAND_SUITABILITY_RELIGION: int
