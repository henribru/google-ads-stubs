import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.services.types import geo_target_constant_service

__all__ = ["GeoTargetConstantServiceTransport"]

class GeoTargetConstantServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def suggest_geo_target_constants(
        self,
    ) -> Callable[
        [geo_target_constant_service.SuggestGeoTargetConstantsRequest],
        geo_target_constant_service.SuggestGeoTargetConstantsResponse
        | Awaitable[geo_target_constant_service.SuggestGeoTargetConstantsResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
