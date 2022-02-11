from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import reach_plan_service

from .base import ReachPlanServiceTransport

class ReachPlanServiceGrpcTransport(ReachPlanServiceTransport):
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
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        scopes: Optional[Sequence[str]] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    def close(self) -> None: ...
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
    def generate_product_mix_ideas(
        self,
    ) -> Callable[
        [reach_plan_service.GenerateProductMixIdeasRequest],
        reach_plan_service.GenerateProductMixIdeasResponse,
    ]: ...
    @property
    def generate_reach_forecast(
        self,
    ) -> Callable[
        [reach_plan_service.GenerateReachForecastRequest],
        reach_plan_service.GenerateReachForecastResponse,
    ]: ...
