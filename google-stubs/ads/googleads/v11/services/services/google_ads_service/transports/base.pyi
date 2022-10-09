import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v11.services.types import google_ads_service

class GoogleAdsServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def search(
        self,
    ) -> Callable[
        [google_ads_service.SearchGoogleAdsRequest],
        Union[
            google_ads_service.SearchGoogleAdsResponse,
            Awaitable[google_ads_service.SearchGoogleAdsResponse],
        ],
    ]: ...
    @property
    def search_stream(
        self,
    ) -> Callable[
        [google_ads_service.SearchGoogleAdsStreamRequest],
        Union[
            google_ads_service.SearchGoogleAdsStreamResponse,
            Awaitable[google_ads_service.SearchGoogleAdsStreamResponse],
        ],
    ]: ...
    @property
    def mutate(
        self,
    ) -> Callable[
        [google_ads_service.MutateGoogleAdsRequest],
        Union[
            google_ads_service.MutateGoogleAdsResponse,
            Awaitable[google_ads_service.MutateGoogleAdsResponse],
        ],
    ]: ...
