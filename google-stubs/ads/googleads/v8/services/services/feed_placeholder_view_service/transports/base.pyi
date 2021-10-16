import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import feed_placeholder_view
from google.ads.googleads.v8.services.types import feed_placeholder_view_service

class FeedPlaceholderViewServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_feed_placeholder_view(
        self,
    ) -> typing.Callable[
        [feed_placeholder_view_service.GetFeedPlaceholderViewRequest],
        feed_placeholder_view.FeedPlaceholderView,
    ]: ...
