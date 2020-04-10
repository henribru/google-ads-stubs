from google.ads.google_ads.v3.proto.services import (
    media_file_service_pb2 as media_file_service_pb2,
)
from google.ads.google_ads.v3.services import (
    media_file_service_client_config as media_file_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    media_file_service_grpc_transport as media_file_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.media_file_service_grpc_transport import (
    MediaFileServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.media_file_pb2 import MediaFile
from google.ads.google_ads.v3.proto.services.media_file_service_pb2 import (
    MediaFileOperation,
    MutateMediaFilesResponse,
)

class MediaFileServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MediaFileServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MediaFileServiceClient: ...
    @classmethod
    def media_file_path(cls, customer: Any, media_file: Any) -> str: ...
    transport: Union[
        MediaFileServiceGrpcTransport,
        Callable[[Credentials, type], MediaFileServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                MediaFileServiceGrpcTransport,
                Callable[[Credentials, type], MediaFileServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_media_file(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MediaFile: ...
    def mutate_media_files(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], MediaFileOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateMediaFilesResponse: ...
