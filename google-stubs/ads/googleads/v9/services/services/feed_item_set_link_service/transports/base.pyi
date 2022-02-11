import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import feed_item_set_link
from google.ads.googleads.v9.services.types import feed_item_set_link_service

class FeedItemSetLinkServiceTransport(metaclass=abc.ABCMeta):
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
    def get_feed_item_set_link(
        self,
    ) -> typing.Callable[
        [feed_item_set_link_service.GetFeedItemSetLinkRequest],
        feed_item_set_link.FeedItemSetLink,
    ]: ...
    @property
    def mutate_feed_item_set_links(
        self,
    ) -> typing.Callable[
        [feed_item_set_link_service.MutateFeedItemSetLinksRequest],
        feed_item_set_link_service.MutateFeedItemSetLinksResponse,
    ]: ...
