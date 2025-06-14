from google.ads.googleads.v19.common.types.ad_type_infos import SmartCampaignAdInfo
from collections.abc import MutableSequence
from google.ads.googleads.v19.resources.types.keyword_theme_constant import KeywordThemeConstant
from google.ads.googleads.v19.common.types.criteria import ProximityInfo
from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.criteria import KeywordThemeInfo
from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.criteria import AdScheduleInfo
from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.criteria import LocationInfo
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SmartCampaignSuggestionInfo(proto.Message):
    class BusinessContext(proto.Message):
        business_name: str
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., business_name: str = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["business_name"]) -> bool: ...
    class LocationList(proto.Message):
        locations: MutableSequence[LocationInfo]
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., locations: MutableSequence[LocationInfo] = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["locations"]) -> bool: ...
    final_url: str
    language_code: str
    ad_schedules: MutableSequence[AdScheduleInfo]
    keyword_themes: MutableSequence[KeywordThemeInfo]
    business_context: SmartCampaignSuggestionInfo.BusinessContext
    business_profile_location: str
    location_list: SmartCampaignSuggestionInfo.LocationList
    proximity: ProximityInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., final_url: str = ..., language_code: str = ..., ad_schedules: MutableSequence[AdScheduleInfo] = ..., keyword_themes: MutableSequence[KeywordThemeInfo] = ..., business_context: SmartCampaignSuggestionInfo.BusinessContext = ..., business_profile_location: str = ..., location_list: SmartCampaignSuggestionInfo.LocationList = ..., proximity: ProximityInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["final_url", "language_code", "ad_schedules", "keyword_themes", "business_context", "business_profile_location", "location_list", "proximity"]) -> bool: ...
class SuggestKeywordThemesRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., suggestion_info: SmartCampaignSuggestionInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "suggestion_info"]) -> bool: ...
class SuggestKeywordThemesResponse(proto.Message):
    class KeywordTheme(proto.Message):
        keyword_theme_constant: KeywordThemeConstant
        free_form_keyword_theme: str
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., keyword_theme_constant: KeywordThemeConstant = ..., free_form_keyword_theme: str = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["keyword_theme_constant", "free_form_keyword_theme"]) -> bool: ...
    keyword_themes: MutableSequence[SuggestKeywordThemesResponse.KeywordTheme]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., keyword_themes: MutableSequence[SuggestKeywordThemesResponse.KeywordTheme] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["keyword_themes"]) -> bool: ...
class SuggestSmartCampaignAdRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., suggestion_info: SmartCampaignSuggestionInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "suggestion_info"]) -> bool: ...
class SuggestSmartCampaignAdResponse(proto.Message):
    ad_info: SmartCampaignAdInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ad_info: SmartCampaignAdInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["ad_info"]) -> bool: ...
class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    customer_id: str
    campaign: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., campaign: str = ..., suggestion_info: SmartCampaignSuggestionInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "campaign", "suggestion_info"]) -> bool: ...
class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    class BudgetOption(proto.Message):
        daily_amount_micros: int
        metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., daily_amount_micros: int = ..., metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["daily_amount_micros", "metrics"]) -> bool: ...
    class Metrics(proto.Message):
        min_daily_clicks: int
        max_daily_clicks: int
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., min_daily_clicks: int = ..., max_daily_clicks: int = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["min_daily_clicks", "max_daily_clicks"]) -> bool: ...
    low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ..., recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ..., high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["low", "recommended", "high"]) -> bool: ...
