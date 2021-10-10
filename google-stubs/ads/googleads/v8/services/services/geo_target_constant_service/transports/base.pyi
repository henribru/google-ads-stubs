import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import geo_target_constant
from google.ads.googleads.v8.services.types import geo_target_constant_service

class GeoTargetConstantServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_geo_target_constant(
        self,
    ) -> typing.Callable[
        [geo_target_constant_service.GetGeoTargetConstantRequest],
        geo_target_constant.GeoTargetConstant,
    ]: ...
    @property
    def suggest_geo_target_constants(
        self,
    ) -> typing.Callable[
        [geo_target_constant_service.SuggestGeoTargetConstantsRequest],
        geo_target_constant_service.SuggestGeoTargetConstantsResponse,
    ]: ...
