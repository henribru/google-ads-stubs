import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import customer_asset
from google.ads.googleads.v7.services.types import customer_asset_service

class CustomerAssetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_customer_asset(
        self,
    ) -> typing.Callable[
        [customer_asset_service.GetCustomerAssetRequest], customer_asset.CustomerAsset
    ]: ...
    @property
    def mutate_customer_assets(
        self,
    ) -> typing.Callable[
        [customer_asset_service.MutateCustomerAssetsRequest],
        customer_asset_service.MutateCustomerAssetsResponse,
    ]: ...
