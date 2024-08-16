import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.services.types import shareable_preview_service

__all__ = ["ShareablePreviewServiceTransport"]

class ShareablePreviewServiceTransport(abc.ABC):
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
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def generate_shareable_previews(
        self,
    ) -> Callable[
        [shareable_preview_service.GenerateShareablePreviewsRequest],
        shareable_preview_service.GenerateShareablePreviewsResponse
        | Awaitable[shareable_preview_service.GenerateShareablePreviewsResponse],
    ]: ...
