from google.ads.google_ads.v3.proto.services import (
    product_group_view_service_pb2 as product_group_view_service_pb2,
)
from google.ads.google_ads.v3.services import (
    product_group_view_service_client_config as product_group_view_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    product_group_view_service_grpc_transport as product_group_view_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.product_group_view_service_grpc_transport import (
    ProductGroupViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.product_group_view_pb2 import (
    ProductGroupView,
)

class ProductGroupViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ProductGroupViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ProductGroupViewServiceClient: ...
    @classmethod
    def product_group_view_path(cls, customer: Any, product_group_view: Any) -> str: ...
    transport: Union[
        ProductGroupViewServiceGrpcTransport,
        Callable[[Credentials, type], ProductGroupViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ProductGroupViewServiceGrpcTransport,
                Callable[[Credentials, type], ProductGroupViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_product_group_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ProductGroupView: ...
