from typing import Callable, Optional, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.ads.googleads.v13.services.types import experiment_service

from .base import ExperimentServiceTransport

class ExperimentServiceGrpcTransport(ExperimentServiceTransport):
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        channel: Optional[grpc.Channel] = ...,
        api_mtls_endpoint: Optional[str] = ...,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = ...,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...
    ) -> None: ...
    @classmethod
    def create_channel(
        cls,
        host: str = ...,
        credentials: Optional[ga_credentials.Credentials] = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        **kwargs
    ) -> grpc.Channel: ...
    @property
    def grpc_channel(self) -> grpc.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsClient: ...  # type: ignore[override]
    @property
    def mutate_experiments(
        self,
    ) -> Callable[
        [experiment_service.MutateExperimentsRequest],
        experiment_service.MutateExperimentsResponse,
    ]: ...
    @property
    def end_experiment(
        self,
    ) -> Callable[[experiment_service.EndExperimentRequest], empty_pb2.Empty]: ...
    @property
    def list_experiment_async_errors(
        self,
    ) -> Callable[
        [experiment_service.ListExperimentAsyncErrorsRequest],
        experiment_service.ListExperimentAsyncErrorsResponse,
    ]: ...
    @property
    def graduate_experiment(
        self,
    ) -> Callable[[experiment_service.GraduateExperimentRequest], empty_pb2.Empty]: ...
    @property
    def schedule_experiment(
        self,
    ) -> Callable[
        [experiment_service.ScheduleExperimentRequest], operations_pb2.Operation
    ]: ...
    @property
    def promote_experiment(
        self,
    ) -> Callable[
        [experiment_service.PromoteExperimentRequest], operations_pb2.Operation
    ]: ...
    def close(self) -> None: ...
