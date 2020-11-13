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

from google.ads.google_ads.v6.proto.services import (
    detail_placement_view_service_pb2 as detail_placement_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    detail_placement_view_service_client_config as detail_placement_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    detail_placement_view_service_grpc_transport as detail_placement_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import DetailPlacementView

class DetailPlacementViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DetailPlacementViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> DetailPlacementViewServiceClient: ...
    @classmethod
    def detail_placement_view_path(
        cls, customer: Any, detail_placement_view: Any
    ) -> str: ...
    transport: Union[
        detail_placement_view_service_grpc_transport.DetailPlacementViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            detail_placement_view_service_grpc_transport.DetailPlacementViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                detail_placement_view_service_grpc_transport.DetailPlacementViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    detail_placement_view_service_grpc_transport.DetailPlacementViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_detail_placement_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DetailPlacementView: ...
