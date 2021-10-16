import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_bid_modifier
from google.ads.googleads.v7.services.types import campaign_bid_modifier_service

class CampaignBidModifierServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_bid_modifier(
        self,
    ) -> typing.Callable[
        [campaign_bid_modifier_service.GetCampaignBidModifierRequest],
        campaign_bid_modifier.CampaignBidModifier,
    ]: ...
    @property
    def mutate_campaign_bid_modifiers(
        self,
    ) -> typing.Callable[
        [campaign_bid_modifier_service.MutateCampaignBidModifiersRequest],
        campaign_bid_modifier_service.MutateCampaignBidModifiersResponse,
    ]: ...
