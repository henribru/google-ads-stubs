import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.age_range_view_service_grpc_transport import (
    AgeRangeViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.age_range_view_pb2 import AgeRangeView

class AgeRangeViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AgeRangeViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AgeRangeViewServiceClient: ...
    @classmethod
    def age_range_view_path(cls, customer: Any, age_range_view: Any) -> str: ...
    transport: Union[
        AgeRangeViewServiceGrpcTransport,
        Callable[[Credentials, type], AgeRangeViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AgeRangeViewServiceGrpcTransport,
                Callable[[Credentials, type], AgeRangeViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_age_range_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AgeRangeView: ...
