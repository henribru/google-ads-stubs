import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import ad_group_asset
from google.ads.googleads.v8.services.types import ad_group_asset_service

class AdGroupAssetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_ad_group_asset(
        self,
    ) -> typing.Callable[
        [ad_group_asset_service.GetAdGroupAssetRequest], ad_group_asset.AdGroupAsset
    ]: ...
    @property
    def mutate_ad_group_assets(
        self,
    ) -> typing.Callable[
        [ad_group_asset_service.MutateAdGroupAssetsRequest],
        ad_group_asset_service.MutateAdGroupAssetsResponse,
    ]: ...
