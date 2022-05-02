from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import keyword_plan_idea_service

from .base import KeywordPlanIdeaServiceTransport

class KeywordPlanIdeaServiceGrpcTransport(KeywordPlanIdeaServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Sequence[str] = ...,
        channel: grpc.Channel = ...,
        api_mtls_endpoint: str = ...,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = ...,
        ssl_channel_credentials: grpc.ChannelCredentials = ...,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: str = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
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
    def close(self) -> None: ...
