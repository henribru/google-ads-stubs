from typing import Callable, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import audience_insights_service

from .base import AudienceInsightsServiceTransport

__all__ = ["AudienceInsightsServiceGrpcTransport"]

class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):
    def intercept_unary_unary(self, continuation, client_call_details, request): ...

class AudienceInsightsServiceGrpcTransport(AudienceInsightsServiceTransport):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        channel: grpc.Channel | Callable[..., grpc.Channel] | None = None,
        api_mtls_endpoint: str | None = None,
        client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None,
        ssl_channel_credentials: grpc.ChannelCredentials | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        **kwargs,
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def generate_insights_finder_report(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateInsightsFinderReportRequest],
        audience_insights_service.GenerateInsightsFinderReportResponse,
    ]: ...
    @property
    def list_audience_insights_attributes(
        self,
    ) -> Callable[
        [audience_insights_service.ListAudienceInsightsAttributesRequest],
        audience_insights_service.ListAudienceInsightsAttributesResponse,
    ]: ...
    @property
    def list_insights_eligible_dates(
        self,
    ) -> Callable[
        [audience_insights_service.ListInsightsEligibleDatesRequest],
        audience_insights_service.ListInsightsEligibleDatesResponse,
    ]: ...
    @property
    def generate_audience_composition_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateAudienceCompositionInsightsRequest],
        audience_insights_service.GenerateAudienceCompositionInsightsResponse,
    ]: ...
    @property
    def generate_suggested_targeting_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateSuggestedTargetingInsightsRequest],
        audience_insights_service.GenerateSuggestedTargetingInsightsResponse,
    ]: ...
    @property
    def generate_audience_overlap_insights(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateAudienceOverlapInsightsRequest],
        audience_insights_service.GenerateAudienceOverlapInsightsResponse,
    ]: ...
    @property
    def generate_targeting_suggestion_metrics(
        self,
    ) -> Callable[
        [audience_insights_service.GenerateTargetingSuggestionMetricsRequest],
        audience_insights_service.GenerateTargetingSuggestionMetricsResponse,
    ]: ...
    def close(self) -> None: ...
    @property
    def kind(self) -> str: ...
