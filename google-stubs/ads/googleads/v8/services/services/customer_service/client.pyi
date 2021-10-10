from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import customer
from google.ads.googleads.v8.services.types import customer_service

from .transports.base import CustomerServiceTransport

class CustomerServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CustomerServiceTransport]: ...

class CustomerServiceClient(metaclass=CustomerServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CustomerServiceTransport: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, CustomerServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_customer(
        self,
        request: customer_service.GetCustomerRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer.Customer: ...
    def mutate_customer(
        self,
        request: customer_service.MutateCustomerRequest = ...,
        *,
        customer_id: str = ...,
        operation: customer_service.CustomerOperation = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_service.MutateCustomerResponse: ...
    def list_accessible_customers(
        self,
        request: customer_service.ListAccessibleCustomersRequest = ...,
        *,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_service.ListAccessibleCustomersResponse: ...
    def create_customer_client(
        self,
        request: customer_service.CreateCustomerClientRequest = ...,
        *,
        customer_id: str = ...,
        customer_client: customer.Customer = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_service.CreateCustomerClientResponse: ...
