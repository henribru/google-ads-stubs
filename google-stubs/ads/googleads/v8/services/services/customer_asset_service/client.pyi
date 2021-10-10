from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import customer_asset
from google.ads.googleads.v8.services.types import customer_asset_service

from .transports.base import CustomerAssetServiceTransport

class CustomerAssetServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[CustomerAssetServiceTransport]: ...

class CustomerAssetServiceClient(metaclass=CustomerAssetServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> CustomerAssetServiceTransport: ...
    @staticmethod
    def asset_path(customer_id: str, asset_id: str) -> str: ...
    @staticmethod
    def parse_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_asset_path(
        customer_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_customer_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, CustomerAssetServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_customer_asset(
        self,
        request: customer_asset_service.GetCustomerAssetRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_asset.CustomerAsset: ...
    def mutate_customer_assets(
        self,
        request: customer_asset_service.MutateCustomerAssetsRequest = ...,
        *,
        customer_id: str = ...,
        operations: Sequence[customer_asset_service.CustomerAssetOperation] = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> customer_asset_service.MutateCustomerAssetsResponse: ...
