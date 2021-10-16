import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import campaign
from google.ads.googleads.v8.services.types import campaign_service

class CampaignServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
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
