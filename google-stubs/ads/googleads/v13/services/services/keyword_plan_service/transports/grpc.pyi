from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import keyword_plan_service

from .base import KeywordPlanServiceTransport

class KeywordPlanServiceGrpcTransport(KeywordPlanServiceTransport):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[grpc.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = False
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
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
    def close(self) -> None: ...
