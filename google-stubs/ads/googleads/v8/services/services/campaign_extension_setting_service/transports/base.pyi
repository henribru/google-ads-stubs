import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import campaign_extension_setting
from google.ads.googleads.v8.services.types import campaign_extension_setting_service

class CampaignExtensionSettingServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_extension_setting(
        self,
    ) -> typing.Callable[
        [campaign_extension_setting_service.GetCampaignExtensionSettingRequest],
        campaign_extension_setting.CampaignExtensionSetting,
    ]: ...
    @property
    def mutate_campaign_extension_settings(
        self,
    ) -> typing.Callable[
        [campaign_extension_setting_service.MutateCampaignExtensionSettingsRequest],
        campaign_extension_setting_service.MutateCampaignExtensionSettingsResponse,
    ]: ...
