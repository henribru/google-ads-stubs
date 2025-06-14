import abc
from _typeshed import Incomplete
from google.ads.googleads.v18.services.types import content_creator_insights_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from typing import Awaitable, Callable, Sequence

__all__ = ['ContentCreatorInsightsServiceTransport']

class ContentCreatorInsightsServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = 'googleads.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def generate_creator_insights(self) -> Callable[[content_creator_insights_service.GenerateCreatorInsightsRequest], content_creator_insights_service.GenerateCreatorInsightsResponse | Awaitable[content_creator_insights_service.GenerateCreatorInsightsResponse]]: ...
    @property
    def kind(self) -> str: ...
