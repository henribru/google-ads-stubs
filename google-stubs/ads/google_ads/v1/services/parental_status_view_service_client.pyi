import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.parental_status_view_service_grpc_transport import (
    ParentalStatusViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.parental_status_view_pb2 import (
    ParentalStatusView,
)

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
        cls, customer: Any, parental_status_view: Any
    ) -> str: ...
    transport: Union[
        ParentalStatusViewServiceGrpcTransport,
        Callable[[Credentials, type], ParentalStatusViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ParentalStatusViewServiceGrpcTransport,
                Callable[[Credentials, type], ParentalStatusViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_parental_status_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ParentalStatusView: ...
