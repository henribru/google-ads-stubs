import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.ad_schedule_view_service_grpc_transport import (
    AdScheduleViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.ad_schedule_view_pb2 import AdScheduleView

class AdScheduleViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdScheduleViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AdScheduleViewServiceClient: ...
    @classmethod
    def ad_schedule_view_path(cls, customer: Any, ad_schedule_view: Any) -> str: ...
    transport: Union[
        AdScheduleViewServiceGrpcTransport,
        Callable[[Credentials, type], AdScheduleViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AdScheduleViewServiceGrpcTransport,
                Callable[[Credentials, type], AdScheduleViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_ad_schedule_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdScheduleView: ...
