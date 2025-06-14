from typing import Callable, Dict, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.enums.types import (
    data_link_status as gage_data_link_status,
)
from google.ads.googleads.v20.resources.types import data_link as gagr_data_link
from google.ads.googleads.v20.services.types import data_link_service

from .transports.base import DataLinkServiceTransport

__all__ = ["DataLinkServiceClient"]

class DataLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[DataLinkServiceTransport]: ...

class DataLinkServiceClient(metaclass=DataLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> DataLinkServiceTransport: ...
    @staticmethod
    def data_link_path(
        customer_id: str, product_link_id: str, data_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_data_link_path(path: str) -> dict[str, str]: ...
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
        transport: str
        | DataLinkServiceTransport
        | Callable[..., DataLinkServiceTransport]
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def create_data_link(
        self,
        request: data_link_service.CreateDataLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        data_link: gagr_data_link.DataLink | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> data_link_service.CreateDataLinkResponse: ...
    def remove_data_link(
        self,
        request: data_link_service.RemoveDataLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        resource_name: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> data_link_service.RemoveDataLinkResponse: ...
    def update_data_link(
        self,
        request: data_link_service.UpdateDataLinkRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        data_link_status: gage_data_link_status.DataLinkStatusEnum.DataLinkStatus
        | None = None,
        resource_name: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> data_link_service.UpdateDataLinkResponse: ...
    def __enter__(self) -> DataLinkServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
