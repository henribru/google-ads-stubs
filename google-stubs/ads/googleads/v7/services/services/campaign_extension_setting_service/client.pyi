from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_extension_setting
from google.ads.googleads.v7.services.types import campaign_extension_setting_service

from .transports.base import CampaignExtensionSettingServiceTransport

class CampaignExtensionSettingServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CampaignExtensionSettingServiceTransport]: ...

class CampaignExtensionSettingServiceClient(
    metaclass=CampaignExtensionSettingServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CampaignExtensionSettingServiceTransport: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_extension_setting_path(
        customer_id: str, campaign_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_extension_setting_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, CampaignExtensionSettingServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_campaign_extension_setting(
        self,
        request: campaign_extension_setting_service.GetCampaignExtensionSettingRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_extension_setting.CampaignExtensionSetting: ...
    def mutate_campaign_extension_settings(
        self,
        request: campaign_extension_setting_service.MutateCampaignExtensionSettingsRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[
            campaign_extension_setting_service.CampaignExtensionSettingOperation
        ] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> campaign_extension_setting_service.MutateCampaignExtensionSettingsResponse: ...
