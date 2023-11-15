import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import keyword_plan_idea_service

class KeywordPlanIdeaServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def generate_keyword_ideas(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateKeywordIdeasRequest],
        Union[
            keyword_plan_idea_service.GenerateKeywordIdeaResponse,
            Awaitable[keyword_plan_idea_service.GenerateKeywordIdeaResponse],
        ],
    ]: ...
    @property
    def generate_keyword_historical_metrics(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateKeywordHistoricalMetricsRequest],
        Union[
            keyword_plan_idea_service.GenerateKeywordHistoricalMetricsResponse,
            Awaitable[
                keyword_plan_idea_service.GenerateKeywordHistoricalMetricsResponse
            ],
        ],
    ]: ...
    @property
    def generate_ad_group_themes(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateAdGroupThemesRequest],
        Union[
            keyword_plan_idea_service.GenerateAdGroupThemesResponse,
            Awaitable[keyword_plan_idea_service.GenerateAdGroupThemesResponse],
        ],
    ]: ...
    @property
    def generate_keyword_forecast_metrics(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateKeywordForecastMetricsRequest],
        Union[
            keyword_plan_idea_service.GenerateKeywordForecastMetricsResponse,
            Awaitable[keyword_plan_idea_service.GenerateKeywordForecastMetricsResponse],
        ],
    ]: ...
