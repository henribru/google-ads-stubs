import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.services.types import conversion_upload_service

class ConversionUploadServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def upload_click_conversions(
        self,
    ) -> typing.Callable[
        [conversion_upload_service.UploadClickConversionsRequest],
        conversion_upload_service.UploadClickConversionsResponse,
    ]: ...
    @property
    def upload_call_conversions(
        self,
    ) -> typing.Callable[
        [conversion_upload_service.UploadCallConversionsRequest],
        conversion_upload_service.UploadCallConversionsResponse,
    ]: ...
