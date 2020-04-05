import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.invoice_service_grpc_transport import (
    InvoiceServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar

from google.ads.google_ads.v2.proto.services.invoice_service_pb2 import (
    ListInvoicesResponse,
)

from google.ads.google_ads.v2.proto.enums.month_of_year_pb2 import MonthOfYearEnum

class InvoiceServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> InvoiceServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> InvoiceServiceClient: ...
    transport: Union[
        InvoiceServiceGrpcTransport,
        Callable[[Credentials, type], InvoiceServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                InvoiceServiceGrpcTransport,
                Callable[[Credentials, type], InvoiceServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def list_invoices(
        self,
        customer_id: str,
        billing_setup: str,
        issue_year: str,
        issue_month: MonthOfYearEnum.MonthOfYear,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Optional[Sequence[Tuple[str, str]]]] = ...,
    ) -> ListInvoicesResponse: ...
