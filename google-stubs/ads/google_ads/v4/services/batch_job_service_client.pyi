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

from google.ads.google_ads.v4.proto.resources import batch_job_pb2 as batch_job_pb2
from google.ads.google_ads.v4.proto.services import (
    batch_job_service_pb2 as batch_job_service_pb2,
)
from google.ads.google_ads.v4.services import (
    batch_job_service_client_config as batch_job_service_client_config,
)
from google.ads.google_ads.v4.services.transports import (
    batch_job_service_grpc_transport as batch_job_service_grpc_transport,
)
from google.ads.google_ads.v4.types import (
    AddBatchJobOperationsResponse,
    BatchJob,
    BatchJobResult,
    MutateOperation,
)

class BatchJobServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> BatchJobServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> BatchJobServiceClient: ...
    @classmethod
    def batch_job_path(cls, customer: Any, batch_job: Any) -> str: ...
    transport: Union[
        batch_job_service_grpc_transport.BatchJobServiceGrpcTransport,
        Callable[
            [Credentials, type],
            batch_job_service_grpc_transport.BatchJobServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                batch_job_service_grpc_transport.BatchJobServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    batch_job_service_grpc_transport.BatchJobServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def mutate_batch_job(
        self,
        customer_id: str,
        operation_: Union[Dict[str, Any], batch_job_service_pb2.BatchJobOperation],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> batch_job_service_pb2.MutateBatchJobResponse: ...
    def get_batch_job(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> BatchJob: ...
    def list_batch_job_results(
        self,
        resource_name: str,
        page_size: Optional[int] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Iterable[BatchJobResult]: ...
    def run_batch_job(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Operation: ...
    def add_batch_job_operations(
        self,
        resource_name: str,
        sequence_token: str,
        mutate_operations: List[Union[Dict[str, Any], MutateOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AddBatchJobOperationsResponse: ...
