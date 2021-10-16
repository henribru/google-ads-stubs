import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import carrier_constant
from google.ads.googleads.v7.services.types import carrier_constant_service

class CarrierConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_carrier_constant(
        self,
    ) -> typing.Callable[
        [carrier_constant_service.GetCarrierConstantRequest],
        carrier_constant.CarrierConstant,
    ]: ...
