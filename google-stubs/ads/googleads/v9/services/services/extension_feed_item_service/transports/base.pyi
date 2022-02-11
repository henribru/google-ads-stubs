import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.resources.types import extension_feed_item
from google.ads.googleads.v9.services.types import extension_feed_item_service

class ExtensionFeedItemServiceTransport(metaclass=abc.ABCMeta):
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
    def get_extension_feed_item(
        self,
    ) -> typing.Callable[
        [extension_feed_item_service.GetExtensionFeedItemRequest],
        extension_feed_item.ExtensionFeedItem,
    ]: ...
    @property
    def mutate_extension_feed_items(
        self,
    ) -> typing.Callable[
        [extension_feed_item_service.MutateExtensionFeedItemsRequest],
        extension_feed_item_service.MutateExtensionFeedItemsResponse,
    ]: ...
