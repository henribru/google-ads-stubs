import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_feed
from google.ads.googleads.v7.services.types import campaign_feed_service

class CampaignFeedServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_feed(
        self,
    ) -> typing.Callable[
        [campaign_feed_service.GetCampaignFeedRequest], campaign_feed.CampaignFeed
    ]: ...
    @property
    def mutate_campaign_feeds(
        self,
    ) -> typing.Callable[
        [campaign_feed_service.MutateCampaignFeedsRequest],
        campaign_feed_service.MutateCampaignFeedsResponse,
    ]: ...
