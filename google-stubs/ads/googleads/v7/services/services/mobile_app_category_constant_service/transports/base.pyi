import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import mobile_app_category_constant
from google.ads.googleads.v7.services.types import mobile_app_category_constant_service

class MobileAppCategoryConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_mobile_app_category_constant(
        self,
    ) -> typing.Callable[
        [mobile_app_category_constant_service.GetMobileAppCategoryConstantRequest],
        mobile_app_category_constant.MobileAppCategoryConstant,
    ]: ...