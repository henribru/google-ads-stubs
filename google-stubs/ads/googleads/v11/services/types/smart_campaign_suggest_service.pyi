import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    ad_type_infos as ad_type_infos,
    criteria as criteria,
)
from google.ads.googleads.v11.resources.types import (
    keyword_theme_constant as keyword_theme_constant,
)

__protobuf__: Incomplete

class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    customer_id: Incomplete
    campaign: Incomplete
    suggestion_info: Incomplete

class SmartCampaignSuggestionInfo(proto.Message):
    class LocationList(proto.Message):
        locations: Incomplete

    class BusinessContext(proto.Message):
        business_name: Incomplete
    final_url: Incomplete
    language_code: Incomplete
    ad_schedules: Incomplete
    keyword_themes: Incomplete
    business_context: Incomplete
    business_profile_location: Incomplete
    location_list: Incomplete
    proximity: Incomplete

class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    class Metrics(proto.Message):
        min_daily_clicks: Incomplete
        max_daily_clicks: Incomplete

    class BudgetOption(proto.Message):
        daily_amount_micros: Incomplete
        metrics: Incomplete
    low: Incomplete
    recommended: Incomplete
    high: Incomplete

class SuggestSmartCampaignAdRequest(proto.Message):
    customer_id: Incomplete
    suggestion_info: Incomplete

class SuggestSmartCampaignAdResponse(proto.Message):
    ad_info: Incomplete

class SuggestKeywordThemesRequest(proto.Message):
    customer_id: Incomplete
    suggestion_info: Incomplete

class SuggestKeywordThemesResponse(proto.Message):
    keyword_themes: Incomplete
