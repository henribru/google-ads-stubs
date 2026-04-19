from typing import BinaryIO, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from google.protobuf import field_mask_pb2

from google.ads.googleads.v23.resources.types import youtube_video_upload
from google.ads.googleads.v23.services.types import youtube_video_upload_service

from .transports.base import YouTubeVideoUploadServiceTransport

__all__ = ["YouTubeVideoUploadServiceAsyncClient"]

class YouTubeVideoUploadServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    you_tube_video_upload_path: Incomplete
    parse_you_tube_video_upload_path: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: ClientOptions | None = None
    ): ...
    @property
    def transport(self) -> YouTubeVideoUploadServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        developer_token: str | None = None,
        login_customer_id: str | None = None,
        linked_customer_id: str | None = None,
        use_cloud_org_for_api_access: bool = False,
        transport: str
        | YouTubeVideoUploadServiceTransport
        | Callable[..., YouTubeVideoUploadServiceTransport]
        | None = "grpc_asyncio",
        client_options: ClientOptions | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    async def create_you_tube_video_upload(
        self,
        request: youtube_video_upload_service.CreateYouTubeVideoUploadRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        you_tube_video_upload: youtube_video_upload.YouTubeVideoUpload | None = None,
        stream: BinaryIO,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.CreateYouTubeVideoUploadResponse: ...
    async def update_you_tube_video_upload(
        self,
        request: youtube_video_upload_service.UpdateYouTubeVideoUploadRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        you_tube_video_upload: youtube_video_upload.YouTubeVideoUpload | None = None,
        update_mask: field_mask_pb2.FieldMask | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.UpdateYouTubeVideoUploadResponse: ...
    async def remove_you_tube_video_upload(
        self,
        request: youtube_video_upload_service.RemoveYouTubeVideoUploadRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        retry: retries.AsyncRetry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.RemoveYouTubeVideoUploadResponse: ...
    async def __aenter__(self) -> YouTubeVideoUploadServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
