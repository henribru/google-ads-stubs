import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v23.services.types import youtube_video_upload_service

__all__ = ["YouTubeVideoUploadServiceTransport"]

class YouTubeVideoUploadServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def create_you_tube_video_upload(
        self,
    ) -> Callable[
        [youtube_video_upload_service.CreateYouTubeVideoUploadRequest],
        youtube_video_upload_service.CreateYouTubeVideoUploadResponse
        | Awaitable[youtube_video_upload_service.CreateYouTubeVideoUploadResponse],
    ]: ...
    @property
    def update_you_tube_video_upload(
        self,
    ) -> Callable[
        [youtube_video_upload_service.UpdateYouTubeVideoUploadRequest],
        youtube_video_upload_service.UpdateYouTubeVideoUploadResponse
        | Awaitable[youtube_video_upload_service.UpdateYouTubeVideoUploadResponse],
    ]: ...
    @property
    def remove_you_tube_video_upload(
        self,
    ) -> Callable[
        [youtube_video_upload_service.RemoveYouTubeVideoUploadRequest],
        youtube_video_upload_service.RemoveYouTubeVideoUploadResponse
        | Awaitable[youtube_video_upload_service.RemoveYouTubeVideoUploadResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
