import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.types import feed_item_service

class FeedItemServiceTransport(abc.ABC):
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
    def mutate_feed_items(
        self,
    ) -> Callable[
        [feed_item_service.MutateFeedItemsRequest],
        Union[
            feed_item_service.MutateFeedItemsResponse,
            Awaitable[feed_item_service.MutateFeedItemsResponse],
        ],
    ]: ...
