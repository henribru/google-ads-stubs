from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.ad_type_infos import SmartCampaignAdInfo
from google.ads.googleads.v14.common.types.criteria import (
    AdScheduleInfo,
    KeywordThemeInfo,
    LocationInfo,
    ProximityInfo,
)
from google.ads.googleads.v14.resources.types.keyword_theme_constant import (
    KeywordThemeConstant,
)

_M = TypeVar("_M")

class SmartCampaignSuggestionInfo(proto.Message):
    class BusinessContext(proto.Message):
        business_name: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            business_name: str = ...
        ) -> None: ...
        def __contains__(self, key: Literal["business_name"]) -> bool: ...  # type: ignore[override]

    class LocationList(proto.Message):
        locations: MutableSequence[LocationInfo]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            locations: MutableSequence[LocationInfo] = ...
        ) -> None: ...
        def __contains__(self, key: Literal["locations"]) -> bool: ...  # type: ignore[override]
    final_url: str
    language_code: str
    ad_schedules: MutableSequence[AdScheduleInfo]
    keyword_themes: MutableSequence[KeywordThemeInfo]
    business_context: SmartCampaignSuggestionInfo.BusinessContext
    business_profile_location: str
    location_list: SmartCampaignSuggestionInfo.LocationList
    proximity: ProximityInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        final_url: str = ...,
        language_code: str = ...,
        ad_schedules: MutableSequence[AdScheduleInfo] = ...,
        keyword_themes: MutableSequence[KeywordThemeInfo] = ...,
        business_context: SmartCampaignSuggestionInfo.BusinessContext = ...,
        business_profile_location: str = ...,
        location_list: SmartCampaignSuggestionInfo.LocationList = ...,
        proximity: ProximityInfo = ...
    ) -> None: ...
    def __contains__(self, key: Literal["final_url", "language_code", "ad_schedules", "keyword_themes", "business_context", "business_profile_location", "location_list", "proximity"]) -> bool: ...  # type: ignore[override]

class SuggestKeywordThemesRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        suggestion_info: SmartCampaignSuggestionInfo = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "suggestion_info"]) -> bool: ...  # type: ignore[override]

class SuggestKeywordThemesResponse(proto.Message):
    class KeywordTheme(proto.Message):
        keyword_theme_constant: KeywordThemeConstant
        free_form_keyword_theme: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            keyword_theme_constant: KeywordThemeConstant = ...,
            free_form_keyword_theme: str = ...
        ) -> None: ...
        def __contains__(self, key: Literal["keyword_theme_constant", "free_form_keyword_theme"]) -> bool: ...  # type: ignore[override]
    keyword_themes: MutableSequence[SuggestKeywordThemesResponse.KeywordTheme]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        keyword_themes: MutableSequence[SuggestKeywordThemesResponse.KeywordTheme] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["keyword_themes"]) -> bool: ...  # type: ignore[override]

class SuggestSmartCampaignAdRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        suggestion_info: SmartCampaignSuggestionInfo = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "suggestion_info"]) -> bool: ...  # type: ignore[override]

class SuggestSmartCampaignAdResponse(proto.Message):
    ad_info: SmartCampaignAdInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_info: SmartCampaignAdInfo = ...
    ) -> None: ...
    def __contains__(self, key: Literal["ad_info"]) -> bool: ...  # type: ignore[override]

class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    customer_id: str
    campaign: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        campaign: str = ...,
        suggestion_info: SmartCampaignSuggestionInfo = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "campaign", "suggestion_info"]) -> bool: ...  # type: ignore[override]

class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    class BudgetOption(proto.Message):
        daily_amount_micros: int
        metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            daily_amount_micros: int = ...,
            metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics = ...
        ) -> None: ...
        def __contains__(self, key: Literal["daily_amount_micros", "metrics"]) -> bool: ...  # type: ignore[override]

    class Metrics(proto.Message):
        min_daily_clicks: int
        max_daily_clicks: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            min_daily_clicks: int = ...,
            max_daily_clicks: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["min_daily_clicks", "max_daily_clicks"]) -> bool: ...  # type: ignore[override]
    low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...,
        recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...,
        high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...
    ) -> None: ...
    def __contains__(self, key: Literal["low", "recommended", "high"]) -> bool: ...  # type: ignore[override]
