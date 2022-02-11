import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import currency_constant
from google.ads.googleads.v9.services.types import currency_constant_service

class CurrencyConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_currency_constant(
        self,
    ) -> typing.Callable[
        [currency_constant_service.GetCurrencyConstantRequest],
        currency_constant.CurrencyConstant,
    ]: ...
