from typing import BinaryIO, Callable, Sequence

from google.api_core import gapic_v1, retry as retries
from google.auth import credentials as ga_credentials

from google.ads.googleads.v23.services.types import youtube_video_upload_service

from .rest_resumable_base import _BaseYouTubeVideoUploadServiceRestResumableTransport

__all__ = ["YouTubeVideoUploadServiceRestResumableTransport"]

class YouTubeVideoUploadServiceRestResumableInterceptor: ...

class YouTubeVideoUploadServiceRestResumableTransport(
    _BaseYouTubeVideoUploadServiceRestResumableTransport
):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        url_scheme: str = "https",
        interceptor: YouTubeVideoUploadServiceRestResumableInterceptor | None = None,
        api_audience: str | None = None,
        developer_token: str | None = None,
        login_customer_id: str | None = None,
        linked_customer_id: str | None = None,
        use_cloud_org_for_api_access: bool = False,
        **kwargs,
    ) -> None: ...
    def create_you_tube_video_upload_resumable(
        self,
        request: youtube_video_upload_service.CreateYouTubeVideoUploadRequest,
        *,
        stream: BinaryIO,
        rewind: bool = False,
        size: int | None = None,
        content_type: str | None = None,
        chunk_size: int | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.CreateYouTubeVideoUploadResponse: ...
