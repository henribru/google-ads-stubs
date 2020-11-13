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

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v6.proto.services import (
    carrier_constant_service_pb2 as carrier_constant_service_pb2,
)
from google.ads.google_ads.v6.services import (
    carrier_constant_service_client_config as carrier_constant_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    carrier_constant_service_grpc_transport as carrier_constant_service_grpc_transport,
)
from google.ads.google_ads.v6.types import CarrierConstant

class CarrierConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CarrierConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CarrierConstantServiceClient: ...
    @classmethod
    def carrier_constant_path(cls, carrier_constant: Any) -> str: ...
    transport: Union[
        carrier_constant_service_grpc_transport.CarrierConstantServiceGrpcTransport,
        Callable[
            [Credentials, type],
            carrier_constant_service_grpc_transport.CarrierConstantServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                carrier_constant_service_grpc_transport.CarrierConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    carrier_constant_service_grpc_transport.CarrierConstantServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_carrier_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CarrierConstant: ...
