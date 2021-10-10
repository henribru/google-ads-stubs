import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_shared_set
from google.ads.googleads.v7.services.types import campaign_shared_set_service

class CampaignSharedSetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_shared_set(
        self,
    ) -> typing.Callable[
        [campaign_shared_set_service.GetCampaignSharedSetRequest],
        campaign_shared_set.CampaignSharedSet,
    ]: ...
    @property
    def mutate_campaign_shared_sets(
        self,
    ) -> typing.Callable[
        [campaign_shared_set_service.MutateCampaignSharedSetsRequest],
        campaign_shared_set_service.MutateCampaignSharedSetsResponse,
    ]: ...
