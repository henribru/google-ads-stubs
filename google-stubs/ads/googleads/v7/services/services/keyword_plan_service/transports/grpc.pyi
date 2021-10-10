from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import keyword_plan
from google.ads.googleads.v7.services.types import keyword_plan_service

from .base import KeywordPlanServiceTransport

class KeywordPlanServiceGrpcTransport(KeywordPlanServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def get_keyword_plan(
        self,
    ) -> Callable[
        [keyword_plan_service.GetKeywordPlanRequest], keyword_plan.KeywordPlan
    ]: ...
    @property
    def mutate_keyword_plans(
        self,
    ) -> Callable[
        [keyword_plan_service.MutateKeywordPlansRequest],
        keyword_plan_service.MutateKeywordPlansResponse,
    ]: ...
    @property
    def generate_forecast_curve(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateForecastCurveRequest],
        keyword_plan_service.GenerateForecastCurveResponse,
    ]: ...
    @property
    def generate_forecast_time_series(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateForecastTimeSeriesRequest],
        keyword_plan_service.GenerateForecastTimeSeriesResponse,
    ]: ...
    @property
    def generate_forecast_metrics(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateForecastMetricsRequest],
        keyword_plan_service.GenerateForecastMetricsResponse,
    ]: ...
    @property
    def generate_historical_metrics(
        self,
    ) -> Callable[
        [keyword_plan_service.GenerateHistoricalMetricsRequest],
        keyword_plan_service.GenerateHistoricalMetricsResponse,
    ]: ...
