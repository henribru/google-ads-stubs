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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v5.proto.services import (
    media_file_service_pb2 as media_file_service_pb2,
)
from google.ads.google_ads.v5.services import (
    media_file_service_client_config as media_file_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    media_file_service_grpc_transport as media_file_service_grpc_transport,
)
from google.ads.google_ads.v5.types import MediaFile, ResponseContentTypeEnum

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
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
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
        response_content_type: Optional[
            ResponseContentTypeEnum.ResponseContentType.V
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> media_file_service_pb2.MutateMediaFilesResponse: ...
