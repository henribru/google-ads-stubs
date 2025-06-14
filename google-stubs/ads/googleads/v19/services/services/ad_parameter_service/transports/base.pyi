import abc
from _typeshed import Incomplete
from google.ads.googleads.v19.services.types import ad_parameter_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from typing import Awaitable, Callable, Sequence

__all__ = ['AdParameterServiceTransport']

class AdParameterServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = ..., credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def mutate_ad_parameters(self) -> Callable[[ad_parameter_service.MutateAdParametersRequest], ad_parameter_service.MutateAdParametersResponse | Awaitable[ad_parameter_service.MutateAdParametersResponse]]: ...
    @property
    def kind(self) -> str: ...
