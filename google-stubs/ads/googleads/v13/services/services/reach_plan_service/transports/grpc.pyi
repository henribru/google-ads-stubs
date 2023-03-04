from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import reach_plan_service

from .base import ReachPlanServiceTransport

class ReachPlanServiceGrpcTransport(ReachPlanServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        channel: Optional[grpc.Channel] = ...,
        api_mtls_endpoint: Optional[str] = ...,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = ...,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def list_plannable_locations(
        self,
    ) -> Callable[
        [reach_plan_service.ListPlannableLocationsRequest],
        reach_plan_service.ListPlannableLocationsResponse,
    ]: ...
    @property
    def list_plannable_products(
        self,
    ) -> Callable[
        [reach_plan_service.ListPlannableProductsRequest],
        reach_plan_service.ListPlannableProductsResponse,
    ]: ...
    @property
    def generate_reach_forecast(
        self,
    ) -> Callable[
        [reach_plan_service.GenerateReachForecastRequest],
        reach_plan_service.GenerateReachForecastResponse,
    ]: ...
    def close(self) -> None: ...
