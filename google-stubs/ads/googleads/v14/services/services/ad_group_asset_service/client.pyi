import types
from typing import Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.types import ad_group_asset_service

from .transports.base import AdGroupAssetServiceTransport

__all__ = ["AdGroupAssetServiceClient"]

class AdGroupAssetServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[AdGroupAssetServiceTransport]: ...

class AdGroupAssetServiceClient(metaclass=AdGroupAssetServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AdGroupAssetServiceTransport: ...
    def __enter__(self) -> AdGroupAssetServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_asset_path(
        customer_id: str, ad_group_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_path(customer_id: str, asset_id: str) -> str: ...
    @staticmethod
    def parse_asset_path(path: str) -> dict[str, str]: ...
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
        transport: str | AdGroupAssetServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_ad_group_assets(
        self,
        request: ad_group_asset_service.MutateAdGroupAssetsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[ad_group_asset_service.AdGroupAssetOperation]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> ad_group_asset_service.MutateAdGroupAssetsResponse: ...
