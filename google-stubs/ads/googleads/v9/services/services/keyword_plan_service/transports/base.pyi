import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import keyword_plan
from google.ads.googleads.v9.services.types import keyword_plan_service

class KeywordPlanServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_keyword_plan(
        self,
    ) -> typing.Callable[
        [keyword_plan_service.GetKeywordPlanRequest], keyword_plan.KeywordPlan
    ]: ...
    @property
    def mutate_keyword_plans(
        self,
    ) -> typing.Callable[
        [keyword_plan_service.MutateKeywordPlansRequest],
        keyword_plan_service.MutateKeywordPlansResponse,
    ]: ...
    @property
    def generate_forecast_curve(
        self,
    ) -> typing.Callable[
        [keyword_plan_service.GenerateForecastCurveRequest],
        keyword_plan_service.GenerateForecastCurveResponse,
    ]: ...
    @property
    def generate_forecast_time_series(
        self,
    ) -> typing.Callable[
        [keyword_plan_service.GenerateForecastTimeSeriesRequest],
        keyword_plan_service.GenerateForecastTimeSeriesResponse,
    ]: ...
    @property
    def generate_forecast_metrics(
        self,
    ) -> typing.Callable[
        [keyword_plan_service.GenerateForecastMetricsRequest],
        keyword_plan_service.GenerateForecastMetricsResponse,
    ]: ...
    @property
    def generate_historical_metrics(
        self,
    ) -> typing.Callable[
        [keyword_plan_service.GenerateHistoricalMetricsRequest],
        keyword_plan_service.GenerateHistoricalMetricsResponse,
    ]: ...
