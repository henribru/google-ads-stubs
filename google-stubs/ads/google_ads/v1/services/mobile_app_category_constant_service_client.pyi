import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.mobile_app_category_constant_service_grpc_transport import (
    MobileAppCategoryConstantServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.mobile_app_category_constant_pb2 import (
    MobileAppCategoryConstant,
)

class MobileAppCategoryConstantServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MobileAppCategoryConstantServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MobileAppCategoryConstantServiceClient: ...
    @classmethod
    def mobile_app_category_constant_path(cls, mobile_app_category_constant: Any): ...
    transport: Union[
        MobileAppCategoryConstantServiceGrpcTransport,
        Callable[[Credentials, type], MobileAppCategoryConstantServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                MobileAppCategoryConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type], MobileAppCategoryConstantServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_mobile_app_category_constant(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MobileAppCategoryConstant: ...
