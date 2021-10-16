from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import merchant_center_link
from google.ads.googleads.v7.services.types import merchant_center_link_service

from .transports.base import MerchantCenterLinkServiceTransport

class MerchantCenterLinkServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[MerchantCenterLinkServiceTransport]: ...

class MerchantCenterLinkServiceClient(metaclass=MerchantCenterLinkServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> MerchantCenterLinkServiceTransport: ...
    @staticmethod
    def merchant_center_link_path(customer_id: str, merchant_center_id: str) -> str: ...
    @staticmethod
    def parse_merchant_center_link_path(path: str) -> Dict[str, str]: ...
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
        credentials: Optional[credentials.Credentials] = ...,
        transport: Union[str, MerchantCenterLinkServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def list_merchant_center_links(
        self,
        request: merchant_center_link_service.ListMerchantCenterLinksRequest = ...,
        *,
        customer_id: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> merchant_center_link_service.ListMerchantCenterLinksResponse: ...
    def get_merchant_center_link(
        self,
        request: merchant_center_link_service.GetMerchantCenterLinkRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> merchant_center_link.MerchantCenterLink: ...
    def mutate_merchant_center_link(
        self,
        request: merchant_center_link_service.MutateMerchantCenterLinkRequest = ...,
        *,
        customer_id: str = ...,
        operation: merchant_center_link_service.MerchantCenterLinkOperation = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> merchant_center_link_service.MutateMerchantCenterLinkResponse: ...