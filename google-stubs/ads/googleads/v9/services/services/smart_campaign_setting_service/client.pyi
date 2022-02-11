from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import smart_campaign_setting
from google.ads.googleads.v9.services.types import smart_campaign_setting_service

from .transports.base import SmartCampaignSettingServiceTransport

class SmartCampaignSettingServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[SmartCampaignSettingServiceTransport]: ...

class SmartCampaignSettingServiceClient(
    metaclass=SmartCampaignSettingServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> SmartCampaignSettingServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def smart_campaign_setting_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_smart_campaign_setting_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[str, SmartCampaignSettingServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_smart_campaign_setting(
        self,
        request: Union[
            smart_campaign_setting_service.GetSmartCampaignSettingRequest, dict
        ] = ...,
        *,
        resource_name: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> smart_campaign_setting.SmartCampaignSetting: ...
    def mutate_smart_campaign_settings(
        self,
        request: Union[
            smart_campaign_setting_service.MutateSmartCampaignSettingsRequest, dict
        ] = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            smart_campaign_setting_service.SmartCampaignSettingOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> smart_campaign_setting_service.MutateSmartCampaignSettingsResponse: ...