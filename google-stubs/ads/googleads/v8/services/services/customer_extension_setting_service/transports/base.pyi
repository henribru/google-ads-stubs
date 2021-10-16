import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import customer_extension_setting
from google.ads.googleads.v8.services.types import customer_extension_setting_service

class CustomerExtensionSettingServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_extension_setting(
        self,
    ) -> typing.Callable[
        [customer_extension_setting_service.GetCustomerExtensionSettingRequest],
        customer_extension_setting.CustomerExtensionSetting,
    ]: ...
    @property
    def mutate_customer_extension_settings(
        self,
    ) -> typing.Callable[
        [customer_extension_setting_service.MutateCustomerExtensionSettingsRequest],
        customer_extension_setting_service.MutateCustomerExtensionSettingsResponse,
    ]: ...
