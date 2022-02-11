import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import campaign_asset_set_service

class CampaignAssetSetServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_campaign_asset_sets(
        self,
    ) -> typing.Callable[
        [campaign_asset_set_service.MutateCampaignAssetSetsRequest],
        campaign_asset_set_service.MutateCampaignAssetSetsResponse,
    ]: ...
