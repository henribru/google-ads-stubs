from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.resources.types import account_link as gagr_account_link
from google.ads.googleads.v14.services.types import account_link_service

from .transports.base import AccountLinkServiceTransport

class AccountLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[AccountLinkServiceTransport]: ...

class AccountLinkServiceClient(metaclass=AccountLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AccountLinkServiceTransport: ...
    def __enter__(self) -> AccountLinkServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def account_link_path(customer_id: str, account_link_id: str) -> str: ...
    @staticmethod
    def parse_account_link_path(path: str) -> Dict[str, str]: ...
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
        transport: Optional[Union[str, AccountLinkServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def create_account_link(
        self,
        request: Optional[
            Union[account_link_service.CreateAccountLinkRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        account_link: Optional[gagr_account_link.AccountLink] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> account_link_service.CreateAccountLinkResponse: ...
    def mutate_account_link(
        self,
        request: Optional[
            Union[account_link_service.MutateAccountLinkRequest, dict]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        operation: Optional[account_link_service.AccountLinkOperation] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> account_link_service.MutateAccountLinkResponse: ...
