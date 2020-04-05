import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.custom_interest_service_grpc_transport import (
    CustomInterestServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.custom_interest_pb2 import CustomInterest
from google.ads.google_ads.v2.proto.services.custom_interest_service_pb2 import (
    CustomInterestOperation,
    MutateCustomInterestsResponse,
)

class CustomInterestServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomInterestServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomInterestServiceClient: ...
    @classmethod
    def custom_interest_path(cls, customer: Any, custom_interest: Any) -> str: ...
    transport: Union[
        CustomInterestServiceGrpcTransport,
        Callable[[Credentials, type], CustomInterestServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                CustomInterestServiceGrpcTransport,
                Callable[[Credentials, type], CustomInterestServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_custom_interest(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomInterest: ...
    def mutate_custom_interests(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], CustomInterestOperation]],
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateCustomInterestsResponse: ...
