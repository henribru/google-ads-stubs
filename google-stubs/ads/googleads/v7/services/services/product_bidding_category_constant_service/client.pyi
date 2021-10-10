from typing import Any, Dict, Optional, Sequence, Tuple, Type, Union

from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials

from google.ads.googleads.v7.resources.types import product_bidding_category_constant
from google.ads.googleads.v7.services.types import (
    product_bidding_category_constant_service,
)

from .transports.base import ProductBiddingCategoryConstantServiceTransport

class ProductBiddingCategoryConstantServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[ProductBiddingCategoryConstantServiceTransport]: ...

class ProductBiddingCategoryConstantServiceClient(
    metaclass=ProductBiddingCategoryConstantServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Any
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Any
    @property
    def transport(self) -> ProductBiddingCategoryConstantServiceTransport: ...
    @staticmethod
    def product_bidding_category_constant_path(
        country_code: str, level: str, id: str
    ) -> str: ...
    @staticmethod
    def parse_product_bidding_category_constant_path(path: str) -> Dict[str, str]: ...
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
        transport: Union[
            str, ProductBiddingCategoryConstantServiceTransport, None
        ] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def get_product_bidding_category_constant(
        self,
        request: product_bidding_category_constant_service.GetProductBiddingCategoryConstantRequest = ...,
        *,
        resource_name: str = ...,
        retry: retries.Retry = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> product_bidding_category_constant.ProductBiddingCategoryConstant: ...
