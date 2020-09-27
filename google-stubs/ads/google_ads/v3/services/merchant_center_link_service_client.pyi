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
    merchant_center_link_service_pb2 as merchant_center_link_service_pb2,
)
from google.ads.google_ads.v3.services import (
    merchant_center_link_service_client_config as merchant_center_link_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    merchant_center_link_service_grpc_transport as merchant_center_link_service_grpc_transport,
)
from google.ads.google_ads.v3.types import (
    ListMerchantCenterLinksResponse,
    MerchantCenterLink,
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
        merchant_center_link_service_grpc_transport.MerchantCenterLinkServiceGrpcTransport,
        Callable[
            [Credentials, type],
            merchant_center_link_service_grpc_transport.MerchantCenterLinkServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                merchant_center_link_service_grpc_transport.MerchantCenterLinkServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    merchant_center_link_service_grpc_transport.MerchantCenterLinkServiceGrpcTransport,
                ],
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
        operation_: Union[
            Dict[str, Any], merchant_center_link_service_pb2.MerchantCenterLinkOperation
        ],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> merchant_center_link_service_pb2.MutateMerchantCenterLinkResponse: ...
