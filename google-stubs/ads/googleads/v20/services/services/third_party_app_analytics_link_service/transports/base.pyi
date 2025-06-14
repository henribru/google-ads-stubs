import abc
from _typeshed import Incomplete
from google.ads.googleads.v20.services.types import third_party_app_analytics_link_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from typing import Awaitable, Callable, Sequence

__all__ = ['ThirdPartyAppAnalyticsLinkServiceTransport']

class ThirdPartyAppAnalyticsLinkServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = ..., credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def regenerate_shareable_link_id(self) -> Callable[[third_party_app_analytics_link_service.RegenerateShareableLinkIdRequest], third_party_app_analytics_link_service.RegenerateShareableLinkIdResponse | Awaitable[third_party_app_analytics_link_service.RegenerateShareableLinkIdResponse]]: ...
    @property
    def kind(self) -> str: ...
