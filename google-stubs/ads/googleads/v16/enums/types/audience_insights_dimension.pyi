from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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
        YOUTUBE_DYNAMIC_LINEUP = 7
        AFFINITY_USER_INTEREST = 8
        IN_MARKET_USER_INTEREST = 9
        PARENTAL_STATUS = 10
        INCOME_RANGE = 11
        AGE_RANGE = 12
        GENDER = 13

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
