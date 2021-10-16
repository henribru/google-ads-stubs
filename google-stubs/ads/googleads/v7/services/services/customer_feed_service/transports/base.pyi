import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_feed
from google.ads.googleads.v7.services.types import customer_feed_service

class CustomerFeedServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_feed(
        self,
    ) -> typing.Callable[
        [customer_feed_service.GetCustomerFeedRequest], customer_feed.CustomerFeed
    ]: ...
    @property
    def mutate_customer_feeds(
        self,
    ) -> typing.Callable[
        [customer_feed_service.MutateCustomerFeedsRequest],
        customer_feed_service.MutateCustomerFeedsResponse,
    ]: ...
