import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import feed_item
from google.ads.googleads.v9.services.types import feed_item_service

class FeedItemServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def get_feed_item(
        self,
    ) -> typing.Callable[
        [feed_item_service.GetFeedItemRequest], feed_item.FeedItem
    ]: ...
    @property
    def mutate_feed_items(
        self,
    ) -> typing.Callable[
        [feed_item_service.MutateFeedItemsRequest],
        feed_item_service.MutateFeedItemsResponse,
    ]: ...
