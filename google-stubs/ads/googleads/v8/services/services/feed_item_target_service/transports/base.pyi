import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import feed_item_target
from google.ads.googleads.v8.services.types import feed_item_target_service

class FeedItemTargetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_feed_item_target(
        self,
    ) -> typing.Callable[
        [feed_item_target_service.GetFeedItemTargetRequest],
        feed_item_target.FeedItemTarget,
    ]: ...
    @property
    def mutate_feed_item_targets(
        self,
    ) -> typing.Callable[
        [feed_item_target_service.MutateFeedItemTargetsRequest],
        feed_item_target_service.MutateFeedItemTargetsResponse,
    ]: ...
