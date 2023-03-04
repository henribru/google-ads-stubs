from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v11.common.types.ad_type_infos import SmartCampaignAdInfo
from google.ads.googleads.v11.common.types.criteria import (
    AdScheduleInfo,
    KeywordThemeInfo,
    LocationInfo,
    ProximityInfo,
)
from google.ads.googleads.v11.resources.types.keyword_theme_constant import (
    KeywordThemeConstant,
)

class SmartCampaignSuggestionInfo(proto.Message):
    class BusinessContext(proto.Message):
        business_name: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            business_name: str = ...
        ) -> None: ...

    class LocationList(proto.Message):
        locations: MutableSequence[LocationInfo]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            locations: MutableSequence[LocationInfo] = ...
        ) -> None: ...
    final_url: str
    language_code: str
    ad_schedules: MutableSequence[AdScheduleInfo]
    keyword_themes: MutableSequence[KeywordThemeInfo]
    business_context: SmartCampaignSuggestionInfo.BusinessContext
    business_profile_location: str
    location_list: SmartCampaignSuggestionInfo.LocationList
    proximity: ProximityInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        final_url: str = ...,
        language_code: str = ...,
        ad_schedules: MutableSequence[AdScheduleInfo] = ...,
        keyword_themes: MutableSequence[KeywordThemeInfo] = ...,
        business_context: SmartCampaignSuggestionInfo.BusinessContext = ...,
        business_profile_location: str = ...,
        location_list: SmartCampaignSuggestionInfo.LocationList = ...,
        proximity: ProximityInfo = ...
    ) -> None: ...

class SuggestKeywordThemesRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        suggestion_info: SmartCampaignSuggestionInfo = ...
    ) -> None: ...

class SuggestKeywordThemesResponse(proto.Message):
    keyword_themes: MutableSequence[KeywordThemeConstant]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        keyword_themes: MutableSequence[KeywordThemeConstant] = ...
    ) -> None: ...

class SuggestSmartCampaignAdRequest(proto.Message):
    customer_id: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        suggestion_info: SmartCampaignSuggestionInfo = ...
    ) -> None: ...

class SuggestSmartCampaignAdResponse(proto.Message):
    ad_info: SmartCampaignAdInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_info: SmartCampaignAdInfo = ...
    ) -> None: ...

class SuggestSmartCampaignBudgetOptionsRequest(proto.Message):
    customer_id: str
    campaign: str
    suggestion_info: SmartCampaignSuggestionInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        campaign: str = ...,
        suggestion_info: SmartCampaignSuggestionInfo = ...
    ) -> None: ...

class SuggestSmartCampaignBudgetOptionsResponse(proto.Message):
    class BudgetOption(proto.Message):
        daily_amount_micros: int
        metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            daily_amount_micros: int = ...,
            metrics: SuggestSmartCampaignBudgetOptionsResponse.Metrics = ...
        ) -> None: ...

    class Metrics(proto.Message):
        min_daily_clicks: int
        max_daily_clicks: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            min_daily_clicks: int = ...,
            max_daily_clicks: int = ...
        ) -> None: ...
    low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        low: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...,
        recommended: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...,
        high: SuggestSmartCampaignBudgetOptionsResponse.BudgetOption = ...
    ) -> None: ...
