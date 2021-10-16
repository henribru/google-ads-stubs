import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import feed_item_set
from google.ads.googleads.v8.services.types import feed_item_set_service

class FeedItemSetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_feed_item_set(
        self,
    ) -> typing.Callable[
        [feed_item_set_service.GetFeedItemSetRequest], feed_item_set.FeedItemSet
    ]: ...
    @property
    def mutate_feed_item_sets(
        self,
    ) -> typing.Callable[
        [feed_item_set_service.MutateFeedItemSetsRequest],
        feed_item_set_service.MutateFeedItemSetsResponse,
    ]: ...
