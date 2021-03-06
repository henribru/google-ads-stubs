from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v6.proto.services import (
    currency_constant_service_pb2 as currency_constant_service_pb2,
)
from google.ads.google_ads.v6.services import (
    currency_constant_service_client_config as currency_constant_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    currency_constant_service_grpc_transport as currency_constant_service_grpc_transport,
)
from google.ads.google_ads.v6.types import CurrencyConstant

class CurrencyConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CurrencyConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CurrencyConstantServiceClient: ...
    @classmethod
    def currency_constant_path(cls, code: Any) -> str: ...
    transport: Union[
        currency_constant_service_grpc_transport.CurrencyConstantServiceGrpcTransport,
        Callable[
            [Credentials, type],
            currency_constant_service_grpc_transport.CurrencyConstantServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                currency_constant_service_grpc_transport.CurrencyConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    currency_constant_service_grpc_transport.CurrencyConstantServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_currency_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CurrencyConstant: ...
