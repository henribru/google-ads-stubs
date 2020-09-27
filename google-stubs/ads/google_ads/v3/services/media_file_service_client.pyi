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

from google.ads.google_ads.v3.proto.services import (
    media_file_service_pb2 as media_file_service_pb2,
)
from google.ads.google_ads.v3.services import (
    media_file_service_client_config as media_file_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    media_file_service_grpc_transport as media_file_service_grpc_transport,
)
from google.ads.google_ads.v3.types import MediaFile

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
        media_file_service_grpc_transport.MediaFileServiceGrpcTransport,
        Callable[
            [Credentials, type],
            media_file_service_grpc_transport.MediaFileServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                media_file_service_grpc_transport.MediaFileServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    media_file_service_grpc_transport.MediaFileServiceGrpcTransport,
                ],
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
        operations: List[
            Union[Dict[str, Any], media_file_service_pb2.MediaFileOperation]
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> media_file_service_pb2.MutateMediaFilesResponse: ...
