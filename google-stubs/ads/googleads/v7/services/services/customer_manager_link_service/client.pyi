from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_manager_link
from google.ads.googleads.v7.services.types import customer_manager_link_service

from .transports.base import CustomerManagerLinkServiceTransport

class CustomerManagerLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CustomerManagerLinkServiceTransport]: ...

class CustomerManagerLinkServiceClient(metaclass=CustomerManagerLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CustomerManagerLinkServiceTransport: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_manager_link_path(
        customer_id: str, manager_customer_id: str, manager_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_manager_link_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, CustomerManagerLinkServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_customer_manager_link(
        self,
        request: customer_manager_link_service.GetCustomerManagerLinkRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_manager_link.CustomerManagerLink: ...
    def mutate_customer_manager_link(
        self,
        request: customer_manager_link_service.MutateCustomerManagerLinkRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            customer_manager_link_service.CustomerManagerLinkOperation
        ] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_manager_link_service.MutateCustomerManagerLinkResponse: ...
    def move_manager_link(
        self,
        request: customer_manager_link_service.MoveManagerLinkRequest = ...,
        *,
        customer_id: str = ...,
        previous_customer_manager_link: str = ...,
        new_manager: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_manager_link_service.MoveManagerLinkResponse: ...
