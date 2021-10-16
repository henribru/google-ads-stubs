import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import campaign_asset
from google.ads.googleads.v7.services.types import campaign_asset_service

class CampaignAssetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_campaign_asset(
        self,
    ) -> typing.Callable[
        [campaign_asset_service.GetCampaignAssetRequest], campaign_asset.CampaignAsset
    ]: ...
    @property
    def mutate_campaign_assets(
        self,
    ) -> typing.Callable[
        [campaign_asset_service.MutateCampaignAssetsRequest],
        campaign_asset_service.MutateCampaignAssetsResponse,
    ]: ...
