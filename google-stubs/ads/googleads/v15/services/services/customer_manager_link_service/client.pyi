import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import customer_manager_link_service

from .transports.base import CustomerManagerLinkServiceTransport

__all__ = ["CustomerManagerLinkServiceClient"]

class CustomerManagerLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[CustomerManagerLinkServiceTransport]: ...

class CustomerManagerLinkServiceClient(metaclass=CustomerManagerLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> CustomerManagerLinkServiceTransport: ...
    def __enter__(self) -> CustomerManagerLinkServiceClient: ...
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
    def customer_manager_link_path(
        customer_id: str, manager_customer_id: str, manager_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_manager_link_path(path: str) -> dict[str, str]: ...
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
        transport: str | CustomerManagerLinkServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_customer_manager_link(
        self,
        request: customer_manager_link_service.MutateCustomerManagerLinkRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            customer_manager_link_service.CustomerManagerLinkOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> customer_manager_link_service.MutateCustomerManagerLinkResponse: ...
    def move_manager_link(
        self,
        request: customer_manager_link_service.MoveManagerLinkRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        previous_customer_manager_link: str | None = None,
        new_manager: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> customer_manager_link_service.MoveManagerLinkResponse: ...
