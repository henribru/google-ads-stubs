import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AudienceInsightsDimensionEnum(proto.Message):
    class AudienceInsightsDimension(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CATEGORY = 2
        KNOWLEDGE_GRAPH = 3
        GEO_TARGET_COUNTRY = 4
        SUB_COUNTRY_LOCATION = 5
        YOUTUBE_CHANNEL = 6
        AFFINITY_USER_INTEREST = 8
        IN_MARKET_USER_INTEREST = 9
        PARENTAL_STATUS = 10
        INCOME_RANGE = 11
        AGE_RANGE = 12
        GENDER = 13
        YOUTUBE_VIDEO = 14
        DEVICE = 15
        YOUTUBE_LINEUP = 16
        USER_LIST = 17
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
