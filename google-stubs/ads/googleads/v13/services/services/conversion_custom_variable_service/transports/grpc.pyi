from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import conversion_custom_variable_service

from .base import ConversionCustomVariableServiceTransport

class ConversionCustomVariableServiceGrpcTransport(
    ConversionCustomVariableServiceTransport
):
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
    def mutate_conversion_custom_variables(
        self,
    ) -> Callable[
        [conversion_custom_variable_service.MutateConversionCustomVariablesRequest],
        conversion_custom_variable_service.MutateConversionCustomVariablesResponse,
    ]: ...
    def close(self) -> None: ...
