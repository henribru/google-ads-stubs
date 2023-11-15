from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import keyword_plan_idea_service

from .base import KeywordPlanIdeaServiceTransport

class KeywordPlanIdeaServiceGrpcTransport(KeywordPlanIdeaServiceTransport):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        channel: grpc.Channel | None = None,
        api_mtls_endpoint: str | None = None,
        client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None,
        ssl_channel_credentials: grpc.ChannelCredentials | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def generate_keyword_ideas(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateKeywordIdeasRequest],
        keyword_plan_idea_service.GenerateKeywordIdeaResponse,
    ]: ...
    @property
    def generate_keyword_historical_metrics(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateKeywordHistoricalMetricsRequest],
        keyword_plan_idea_service.GenerateKeywordHistoricalMetricsResponse,
    ]: ...
    @property
    def generate_ad_group_themes(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateAdGroupThemesRequest],
        keyword_plan_idea_service.GenerateAdGroupThemesResponse,
    ]: ...
    @property
    def generate_keyword_forecast_metrics(
        self,
    ) -> Callable[
        [keyword_plan_idea_service.GenerateKeywordForecastMetricsRequest],
        keyword_plan_idea_service.GenerateKeywordForecastMetricsResponse,
    ]: ...
    def close(self) -> None: ...
