import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.group_placement_view_service_grpc_transport import (
    GroupPlacementViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.group_placement_view_pb2 import (
    GroupPlacementView,
)

class GroupPlacementViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GroupPlacementViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GroupPlacementViewServiceClient: ...
    @classmethod
    def group_placement_view_path(
        cls, customer: Any, group_placement_view: Any
    ) -> str: ...
    transport: Union[
        GroupPlacementViewServiceGrpcTransport,
        Callable[[Credentials, type], GroupPlacementViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                GroupPlacementViewServiceGrpcTransport,
                Callable[[Credentials, type], GroupPlacementViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_group_placement_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GroupPlacementView: ...
