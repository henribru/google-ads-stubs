from google.ads.google_ads.v3.proto.services import (
    domain_category_service_pb2 as domain_category_service_pb2,
)
from google.ads.google_ads.v3.services import (
    domain_category_service_client_config as domain_category_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    domain_category_service_grpc_transport as domain_category_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.domain_category_service_grpc_transport import (
    DomainCategoryServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.domain_category_pb2 import DomainCategory

class DomainCategoryServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DomainCategoryServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DomainCategoryServiceClient: ...
    @classmethod
    def domain_category_path(cls, customer: Any, domain_category: Any) -> str: ...
    transport: Union[
        DomainCategoryServiceGrpcTransport,
        Callable[[Credentials, type], DomainCategoryServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                DomainCategoryServiceGrpcTransport,
                Callable[[Credentials, type], DomainCategoryServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_domain_category(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DomainCategory: ...
