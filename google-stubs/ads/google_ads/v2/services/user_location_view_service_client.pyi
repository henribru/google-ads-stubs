from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore

from google.ads.google_ads.v2.proto.resources.user_location_view_pb2 import (
    UserLocationView,
)
from google.ads.google_ads.v2.services.transports.user_location_view_service_grpc_transport import (
    UserLocationViewServiceGrpcTransport,
)

class UserLocationViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserLocationViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserLocationViewServiceClient: ...
    @classmethod
    def user_location_view_path(cls, customer: Any, user_location_view: Any) -> str: ...
    transport: Union[
        UserLocationViewServiceGrpcTransport,
        Callable[[Credentials, type], UserLocationViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                UserLocationViewServiceGrpcTransport,
                Callable[[Credentials, type], UserLocationViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_user_location_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UserLocationView: ...
