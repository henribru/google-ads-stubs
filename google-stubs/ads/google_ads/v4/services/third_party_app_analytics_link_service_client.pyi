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

from google.ads.google_ads.v4.proto.services import (
    third_party_app_analytics_link_service_pb2 as third_party_app_analytics_link_service_pb2,
)
from google.ads.google_ads.v4.services import (
    third_party_app_analytics_link_service_client_config as third_party_app_analytics_link_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    third_party_app_analytics_link_service_grpc_transport as third_party_app_analytics_link_service_grpc_transport,
)
from google.ads.google_ads.v4.types import ThirdPartyAppAnalyticsLink

class ThirdPartyAppAnalyticsLinkServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ThirdPartyAppAnalyticsLinkServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ThirdPartyAppAnalyticsLinkServiceClient: ...
    @classmethod
    def third_party_app_analytics_link_path(
        cls, customer: Any, third_party_app_analytics_link: Any
    ) -> str: ...
    transport: Union[
        third_party_app_analytics_link_service_grpc_transport.ThirdPartyAppAnalyticsLinkServiceGrpcTransport,
        Callable[
            [Credentials, type],
            third_party_app_analytics_link_service_grpc_transport.ThirdPartyAppAnalyticsLinkServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                third_party_app_analytics_link_service_grpc_transport.ThirdPartyAppAnalyticsLinkServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    third_party_app_analytics_link_service_grpc_transport.ThirdPartyAppAnalyticsLinkServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_third_party_app_analytics_link(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ThirdPartyAppAnalyticsLink: ...
