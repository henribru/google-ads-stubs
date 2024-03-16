import types
from typing import Dict, Sequence, Tuple, Type

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.services.types import (
    customer_sk_ad_network_conversion_value_schema_service,
)

from .transports.base import CustomerSkAdNetworkConversionValueSchemaServiceTransport

__all__ = ["CustomerSkAdNetworkConversionValueSchemaServiceClient"]

class CustomerSkAdNetworkConversionValueSchemaServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[CustomerSkAdNetworkConversionValueSchemaServiceTransport]: ...

class CustomerSkAdNetworkConversionValueSchemaServiceClient(
    metaclass=CustomerSkAdNetworkConversionValueSchemaServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> CustomerSkAdNetworkConversionValueSchemaServiceTransport: ...
    def __enter__(self) -> CustomerSkAdNetworkConversionValueSchemaServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def customer_sk_ad_network_conversion_value_schema_path(
        customer_id: str, account_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_sk_ad_network_conversion_value_schema_path(
        path: str,
    ) -> dict[str, str]: ...
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
        transport: str
        | CustomerSkAdNetworkConversionValueSchemaServiceTransport
        | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_customer_sk_ad_network_conversion_value_schema(
        self,
        request: customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaRequest
        | dict
        | None = None,
        *,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> customer_sk_ad_network_conversion_value_schema_service.MutateCustomerSkAdNetworkConversionValueSchemaResponse: ...
