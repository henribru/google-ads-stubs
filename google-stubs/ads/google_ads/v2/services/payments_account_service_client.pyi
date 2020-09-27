from typing import Any, Callable, ClassVar, Dict, List, Optional, Sequence, Tuple, Union

import grpc  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore

from google.ads.google_ads.v2.proto.services.payments_account_service_pb2 import (
    ListPaymentsAccountsResponse,
)
from google.ads.google_ads.v2.services.transports.payments_account_service_grpc_transport import (
    PaymentsAccountServiceGrpcTransport,
)

class PaymentsAccountServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> PaymentsAccountServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> PaymentsAccountServiceClient: ...
    transport: Union[
        PaymentsAccountServiceGrpcTransport,
        Callable[[Credentials, type], PaymentsAccountServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                PaymentsAccountServiceGrpcTransport,
                Callable[[Credentials, type], PaymentsAccountServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def list_payments_accounts(
        self,
        customer_id: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> ListPaymentsAccountsResponse: ...
