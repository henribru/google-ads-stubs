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
    ad_schedule_view_service_pb2 as ad_schedule_view_service_pb2,
)
from google.ads.google_ads.v6.services import (
    ad_schedule_view_service_client_config as ad_schedule_view_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    ad_schedule_view_service_grpc_transport as ad_schedule_view_service_grpc_transport,
)
from google.ads.google_ads.v6.types import AdScheduleView

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
        ad_schedule_view_service_grpc_transport.AdScheduleViewServiceGrpcTransport,
        Callable[
            [Credentials, type],
            ad_schedule_view_service_grpc_transport.AdScheduleViewServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                ad_schedule_view_service_grpc_transport.AdScheduleViewServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    ad_schedule_view_service_grpc_transport.AdScheduleViewServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_ad_schedule_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AdScheduleView: ...
