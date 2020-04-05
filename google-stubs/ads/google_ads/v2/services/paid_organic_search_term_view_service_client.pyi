import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.paid_organic_search_term_view_service_grpc_transport import (
    PaidOrganicSearchTermViewServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.paid_organic_search_term_view_pb2 import (
    PaidOrganicSearchTermView,
)

class PaidOrganicSearchTermViewServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> PaidOrganicSearchTermViewServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> PaidOrganicSearchTermViewServiceClient: ...
    @classmethod
    def paid_organic_search_term_view_path(
        cls, customer: Any, paid_organic_search_term_view: Any
    ) -> str: ...
    transport: Union[
        PaidOrganicSearchTermViewServiceGrpcTransport,
        Callable[[Credentials, type], PaidOrganicSearchTermViewServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                PaidOrganicSearchTermViewServiceGrpcTransport,
                Callable[
                    [Credentials, type], PaidOrganicSearchTermViewServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_paid_organic_search_term_view(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> PaidOrganicSearchTermView: ...
