from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v3.proto.services import (
    invoice_service_pb2 as invoice_service_pb2,
)
from google.ads.google_ads.v3.services import (
    invoice_service_client_config as invoice_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    invoice_service_grpc_transport as invoice_service_grpc_transport,
)
from google.ads.google_ads.v3.types import ListInvoicesResponse, MonthOfYearEnum

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
        invoice_service_grpc_transport.InvoiceServiceGrpcTransport,
        Callable[
            [Credentials, type],
            invoice_service_grpc_transport.InvoiceServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                invoice_service_grpc_transport.InvoiceServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    invoice_service_grpc_transport.InvoiceServiceGrpcTransport,
                ],
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
        issue_month: MonthOfYearEnum.MonthOfYearValue,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListInvoicesResponse: ...
