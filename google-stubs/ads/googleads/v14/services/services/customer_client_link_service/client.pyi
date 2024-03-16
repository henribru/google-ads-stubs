import types
from typing import Dict, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import customer_client_link_service

from .transports.base import CustomerClientLinkServiceTransport

__all__ = ["CustomerClientLinkServiceClient"]

class CustomerClientLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[CustomerClientLinkServiceTransport]: ...

class CustomerClientLinkServiceClient(metaclass=CustomerClientLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> CustomerClientLinkServiceTransport: ...
    def __enter__(self) -> CustomerClientLinkServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_client_link_path(
        customer_id: str, client_customer_id: str, manager_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_client_link_path(path: str) -> dict[str, str]: ...
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
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str | CustomerClientLinkServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_customer_client_link(
        self,
        request: customer_client_link_service.MutateCustomerClientLinkRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operation: customer_client_link_service.CustomerClientLinkOperation
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> customer_client_link_service.MutateCustomerClientLinkResponse: ...
