from .transports.base import InvoiceServiceTransport
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import month_of_year
from google.ads.googleads.v19.services.types import invoice_service
from google.api_core import gapic_v1, retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from typing import Callable, Sequence

__all__ = ['InvoiceServiceAsyncClient']

class InvoiceServiceAsyncClient:
    DEFAULT_ENDPOINT: Incomplete
    DEFAULT_MTLS_ENDPOINT: Incomplete
    invoice_path: Incomplete
    parse_invoice_path: Incomplete
    common_billing_account_path: Incomplete
    parse_common_billing_account_path: Incomplete
    common_folder_path: Incomplete
    parse_common_folder_path: Incomplete
    common_organization_path: Incomplete
    parse_common_organization_path: Incomplete
    common_project_path: Incomplete
    parse_common_project_path: Incomplete
    common_location_path: Incomplete
    parse_common_location_path: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: ClientOptions | None = None): ...
    @property
    def transport(self) -> InvoiceServiceTransport: ...
    @property
    def api_endpoint(self): ...
    @property
    def universe_domain(self) -> str: ...
    get_transport_class: Incomplete
    def __init__(self, *, credentials: ga_credentials.Credentials | None = None, transport: str | InvoiceServiceTransport | Callable[..., InvoiceServiceTransport] | None = 'grpc_asyncio', client_options: ClientOptions | None = None, client_info: gapic_v1.client_info.ClientInfo = ...) -> None: ...
    async def list_invoices(self, request: invoice_service.ListInvoicesRequest | dict | None = None, *, customer_id: str | None = None, billing_setup: str | None = None, issue_year: str | None = None, issue_month: month_of_year.MonthOfYearEnum.MonthOfYear | None = None, retry: retries.AsyncRetry | gapic_v1.method._MethodDefault = ..., timeout: float | object = ..., metadata: Sequence[tuple[str, str | bytes]] = ()) -> invoice_service.ListInvoicesResponse: ...
    async def __aenter__(self) -> InvoiceServiceAsyncClient: ...
    async def __aexit__(self, exc_type, exc, tb) -> None: ...
