from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

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
        KEYWORD_MATCH_TYPE = 14
        MOVE_UNUSED_BUDGET = 15
        FORECASTING_CAMPAIGN_BUDGET = 16
        TARGET_ROAS_OPT_IN = 17
        RESPONSIVE_SEARCH_AD = 18
        MARGINAL_ROI_CAMPAIGN_BUDGET = 19
        USE_BROAD_MATCH_KEYWORD = 20
        RESPONSIVE_SEARCH_AD_ASSET = 21
        UPGRADE_SMART_SHOPPING_CAMPAIGN_TO_PERFORMANCE_MAX = 22
        RESPONSIVE_SEARCH_AD_IMPROVE_AD_STRENGTH = 23
        DISPLAY_EXPANSION_OPT_IN = 24
        UPGRADE_LOCAL_CAMPAIGN_TO_PERFORMANCE_MAX = 25
        RAISE_TARGET_CPA_BID_TOO_LOW = 26
        FORECASTING_SET_TARGET_ROAS = 27
        CALLOUT_ASSET = 28
        SITELINK_ASSET = 29
        CALL_ASSET = 30
        SHOPPING_ADD_AGE_GROUP = 31
        SHOPPING_ADD_COLOR = 32
        SHOPPING_ADD_GENDER = 33
        SHOPPING_ADD_GTIN = 34
        SHOPPING_ADD_MORE_IDENTIFIERS = 35
        SHOPPING_ADD_SIZE = 36
        SHOPPING_ADD_PRODUCTS_TO_CAMPAIGN = 37
        SHOPPING_FIX_DISAPPROVED_PRODUCTS = 38
        SHOPPING_TARGET_ALL_OFFERS = 39
        SHOPPING_FIX_SUSPENDED_MERCHANT_CENTER_ACCOUNT = 40
        SHOPPING_FIX_MERCHANT_CENTER_ACCOUNT_SUSPENSION_WARNING = 41
        SHOPPING_MIGRATE_REGULAR_SHOPPING_CAMPAIGN_OFFERS_TO_PERFORMANCE_MAX = 42
        DYNAMIC_IMAGE_EXTENSION_OPT_IN = 43
        RAISE_TARGET_CPA = 44
        LOWER_TARGET_ROAS = 45
        PERFORMANCE_MAX_OPT_IN = 46
        IMPROVE_PERFORMANCE_MAX_AD_STRENGTH = 47
        MIGRATE_DYNAMIC_SEARCH_ADS_CAMPAIGN_TO_PERFORMANCE_MAX = 48
        FORECASTING_SET_TARGET_CPA = 49
        SET_TARGET_CPA = 50
        SET_TARGET_ROAS = 51

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
