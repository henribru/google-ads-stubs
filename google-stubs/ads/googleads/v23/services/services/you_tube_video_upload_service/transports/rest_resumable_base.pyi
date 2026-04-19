from typing import Any

from google.api_core import gapic_v1

from .base import YouTubeVideoUploadServiceTransport

__all__ = ["_BaseYouTubeVideoUploadServiceRestResumableTransport"]

class _BaseYouTubeVideoUploadServiceRestResumableTransport(
    YouTubeVideoUploadServiceTransport
):
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: Any | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        url_scheme: str = "https",
        api_audience: str | None = None,
    ) -> None: ...
    class _BaseCreateYouTubeVideoUploadRequest:
        def __hash__(self): ...
