import types
from typing import Callable, Dict, MutableSequence, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v20.services.types import ad_group_ad_service

from .transports.base import AdGroupAdServiceTransport

__all__ = ["AdGroupAdServiceClient"]

class AdGroupAdServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[AdGroupAdServiceTransport]: ...

class AdGroupAdServiceClient(metaclass=AdGroupAdServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AdGroupAdServiceTransport: ...
    @staticmethod
    def ad_path(customer_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_ad_path(customer_id: str, ad_group_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_ad_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_ad_label_path(
        customer_id: str, ad_group_id: str, ad_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_ad_label_path(path: str) -> dict[str, str]: ...
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
    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: client_options_lib.ClientOptions | None = None
    ): ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str
        | AdGroupAdServiceTransport
        | Callable[..., AdGroupAdServiceTransport]
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_ad_group_ads(
        self,
        request: ad_group_ad_service.MutateAdGroupAdsRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operations: MutableSequence[ad_group_ad_service.AdGroupAdOperation]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> ad_group_ad_service.MutateAdGroupAdsResponse: ...
    def remove_automatically_created_assets(
        self,
        request: ad_group_ad_service.RemoveAutomaticallyCreatedAssetsRequest
        | dict
        | None = None,
        *,
        ad_group_ad: str | None = None,
        assets_with_field_type: MutableSequence[ad_group_ad_service.AssetsWithFieldType]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str | bytes]] = (),
    ) -> None: ...
    def __enter__(self) -> AdGroupAdServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
