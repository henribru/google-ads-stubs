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
    group_placement_view_service_pb2 as group_placement_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    group_placement_view_service_client_config as group_placement_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    group_placement_view_service_grpc_transport as group_placement_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import GroupPlacementView

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
        group_placement_view_service_grpc_transport.GroupPlacementViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            group_placement_view_service_grpc_transport.GroupPlacementViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                group_placement_view_service_grpc_transport.GroupPlacementViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    group_placement_view_service_grpc_transport.GroupPlacementViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_group_placement_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GroupPlacementView: ...
