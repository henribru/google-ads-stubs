import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import keyword_plan_service

class KeywordPlanServiceTransport(abc.ABC):
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
    def mutate_keyword_plans(
        self,
    ) -> Callable[
        [keyword_plan_service.MutateKeywordPlansRequest],
        Union[
            keyword_plan_service.MutateKeywordPlansResponse,
            Awaitable[keyword_plan_service.MutateKeywordPlansResponse],
        ],
    ]: ...
    @property
    def generate_forecast_curve(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateForecastCurveRequest],
        Union[
            keyword_plan_service.GenerateForecastCurveResponse,
            Awaitable[keyword_plan_service.GenerateForecastCurveResponse],
        ],
    ]: ...
    @property
    def generate_forecast_time_series(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateForecastTimeSeriesRequest],
        Union[
            keyword_plan_service.GenerateForecastTimeSeriesResponse,
            Awaitable[keyword_plan_service.GenerateForecastTimeSeriesResponse],
        ],
    ]: ...
    @property
    def generate_forecast_metrics(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateForecastMetricsRequest],
        Union[
            keyword_plan_service.GenerateForecastMetricsResponse,
            Awaitable[keyword_plan_service.GenerateForecastMetricsResponse],
        ],
    ]: ...
    @property
    def generate_historical_metrics(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateHistoricalMetricsRequest],
        Union[
            keyword_plan_service.GenerateHistoricalMetricsResponse,
            Awaitable[keyword_plan_service.GenerateHistoricalMetricsResponse],
        ],
    ]: ...
