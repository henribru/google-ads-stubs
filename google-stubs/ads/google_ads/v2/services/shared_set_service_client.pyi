import grpc  # type: ignore
from google.ads.google_ads.v2.services.transports.shared_set_service_grpc_transport import (
    SharedSetServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v2.proto.resources.shared_set_pb2 import SharedSet
from google.ads.google_ads.v2.proto.services.shared_set_service_pb2 import (
    SharedSetOperation,
    MutateSharedSetsResponse,
)

class SharedSetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedSetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> SharedSetServiceClient: ...
    @classmethod
    def shared_set_path(cls, customer: Any, shared_set: Any) -> str: ...
    transport: Union[
        SharedSetServiceGrpcTransport,
        Callable[[Credentials, type], SharedSetServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                SharedSetServiceGrpcTransport,
                Callable[[Credentials, type], SharedSetServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_shared_set(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> SharedSet: ...
    def mutate_shared_sets(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], SharedSetOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateSharedSetsResponse: ...
