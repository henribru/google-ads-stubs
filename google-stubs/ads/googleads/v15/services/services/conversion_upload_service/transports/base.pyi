import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import conversion_upload_service

class ConversionUploadServiceTransport(abc.ABC):
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
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def upload_click_conversions(
        self,
    ) -> Callable[
        [conversion_upload_service.UploadClickConversionsRequest],
        conversion_upload_service.UploadClickConversionsResponse
        | Awaitable[conversion_upload_service.UploadClickConversionsResponse],
    ]: ...
    @property
    def upload_call_conversions(
        self,
    ) -> Callable[
        [conversion_upload_service.UploadCallConversionsRequest],
        conversion_upload_service.UploadCallConversionsResponse
        | Awaitable[conversion_upload_service.UploadCallConversionsResponse],
    ]: ...
