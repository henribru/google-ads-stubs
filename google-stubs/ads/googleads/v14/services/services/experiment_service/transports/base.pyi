import abc
from typing import Awaitable, Callable, Sequence

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.ads.googleads.v14.services.types import experiment_service

__all__ = ["ExperimentServiceTransport"]

class ExperimentServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: ga_credentials.Credentials | None = None,
        credentials_file: str | None = None,
        scopes: Sequence[str] | None = None,
        quota_project_id: str | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: bool | None = False,
        **kwargs,
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def mutate_experiments(
        self,
    ) -> Callable[
        [experiment_service.MutateExperimentsRequest],
        experiment_service.MutateExperimentsResponse
        | Awaitable[experiment_service.MutateExperimentsResponse],
    ]: ...
    @property
    def end_experiment(
        self,
    ) -> Callable[
        [experiment_service.EndExperimentRequest],
        empty_pb2.Empty | Awaitable[empty_pb2.Empty],
    ]: ...
    @property
    def list_experiment_async_errors(
        self,
    ) -> Callable[
        [experiment_service.ListExperimentAsyncErrorsRequest],
        experiment_service.ListExperimentAsyncErrorsResponse
        | Awaitable[experiment_service.ListExperimentAsyncErrorsResponse],
    ]: ...
    @property
    def graduate_experiment(
        self,
    ) -> Callable[
        [experiment_service.GraduateExperimentRequest],
        empty_pb2.Empty | Awaitable[empty_pb2.Empty],
    ]: ...
    @property
    def schedule_experiment(
        self,
    ) -> Callable[
        [experiment_service.ScheduleExperimentRequest],
        operations_pb2.Operation | Awaitable[operations_pb2.Operation],
    ]: ...
    @property
    def promote_experiment(
        self,
    ) -> Callable[
        [experiment_service.PromoteExperimentRequest],
        operations_pb2.Operation | Awaitable[operations_pb2.Operation],
    ]: ...
