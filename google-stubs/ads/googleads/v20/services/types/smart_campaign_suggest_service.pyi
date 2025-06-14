import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import ad_type_infos, criteria
from google.ads.googleads.v20.resources.types import keyword_theme_constant as gagr_keyword_theme_constant
from typing import MutableSequence

__protobuf__: Incomplete

class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    customer_id: str
    campaign: str
    suggestion_info: SmartCampaignSuggestionInfo

class SmartCampaignSuggestionInfo(proto.Message):
    class LocationList(proto.Message):
        locations: MutableSequence[criteria.LocationInfo]
    class BusinessContext(proto.Message):
        business_name: str
    final_url: str
    language_code: str
    ad_schedules: MutableSequence[criteria.AdScheduleInfo]
    keyword_themes: MutableSequence[criteria.KeywordThemeInfo]
    business_context: BusinessContext
    business_profile_location: str
    location_list: LocationList
    proximity: criteria.ProximityInfo

class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    class Metrics(proto.Message):
        min_daily_clicks: int
        max_daily_clicks: int
    class BudgetOption(proto.Message):
        daily_amount_micros: int
        metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics
    low: BudgetOption
    recommended: BudgetOption
    high: BudgetOption

class SuggestSmartCampaignAdRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo

class SuggestSmartCampaignAdResponse(proto.Message):
    ad_info: ad_type_infos.SmartCampaignAdInfo

class SuggestKeywordThemesRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo

class SuggestKeywordThemesResponse(proto.Message):
    class KeywordTheme(proto.Message):
        keyword_theme_constant: gagr_keyword_theme_constant.KeywordThemeConstant
        free_form_keyword_theme: str
    keyword_themes: MutableSequence[KeywordTheme]
