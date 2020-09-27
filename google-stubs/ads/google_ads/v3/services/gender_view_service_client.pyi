from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v3.proto.resources.gender_view_pb2 import GenderView
from google.ads.google_ads.v3.proto.services import (
    gender_view_service_pb2 as gender_view_service_pb2,
)
from google.ads.google_ads.v3.services import (
    gender_view_service_client_config as gender_view_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    gender_view_service_grpc_transport as gender_view_service_grpc_transport,
)
from google.ads.google_ads.v3.services.transports.gender_view_service_grpc_transport import (
    GenderViewServiceGrpcTransport,
)

class GenderViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GenderViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GenderViewServiceClient: ...
    @classmethod
    def gender_view_path(cls, customer: Any, gender_view: Any) -> str: ...
    transport: Union[
        GenderViewServiceGrpcTransport,
        Callable[[Credentials, type], GenderViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                GenderViewServiceGrpcTransport,
                Callable[[Credentials, type], GenderViewServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_gender_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> GenderView: ...
