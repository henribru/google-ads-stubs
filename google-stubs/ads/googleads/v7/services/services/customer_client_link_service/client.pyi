from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_client_link
from google.ads.googleads.v7.services.types import customer_client_link_service

from .transports.base import CustomerClientLinkServiceTransport

class CustomerClientLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CustomerClientLinkServiceTransport]: ...

class CustomerClientLinkServiceClient(metaclass=CustomerClientLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CustomerClientLinkServiceTransport: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_client_link_path(
        customer_id: str, client_customer_id: str, manager_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_client_link_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, CustomerClientLinkServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_customer_client_link(
        self,
        request: customer_client_link_service.GetCustomerClientLinkRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_client_link.CustomerClientLink: ...
    def mutate_customer_client_link(
        self,
        request: customer_client_link_service.MutateCustomerClientLinkRequest = ...,
        *,
        customer_id: str = ...,
        operation: customer_client_link_service.CustomerClientLinkOperation = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_client_link_service.MutateCustomerClientLinkResponse: ...
