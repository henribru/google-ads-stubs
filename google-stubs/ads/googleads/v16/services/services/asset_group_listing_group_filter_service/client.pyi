import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v16.services.types import (
    asset_group_listing_group_filter_service,
)

from .transports.base import AssetGroupListingGroupFilterServiceTransport

__all__ = ["AssetGroupListingGroupFilterServiceClient"]

class AssetGroupListingGroupFilterServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[AssetGroupListingGroupFilterServiceTransport]: ...

class AssetGroupListingGroupFilterServiceClient(
    metaclass=AssetGroupListingGroupFilterServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AssetGroupListingGroupFilterServiceTransport: ...
    def __enter__(self) -> AssetGroupListingGroupFilterServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def asset_group_path(customer_id: str, asset_group_id: str) -> str: ...
    @staticmethod
    def parse_asset_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_group_listing_group_filter_path(
        customer_id: str, asset_group_id: str, listing_group_filter_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_listing_group_filter_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str | AssetGroupListingGroupFilterServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_asset_group_listing_group_filters(
        self,
        request: asset_group_listing_group_filter_service.MutateAssetGroupListingGroupFiltersRequest
        | dict
        | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[
            asset_group_listing_group_filter_service.AssetGroupListingGroupFilterOperation
        ]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> asset_group_listing_group_filter_service.MutateAssetGroupListingGroupFiltersResponse: ...
