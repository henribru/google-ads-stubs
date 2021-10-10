import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import smart_campaign_setting
from google.ads.googleads.v8.services.types import smart_campaign_setting_service

class SmartCampaignSettingServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_smart_campaign_setting(
        self,
    ) -> typing.Callable[
        [smart_campaign_setting_service.GetSmartCampaignSettingRequest],
        smart_campaign_setting.SmartCampaignSetting,
    ]: ...
    @property
    def mutate_smart_campaign_settings(
        self,
    ) -> typing.Callable[
        [smart_campaign_setting_service.MutateSmartCampaignSettingsRequest],
        smart_campaign_setting_service.MutateSmartCampaignSettingsResponse,
    ]: ...
