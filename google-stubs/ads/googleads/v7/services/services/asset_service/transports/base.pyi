import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import asset
from google.ads.googleads.v7.services.types import asset_service

class AssetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_asset(
        self,
    ) -> typing.Callable[[asset_service.GetAssetRequest], asset.Asset]: ...
    @property
    def mutate_assets(
        self,
    ) -> typing.Callable[
        [asset_service.MutateAssetsRequest], asset_service.MutateAssetsResponse
    ]: ...
