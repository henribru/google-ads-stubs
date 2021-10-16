import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import mobile_device_constant
from google.ads.googleads.v7.services.types import mobile_device_constant_service

class MobileDeviceConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_mobile_device_constant(
        self,
    ) -> typing.Callable[
        [mobile_device_constant_service.GetMobileDeviceConstantRequest],
        mobile_device_constant.MobileDeviceConstant,
    ]: ...
