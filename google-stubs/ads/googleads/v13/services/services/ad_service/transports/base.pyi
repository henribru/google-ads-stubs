import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.resources.types import ad
from google.ads.googleads.v13.services.types import ad_service

class AdServiceTransport(abc.ABC):
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
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_ad(
        self,
    ) -> Callable[[ad_service.GetAdRequest], ad.Ad | Awaitable[ad.Ad]]: ...
    @property
    def mutate_ads(
        self,
    ) -> Callable[
        [ad_service.MutateAdsRequest],
        ad_service.MutateAdsResponse | Awaitable[ad_service.MutateAdsResponse],
    ]: ...
