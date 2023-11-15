import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import smart_campaign_suggest_service

class SmartCampaignSuggestServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def suggest_smart_campaign_budget_options(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsRequest],
        smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse
        | Awaitable[
            smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse
        ],
    ]: ...
    @property
    def suggest_smart_campaign_ad(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignAdRequest],
        smart_campaign_suggest_service.SuggestSmartCampaignAdResponse
        | Awaitable[smart_campaign_suggest_service.SuggestSmartCampaignAdResponse],
    ]: ...
    @property
    def suggest_keyword_themes(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestKeywordThemesRequest],
        smart_campaign_suggest_service.SuggestKeywordThemesResponse
        | Awaitable[smart_campaign_suggest_service.SuggestKeywordThemesResponse],
    ]: ...
