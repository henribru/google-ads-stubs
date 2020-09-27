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
from google.api_core.operation import Operation  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore
from google.protobuf import empty_pb2 as empty_pb2

from google.ads.google_ads.v3.proto.resources import mutate_job_pb2 as mutate_job_pb2
from google.ads.google_ads.v3.proto.services import (
    mutate_job_service_pb2 as mutate_job_service_pb2,
)
from google.ads.google_ads.v3.services import (
    mutate_job_service_client_config as mutate_job_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    mutate_job_service_grpc_transport as mutate_job_service_grpc_transport,
)
from google.ads.google_ads.v3.types import (
    AddMutateJobOperationsResponse,
    CreateMutateJobResponse,
    MutateJob,
    MutateJobResult,
    MutateOperation,
)

class MutateJobServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MutateJobServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> MutateJobServiceClient: ...
    @classmethod
    def mutate_job_path(cls, customer: Any, mutate_job: Any) -> str: ...
    transport: Union[
        mutate_job_service_grpc_transport.MutateJobServiceGrpcTransport,
        Callable[
            [Credentials, type],
            mutate_job_service_grpc_transport.MutateJobServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                mutate_job_service_grpc_transport.MutateJobServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    mutate_job_service_grpc_transport.MutateJobServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def create_mutate_job(
        self,
        customer_id: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CreateMutateJobResponse: ...
    def get_mutate_job(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateJob: ...
    def list_mutate_job_results(
        self,
        resource_name: str,
        page_size: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[MutateJobResult]: ...
    def run_mutate_job(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Operation: ...
    def add_mutate_job_operations(
        self,
        resource_name: str,
        sequence_token: str,
        mutate_operations: List[Union[Dict[str, Any], MutateOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AddMutateJobOperationsResponse: ...
