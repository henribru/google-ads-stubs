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
    click_view_service_pb2 as click_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    click_view_service_client_config as click_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    click_view_service_grpc_transport as click_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import ClickView

class ClickViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ClickViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ClickViewServiceClient: ...
    @classmethod
    def click_view_path(cls, customer_id: Any, date: Any, gclid: Any) -> str: ...
    transport: Union[
        click_view_service_grpc_transport.ClickViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            click_view_service_grpc_transport.ClickViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                click_view_service_grpc_transport.ClickViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    click_view_service_grpc_transport.ClickViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_click_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ClickView: ...
