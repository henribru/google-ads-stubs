import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ContentLabelTypeEnum(proto.Message):
    class ContentLabelType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SEXUALLY_SUGGESTIVE = 2
        BELOW_THE_FOLD = 3
        PARKED_DOMAIN = 4
        JUVENILE = 6
        PROFANITY = 7
        TRAGEDY = 8
        VIDEO = 9
        VIDEO_RATING_DV_G = 10
        VIDEO_RATING_DV_PG = 11
        VIDEO_RATING_DV_T = 12
        VIDEO_RATING_DV_MA = 13
        VIDEO_NOT_YET_RATED = 14
        EMBEDDED_VIDEO = 15
        LIVE_STREAMING_VIDEO = 16
        SOCIAL_ISSUES = 17
        BRAND_SUITABILITY_CONTENT_FOR_FAMILIES = 18
        BRAND_SUITABILITY_GAMES_FIGHTING = 19
        BRAND_SUITABILITY_GAMES_MATURE = 20
        BRAND_SUITABILITY_HEALTH_SENSITIVE = 21
        BRAND_SUITABILITY_HEALTH_SOURCE_UNDETERMINED = 22
        BRAND_SUITABILITY_NEWS_RECENT = 23
        BRAND_SUITABILITY_NEWS_SENSITIVE = 24
        BRAND_SUITABILITY_NEWS_SOURCE_NOT_FEATURED = 25
        BRAND_SUITABILITY_POLITICS = 26
        BRAND_SUITABILITY_RELIGION = 27
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
