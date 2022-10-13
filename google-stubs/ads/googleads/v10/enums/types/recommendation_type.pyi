from typing import Any

import proto

class RecommendationTypeEnum(proto.Message):
    class RecommendationType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CAMPAIGN_BUDGET = 2
        KEYWORD = 3
        TEXT_AD = 4
        TARGET_CPA_OPT_IN = 5
        MAXIMIZE_CONVERSIONS_OPT_IN = 6
        ENHANCED_CPC_OPT_IN = 7
        SEARCH_PARTNERS_OPT_IN = 8
        MAXIMIZE_CLICKS_OPT_IN = 9
        OPTIMIZE_AD_ROTATION = 10
        CALLOUT_EXTENSION = 11
        SITELINK_EXTENSION = 12
        CALL_EXTENSION = 13
        KEYWORD_MATCH_TYPE = 14
        MOVE_UNUSED_BUDGET = 15
        FORECASTING_CAMPAIGN_BUDGET = 16
        TARGET_ROAS_OPT_IN = 17
        RESPONSIVE_SEARCH_AD = 18
        MARGINAL_ROI_CAMPAIGN_BUDGET = 19
        USE_BROAD_MATCH_KEYWORD = 20
        RESPONSIVE_SEARCH_AD_ASSET = 21
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
