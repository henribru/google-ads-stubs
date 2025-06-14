from typing import Awaitable, Callable, Sequence, Tuple

import grpc
from google.api_core import gapic_v1, operations_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from grpc.experimental import aio  # type: ignore[attr-defined]

from google.ads.googleads.v19.services.types import experiment_service

from .base import ExperimentServiceTransport

__all__ = ["ExperimentServiceGrpcAsyncIOTransport"]

class _LoggingClientAIOInterceptor(grpc.aio.UnaryUnaryClientInterceptor):
    async def intercept_unary_unary(
        self, continuation, client_call_details, request
    ): ...

class ExperimentServiceGrpcAsyncIOTransport(ExperimentServiceTransport):
    @classmethod
    def create_channel(
        cls,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        **kwargs,
    ) -> aio.Channel: ...
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        channel: aio.Channel | Callable[..., aio.Channel] | None = None,
        api_mtls_endpoint: str | None = None,
        client_cert_source: Callable[[], tuple[bytes, bytes]] | None = None,
        ssl_channel_credentials: grpc.ChannelCredentials | None = None,
        client_cert_source_for_mtls: Callable[[], tuple[bytes, bytes]] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        api_audience: str | None = None,
    ) -> None: ...
    @property
    def grpc_channel(self) -> aio.Channel: ...
    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient: ...  # type: ignore[override]
    @property
    def mutate_experiments(
        self,
    ) -> Callable[
        [experiment_service.MutateExperimentsRequest],
        Awaitable[experiment_service.MutateExperimentsResponse],
    ]: ...
    @property
    def end_experiment(
        self,
    ) -> Callable[
        [experiment_service.EndExperimentRequest], Awaitable[empty_pb2.Empty]
    ]: ...
    @property
    def list_experiment_async_errors(
        self,
    ) -> Callable[
        [experiment_service.ListExperimentAsyncErrorsRequest],
        Awaitable[experiment_service.ListExperimentAsyncErrorsResponse],
    ]: ...
    @property
    def graduate_experiment(
        self,
    ) -> Callable[
        [experiment_service.GraduateExperimentRequest], Awaitable[empty_pb2.Empty]
    ]: ...
    @property
    def schedule_experiment(
        self,
    ) -> Callable[
        [experiment_service.ScheduleExperimentRequest],
        Awaitable[operations_pb2.Operation],
    ]: ...
    @property
    def promote_experiment(
        self,
    ) -> Callable[
        [experiment_service.PromoteExperimentRequest],
        Awaitable[operations_pb2.Operation],
    ]: ...
    def close(self): ...
    @property
    def kind(self) -> str: ...
