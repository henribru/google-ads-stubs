from google.ads.google_ads.v3.proto.services import (
    video_service_pb2 as video_service_pb2,
)
from google.ads.google_ads.v3.services import (
    video_service_client_config as video_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    video_service_grpc_transport as video_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.video_service_grpc_transport import (
    VideoServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.video_pb2 import Video

class VideoServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> VideoServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> VideoServiceClient: ...
    @classmethod
    def video_path(cls, customer: Any, video: Any) -> str: ...
    transport: Union[
        VideoServiceGrpcTransport,
        Callable[[Credentials, type], VideoServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                VideoServiceGrpcTransport,
                Callable[[Credentials, type], VideoServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_video(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Video: ...
