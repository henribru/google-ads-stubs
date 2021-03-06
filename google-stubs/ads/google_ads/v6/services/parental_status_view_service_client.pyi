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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v6.proto.services import (
    parental_status_view_service_pb2 as parental_status_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    parental_status_view_service_client_config as parental_status_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    parental_status_view_service_grpc_transport as parental_status_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import ParentalStatusView

class ParentalStatusViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ParentalStatusViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ParentalStatusViewServiceClient: ...
    @classmethod
    def parental_status_view_path(
        cls, customer_id: Any, ad_group_id: Any, criterion_id: Any
    ) -> str: ...
    transport: Union[
        parental_status_view_service_grpc_transport.ParentalStatusViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            parental_status_view_service_grpc_transport.ParentalStatusViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                parental_status_view_service_grpc_transport.ParentalStatusViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    parental_status_view_service_grpc_transport.ParentalStatusViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_parental_status_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ParentalStatusView: ...
