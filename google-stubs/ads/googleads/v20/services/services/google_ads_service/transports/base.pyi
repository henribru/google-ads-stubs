import abc
from _typeshed import Incomplete
from google.ads.googleads.v20.services.types import google_ads_service
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from typing import Awaitable, Callable, Sequence

__all__ = ['GoogleAdsServiceTransport']

class GoogleAdsServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(self, *, host: str = 'googleads.googleapis.com', credentials: ga_credentials.Credentials | None = None, credentials_file: str | None = None, scopes: Sequence[str] | None = None, quota_project_id: str | None = None, client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: bool | None = False, api_audience: str | None = None, **kwargs) -> None: ...
    @property
    def host(self): ...
    def close(self) -> None: ...
    @property
    def search(self) -> Callable[[google_ads_service.SearchGoogleAdsRequest], google_ads_service.SearchGoogleAdsResponse | Awaitable[google_ads_service.SearchGoogleAdsResponse]]: ...
    @property
    def search_stream(self) -> Callable[[google_ads_service.SearchGoogleAdsStreamRequest], google_ads_service.SearchGoogleAdsStreamResponse | Awaitable[google_ads_service.SearchGoogleAdsStreamResponse]]: ...
    @property
    def mutate(self) -> Callable[[google_ads_service.MutateGoogleAdsRequest], google_ads_service.MutateGoogleAdsResponse | Awaitable[google_ads_service.MutateGoogleAdsResponse]]: ...
    @property
    def kind(self) -> str: ...
