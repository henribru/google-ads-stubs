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

from google.ads.google_ads.v5.proto.services import (
    dynamic_search_ads_search_term_view_service_pb2 as dynamic_search_ads_search_term_view_service_pb2,
)
from google.ads.google_ads.v5.services import (
    dynamic_search_ads_search_term_view_service_client_config as dynamic_search_ads_search_term_view_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    dynamic_search_ads_search_term_view_service_grpc_transport as dynamic_search_ads_search_term_view_service_grpc_transport,
)
from google.ads.google_ads.v5.types import DynamicSearchAdsSearchTermView

class DynamicSearchAdsSearchTermViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DynamicSearchAdsSearchTermViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DynamicSearchAdsSearchTermViewServiceClient: ...
    @classmethod
    def dynamic_search_ads_search_term_view_path(
        cls, customer: Any, dynamic_search_ads_search_term_view: Any
    ) -> str: ...
    transport: Union[
        dynamic_search_ads_search_term_view_service_grpc_transport.DynamicSearchAdsSearchTermViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            dynamic_search_ads_search_term_view_service_grpc_transport.DynamicSearchAdsSearchTermViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                dynamic_search_ads_search_term_view_service_grpc_transport.DynamicSearchAdsSearchTermViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    dynamic_search_ads_search_term_view_service_grpc_transport.DynamicSearchAdsSearchTermViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_dynamic_search_ads_search_term_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DynamicSearchAdsSearchTermView: ...
