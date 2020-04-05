import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.detail_placement_view_service_grpc_transport import (
    DetailPlacementViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.detail_placement_view_pb2 import (
    DetailPlacementView,
)

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
        DetailPlacementViewServiceGrpcTransport,
        Callable[[Credentials, type], DetailPlacementViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                DetailPlacementViewServiceGrpcTransport,
                Callable[[Credentials, type], DetailPlacementViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_detail_placement_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> DetailPlacementView: ...
