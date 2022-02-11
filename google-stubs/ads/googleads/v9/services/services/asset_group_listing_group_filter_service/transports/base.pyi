import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v9.services.types import (
    asset_group_listing_group_filter_service,
)

class AssetGroupListingGroupFilterServiceTransport(metaclass=abc.ABCMeta):
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
    def mutate_asset_group_listing_group_filters(
        self,
    ) -> typing.Callable[
        [
            asset_group_listing_group_filter_service.MutateAssetGroupListingGroupFiltersRequest
        ],
        asset_group_listing_group_filter_service.MutateAssetGroupListingGroupFiltersResponse,
    ]: ...
