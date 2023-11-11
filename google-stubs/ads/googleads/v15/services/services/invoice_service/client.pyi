from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v15.enums.types import month_of_year
from google.ads.googleads.v15.services.types import invoice_service

from .transports.base import InvoiceServiceTransport

class InvoiceServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[InvoiceServiceTransport]: ...

class InvoiceServiceClient(metaclass=InvoiceServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> InvoiceServiceTransport: ...
    def __enter__(self) -> InvoiceServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def invoice_path(customer_id: str, invoice_id: str) -> str: ...
    @staticmethod
    def parse_invoice_path(path: str) -> Dict[str, str]: ...
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
        transport: Optional[Union[str, InvoiceServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def list_invoices(
        self,
        request: Optional[Union[invoice_service.ListInvoicesRequest, dict]] = ...,
        *,
        customer_id: Optional[str] = ...,
        billing_setup: Optional[str] = ...,
        issue_year: Optional[str] = ...,
        issue_month: Optional[month_of_year.MonthOfYearEnum.MonthOfYear] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> invoice_service.ListInvoicesResponse: ...
