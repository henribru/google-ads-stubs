from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import ad_group_extension_setting_service

from .transports.base import AdGroupExtensionSettingServiceTransport

class AdGroupExtensionSettingServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[AdGroupExtensionSettingServiceTransport]: ...

class AdGroupExtensionSettingServiceClient(
    metaclass=AdGroupExtensionSettingServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> AdGroupExtensionSettingServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_extension_setting_path(
        customer_id: str, ad_group_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_extension_setting_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, AdGroupExtensionSettingServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_ad_group_extension_settings(
        self,
        request: Union[
            ad_group_extension_setting_service.MutateAdGroupExtensionSettingsRequest,
            dict,
        ] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            ad_group_extension_setting_service.AdGroupExtensionSettingOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> ad_group_extension_setting_service.MutateAdGroupExtensionSettingsResponse: ...
