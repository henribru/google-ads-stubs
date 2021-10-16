import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import ad_group_extension_setting
from google.ads.googleads.v7.services.types import ad_group_extension_setting_service

class AdGroupExtensionSettingServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_ad_group_extension_setting(
        self,
    ) -> typing.Callable[
        [ad_group_extension_setting_service.GetAdGroupExtensionSettingRequest],
        ad_group_extension_setting.AdGroupExtensionSetting,
    ]: ...
    @property
    def mutate_ad_group_extension_settings(
        self,
    ) -> typing.Callable[
        [ad_group_extension_setting_service.MutateAdGroupExtensionSettingsRequest],
        ad_group_extension_setting_service.MutateAdGroupExtensionSettingsResponse,
    ]: ...
