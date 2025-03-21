import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v17.services.types import ad_group_feed_service

__all__ = ["AdGroupFeedServiceTransport"]

class AdGroupFeedServiceTransport(abc.ABC):
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
    def mutate_ad_group_feeds(
        self,
    ) -> Callable[
        [ad_group_feed_service.MutateAdGroupFeedsRequest],
        ad_group_feed_service.MutateAdGroupFeedsResponse
        | Awaitable[ad_group_feed_service.MutateAdGroupFeedsResponse],
    ]: ...
    @property
    def kind(self) -> str: ...
