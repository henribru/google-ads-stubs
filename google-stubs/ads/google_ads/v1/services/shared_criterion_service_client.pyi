import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.shared_criterion_service_grpc_transport import (
    SharedCriterionServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.shared_criterion_pb2 import (
    SharedCriterion,
)
from google.ads.google_ads.v1.proto.services.shared_criterion_service_pb2 import (
    SharedCriterionOperation,
    MutateSharedCriteriaResponse,
)

class SharedCriterionServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedCriterionServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedCriterionServiceClient: ...
    @classmethod
    def shared_criteria_path(cls, customer: Any, shared_criteria: Any) -> str: ...
    transport: Union[
        SharedCriterionServiceGrpcTransport,
        Callable[[Credentials, type], SharedCriterionServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                SharedCriterionServiceGrpcTransport,
                Callable[[Credentials, type], SharedCriterionServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_shared_criterion(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> SharedCriterion: ...
    def mutate_shared_criteria(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], SharedCriterionOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateSharedCriteriaResponse: ...
