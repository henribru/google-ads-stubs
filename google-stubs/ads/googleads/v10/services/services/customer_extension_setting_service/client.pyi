from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import customer_extension_setting_service

from .transports.base import CustomerExtensionSettingServiceTransport

class CustomerExtensionSettingServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CustomerExtensionSettingServiceTransport]: ...

class CustomerExtensionSettingServiceClient(
    metaclass=CustomerExtensionSettingServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> CustomerExtensionSettingServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def customer_extension_setting_path(
        customer_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_customer_extension_setting_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def extension_feed_item_path(customer_id: str, feed_item_id: str) -> str: ...
    @staticmethod
    def parse_extension_feed_item_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, CustomerExtensionSettingServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_customer_extension_settings(
        self,
        request: Union[
            customer_extension_setting_service.MutateCustomerExtensionSettingsRequest,
            dict,
        ] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            customer_extension_setting_service.CustomerExtensionSettingOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_extension_setting_service.MutateCustomerExtensionSettingsResponse: ...
