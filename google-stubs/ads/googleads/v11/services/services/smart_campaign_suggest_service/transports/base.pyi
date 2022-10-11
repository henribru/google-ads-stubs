import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import smart_campaign_suggest_service

class SmartCampaignSuggestServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def suggest_smart_campaign_budget_options(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsRequest],
        Union[
            smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse,
            Awaitable[
                smart_campaign_suggest_service.SuggestSmartCampaignBudgetOptionsResponse
            ],
        ],
    ]: ...
    @property
    def suggest_smart_campaign_ad(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestSmartCampaignAdRequest],
        Union[
            smart_campaign_suggest_service.SuggestSmartCampaignAdResponse,
            Awaitable[smart_campaign_suggest_service.SuggestSmartCampaignAdResponse],
        ],
    ]: ...
    @property
    def suggest_keyword_themes(
        self,
    ) -> Callable[
        [smart_campaign_suggest_service.SuggestKeywordThemesRequest],
        Union[
            smart_campaign_suggest_service.SuggestKeywordThemesResponse,
            Awaitable[smart_campaign_suggest_service.SuggestKeywordThemesResponse],
        ],
    ]: ...
