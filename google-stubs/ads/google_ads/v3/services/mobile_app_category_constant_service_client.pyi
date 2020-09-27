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
    mobile_app_category_constant_service_pb2 as mobile_app_category_constant_service_pb2,
)
from google.ads.google_ads.v3.services import (
    mobile_app_category_constant_service_client_config as mobile_app_category_constant_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    mobile_app_category_constant_service_grpc_transport as mobile_app_category_constant_service_grpc_transport,
)
from google.ads.google_ads.v3.types import MobileAppCategoryConstant

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
    def mobile_app_category_constant_path(
        cls, mobile_app_category_constant: Any
    ) -> str: ...
    transport: Union[
        mobile_app_category_constant_service_grpc_transport.MobileAppCategoryConstantServiceGrpcTransport,
        Callable[
            [Credentials, type],
            mobile_app_category_constant_service_grpc_transport.MobileAppCategoryConstantServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                mobile_app_category_constant_service_grpc_transport.MobileAppCategoryConstantServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    mobile_app_category_constant_service_grpc_transport.MobileAppCategoryConstantServiceGrpcTransport,
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
