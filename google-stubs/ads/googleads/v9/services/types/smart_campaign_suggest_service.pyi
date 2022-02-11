from typing import Any

import proto

from google.ads.googleads.v9.common.types import (
    ad_type_infos as ad_type_infos,
    criteria as criteria,
)
from google.ads.googleads.v9.resources.types import (
    keyword_theme_constant as keyword_theme_constant,
)

__protobuf__: Any

class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    customer_id: Any
    campaign: Any
    suggestion_info: Any

class SmartCampaignSuggestionInfo(proto.Message):
    class LocationList(proto.Message):
        locations: Any
    class BusinessContext(proto.Message):
        business_name: Any
    final_url: Any
    language_code: Any
    ad_schedules: Any
    keyword_themes: Any
    business_context: Any
    business_location_id: Any
    location_list: Any
    proximity: Any

class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    class Metrics(proto.Message):
        min_daily_clicks: Any
        max_daily_clicks: Any
    class BudgetOption(proto.Message):
        daily_amount_micros: Any
        metrics: Any
    low: Any
    recommended: Any
    high: Any

class SuggestSmartCampaignAdRequest(proto.Message):
    customer_id: Any
    suggestion_info: Any

class SuggestSmartCampaignAdResponse(proto.Message):
    ad_info: Any

class SuggestKeywordThemesRequest(proto.Message):
    customer_id: Any
    suggestion_info: Any

class SuggestKeywordThemesResponse(proto.Message):
    keyword_themes: Any
