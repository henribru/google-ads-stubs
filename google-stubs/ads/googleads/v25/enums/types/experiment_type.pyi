from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ExperimentTypeEnum(proto.Message):
    class ExperimentType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DISPLAY_AND_VIDEO_360 = 2
        AD_VARIATION = 3
        YOUTUBE_CUSTOM = 5
        DISPLAY_CUSTOM = 6
        SEARCH_CUSTOM = 7
        DISPLAY_AUTOMATED_BIDDING_STRATEGY = 8
        SEARCH_AUTOMATED_BIDDING_STRATEGY = 9
        SHOPPING_AUTOMATED_BIDDING_STRATEGY = 10
        SMART_MATCHING = 11
        HOTEL_CUSTOM = 12
        OPTIMIZE_ASSETS = 13
        ADOPT_AI_MAX = 14
        ADOPT_BROAD_MATCH_KEYWORDS = 15
        PMAX_REPLACEMENT_SHOPPING = 16
        COMPARE_CAMPAIGNS = 17
        PMAX_TEXT_CUSTOMIZATION_FINAL_URL_EXPANSION = 18

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
