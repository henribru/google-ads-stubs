from google.ads.google_ads.v3.proto.services import ad_service_pb2 as ad_service_pb2
from google.ads.google_ads.v3.services import (
    ad_service_client_config as ad_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    ad_service_grpc_transport as ad_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.ad_service_grpc_transport import (
    AdServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.ad_pb2 import Ad
from google.ads.google_ads.v3.proto.services.ad_service_pb2 import (
    AdOperation,
    MutateAdsResponse,
)

class AdServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdServiceClient: ...
    @classmethod
    def ad_path(cls, customer: Any, ad: Any) -> str: ...
    transport: Union[
        AdServiceGrpcTransport, Callable[[Credentials, type], AdServiceGrpcTransport]
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdServiceGrpcTransport,
                Callable[[Credentials, type], AdServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Ad: ...
    def mutate_ads(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], AdOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAdsResponse: ...
