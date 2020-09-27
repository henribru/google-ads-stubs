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

from google.ads.google_ads.v3.proto.services import (
    mobile_device_constant_service_pb2 as mobile_device_constant_service_pb2,
)
from google.ads.google_ads.v3.services import (
    mobile_device_constant_service_client_config as mobile_device_constant_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    mobile_device_constant_service_grpc_transport as mobile_device_constant_service_grpc_transport,
)
from google.ads.google_ads.v3.types import MobileDeviceConstant

class MobileDeviceConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MobileDeviceConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MobileDeviceConstantServiceClient: ...
    @classmethod
    def mobile_device_constant_path(cls, mobile_device_constant: Any) -> str: ...
    transport: Union[
        mobile_device_constant_service_grpc_transport.MobileDeviceConstantServiceGrpcTransport,
        Callable[
            [Credentials, type],
            mobile_device_constant_service_grpc_transport.MobileDeviceConstantServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                mobile_device_constant_service_grpc_transport.MobileDeviceConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    mobile_device_constant_service_grpc_transport.MobileDeviceConstantServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_mobile_device_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MobileDeviceConstant: ...
