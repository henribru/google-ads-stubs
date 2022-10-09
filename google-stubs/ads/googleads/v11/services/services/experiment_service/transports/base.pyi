import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2

from google.ads.googleads.v11.services.types import experiment_service

class ExperimentServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        credentials_file: Optional[str] = ...,
        scopes: Optional[Sequence[str]] = ...,
        quota_project_id: Optional[str] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = ...,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def operations_client(self) -> None: ...
    @property
    def mutate_experiments(
        self,
    ) -> Callable[
        [experiment_service.MutateExperimentsRequest],
        Union[
            experiment_service.MutateExperimentsResponse,
            Awaitable[experiment_service.MutateExperimentsResponse],
        ],
    ]: ...
    @property
    def end_experiment(
        self,
    ) -> Callable[
        [experiment_service.EndExperimentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]: ...
    @property
    def list_experiment_async_errors(
        self,
    ) -> Callable[
        [experiment_service.ListExperimentAsyncErrorsRequest],
        Union[
            experiment_service.ListExperimentAsyncErrorsResponse,
            Awaitable[experiment_service.ListExperimentAsyncErrorsResponse],
        ],
    ]: ...
    @property
    def graduate_experiment(
        self,
    ) -> Callable[
        [experiment_service.GraduateExperimentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]: ...
    @property
    def schedule_experiment(
        self,
    ) -> Callable[
        [experiment_service.ScheduleExperimentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
    @property
    def promote_experiment(
        self,
    ) -> Callable[
        [experiment_service.PromoteExperimentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]: ...
