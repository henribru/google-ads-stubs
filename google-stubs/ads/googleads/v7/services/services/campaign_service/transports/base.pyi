import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign
from google.ads.googleads.v7.services.types import campaign_service

class CampaignServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign(
        self,
    ) -> typing.Callable[[campaign_service.GetCampaignRequest], campaign.Campaign]: ...
    @property
    def mutate_campaigns(
        self,
    ) -> typing.Callable[
        [campaign_service.MutateCampaignsRequest],
        campaign_service.MutateCampaignsResponse,
    ]: ...
