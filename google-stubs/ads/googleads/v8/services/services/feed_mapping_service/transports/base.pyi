import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import feed_mapping
from google.ads.googleads.v8.services.types import feed_mapping_service

class FeedMappingServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_feed_mapping(
        self,
    ) -> typing.Callable[
        [feed_mapping_service.GetFeedMappingRequest], feed_mapping.FeedMapping
    ]: ...
    @property
    def mutate_feed_mappings(
        self,
    ) -> typing.Callable[
        [feed_mapping_service.MutateFeedMappingsRequest],
        feed_mapping_service.MutateFeedMappingsResponse,
    ]: ...
