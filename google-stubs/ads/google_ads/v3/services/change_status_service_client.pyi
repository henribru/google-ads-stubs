from google.ads.google_ads.v3.proto.services import (
    change_status_service_pb2 as change_status_service_pb2,
)
from google.ads.google_ads.v3.services import (
    change_status_service_client_config as change_status_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    change_status_service_grpc_transport as change_status_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.change_status_service_grpc_transport import (
    ChangeStatusServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.change_status_pb2 import ChangeStatus

class ChangeStatusServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ChangeStatusServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> ChangeStatusServiceClient: ...
    @classmethod
    def change_status_path(cls, customer: Any, change_status: Any) -> str: ...
    transport: Union[
        ChangeStatusServiceGrpcTransport,
        Callable[[Credentials, type], ChangeStatusServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ChangeStatusServiceGrpcTransport,
                Callable[[Credentials, type], ChangeStatusServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_change_status(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ChangeStatus: ...
