import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.merchant_center_link_service_grpc_transport import (
    MerchantCenterLinkServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.merchant_center_link_pb2 import (
    MerchantCenterLink,
)
from google.ads.google_ads.v2.proto.services.merchant_center_link_service_pb2 import (
    MerchantCenterLinkOperation,
    MutateMerchantCenterLinkResponse,
    ListMerchantCenterLinksResponse,
)

class MerchantCenterLinkServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MerchantCenterLinkServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MerchantCenterLinkServiceClient: ...
    @classmethod
    def merchant_center_link_path(
        cls, customer: Any, merchant_center_link: Any
    ) -> str: ...
    transport: Union[
        MerchantCenterLinkServiceGrpcTransport,
        Callable[[Credentials, type], MerchantCenterLinkServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                MerchantCenterLinkServiceGrpcTransport,
                Callable[[Credentials, type], MerchantCenterLinkServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def list_merchant_center_links(
        self,
        customer_id: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListMerchantCenterLinksResponse: ...
    def get_merchant_center_link(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MerchantCenterLink: ...
    def mutate_merchant_center_link(
        self,
        customer_id: str,
        operation_: Union[Dict[str, Any], MerchantCenterLinkOperation],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateMerchantCenterLinkResponse: ...
