from typing import Any

import proto

__protobuf__: Any

class RecommendationTypeEnum(proto.Message):
    class RecommendationType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CAMPAIGN_BUDGET: int
        KEYWORD: int
        TEXT_AD: int
        TARGET_CPA_OPT_IN: int
        MAXIMIZE_CONVERSIONS_OPT_IN: int
        ENHANCED_CPC_OPT_IN: int
        SEARCH_PARTNERS_OPT_IN: int
        MAXIMIZE_CLICKS_OPT_IN: int
        OPTIMIZE_AD_ROTATION: int
        CALLOUT_EXTENSION: int
        SITELINK_EXTENSION: int
        CALL_EXTENSION: int
        KEYWORD_MATCH_TYPE: int
        MOVE_UNUSED_BUDGET: int
        FORECASTING_CAMPAIGN_BUDGET: int
        TARGET_ROAS_OPT_IN: int
        RESPONSIVE_SEARCH_AD: int
        MARGINAL_ROI_CAMPAIGN_BUDGET: int
