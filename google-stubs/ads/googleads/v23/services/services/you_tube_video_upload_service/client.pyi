import types
from typing import BinaryIO, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials
from google.protobuf import field_mask_pb2

from google.ads.googleads.v23.resources.types import youtube_video_upload
from google.ads.googleads.v23.services.types import youtube_video_upload_service

from .transports.base import YouTubeVideoUploadServiceTransport

__all__ = ["YouTubeVideoUploadServiceClient"]

class YouTubeVideoUploadServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[YouTubeVideoUploadServiceTransport]: ...

class YouTubeVideoUploadServiceClient(metaclass=YouTubeVideoUploadServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> YouTubeVideoUploadServiceTransport: ...
    @staticmethod
    def you_tube_video_upload_path(customer_id: str, video_upload_id: str) -> str: ...
    @staticmethod
    def parse_you_tube_video_upload_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> dict[str, str]: ...
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: client_options_lib.ClientOptions | None = None
    ): ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
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
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def create_you_tube_video_upload(
        self,
        request: youtube_video_upload_service.CreateYouTubeVideoUploadRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        you_tube_video_upload: youtube_video_upload.YouTubeVideoUpload | None = None,
        stream: BinaryIO,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.CreateYouTubeVideoUploadResponse: ...
    def update_you_tube_video_upload(
        self,
        request: youtube_video_upload_service.UpdateYouTubeVideoUploadRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        you_tube_video_upload: youtube_video_upload.YouTubeVideoUpload | None = None,
        update_mask: field_mask_pb2.FieldMask | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.UpdateYouTubeVideoUploadResponse: ...
    def remove_you_tube_video_upload(
        self,
        request: youtube_video_upload_service.RemoveYouTubeVideoUploadRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault | None = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> youtube_video_upload_service.RemoveYouTubeVideoUploadResponse: ...
    def __enter__(self) -> YouTubeVideoUploadServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
