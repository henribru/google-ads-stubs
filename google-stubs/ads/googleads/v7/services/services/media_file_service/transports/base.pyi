import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import media_file
from google.ads.googleads.v7.services.types import media_file_service

class MediaFileServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_media_file(
        self,
    ) -> typing.Callable[
        [media_file_service.GetMediaFileRequest], media_file.MediaFile
    ]: ...
    @property
    def mutate_media_files(
        self,
    ) -> typing.Callable[
        [media_file_service.MutateMediaFilesRequest],
        media_file_service.MutateMediaFilesResponse,
    ]: ...
