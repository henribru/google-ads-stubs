from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import ad_parameter
from google.ads.googleads.v8.services.types import ad_parameter_service

from .base import AdParameterServiceTransport

class AdParameterServiceGrpcTransport(AdParameterServiceTransport):
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
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def get_ad_parameter(
        self,
    ) -> Callable[
        [ad_parameter_service.GetAdParameterRequest], ad_parameter.AdParameter
    ]: ...
    @property
    def mutate_ad_parameters(
        self,
    ) -> Callable[
        [ad_parameter_service.MutateAdParametersRequest],
        ad_parameter_service.MutateAdParametersResponse,
    ]: ...
