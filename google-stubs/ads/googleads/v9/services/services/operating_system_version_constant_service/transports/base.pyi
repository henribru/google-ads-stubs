import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import operating_system_version_constant
from google.ads.googleads.v9.services.types import (
    operating_system_version_constant_service,
)

class OperatingSystemVersionConstantServiceTransport(metaclass=abc.ABCMeta):
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
    def get_operating_system_version_constant(
        self,
    ) -> typing.Callable[
        [
            operating_system_version_constant_service.GetOperatingSystemVersionConstantRequest
        ],
        operating_system_version_constant.OperatingSystemVersionConstant,
    ]: ...