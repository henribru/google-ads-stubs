from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import customer_manager_link_service

from .transports.base import CustomerManagerLinkServiceTransport

class CustomerManagerLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[CustomerManagerLinkServiceTransport]: ...

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
    def __exit__(self, type, value, traceback) -> None: ...
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
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Optional[Union[str, CustomerManagerLinkServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_customer_manager_link(
        self,
        request: Optional[
            Union[customer_manager_link_service.MutateCustomerManagerLinkRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        operations: Optional[
            MutableSequence[customer_manager_link_service.CustomerManagerLinkOperation]
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_manager_link_service.MutateCustomerManagerLinkResponse: ...
    def move_manager_link(
        self,
        request: Optional[
            Union[customer_manager_link_service.MoveManagerLinkRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        previous_customer_manager_link: Optional[str] = ...,
        new_manager: Optional[str] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_manager_link_service.MoveManagerLinkResponse: ...
