import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.google_ads_service_grpc_transport import (
    GoogleAdsServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import (
    Optional,
    Dict,
    Any,
    List,
    Sequence,
    Tuple,
    Union,
    Callable,
    ClassVar,
    Iterator,
)

from google.ads.google_ads.v2.proto.services.google_ads_service_pb2 import (
    GoogleAdsRow,
    MutateGoogleAdsResponse,
    MutateOperation,
)

class GoogleAdsServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GoogleAdsServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> GoogleAdsServiceClient: ...
    transport: Union[
        GoogleAdsServiceGrpcTransport,
        Callable[[Credentials, type], GoogleAdsServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                GoogleAdsServiceGrpcTransport,
                Callable[[Credentials, type], GoogleAdsServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def search(
        self,
        customer_id: str,
        query: str,
        page_size: Optional[int] = ...,
        validate_only: Optional[bool] = ...,
        return_summary_row: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterator[GoogleAdsRow]: ...
    def mutate(
        self,
        customer_id: str,
        mutate_operations: List[Union[Dict[str, Any], MutateOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateGoogleAdsResponse: ...
