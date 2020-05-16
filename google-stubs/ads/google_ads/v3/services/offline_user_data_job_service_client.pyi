from google.ads.google_ads.v3.proto.services import (
    offline_user_data_job_service_pb2 as offline_user_data_job_service_pb2,
)
from google.ads.google_ads.v3.services import (
    offline_user_data_job_service_client_config as offline_user_data_job_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    offline_user_data_job_service_grpc_transport as offline_user_data_job_service_grpc_transport,
)
from google.oauth2 import service_account as service_account
from google.protobuf import empty_pb2 as empty_pb2
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.offline_user_data_job_service_grpc_transport import (
    OfflineUserDataJobServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.types import (
    OfflineUserDataJob,
    OfflineUserDataJobOperation,
    CreateOfflineUserDataJobResponse,
    AddOfflineUserDataJobOperationsResponse,
    BoolValue,
)
from google.api_core.operation import Operation  # type: ignore
from typing_extensions import TypedDict

class BoolValueDict(TypedDict):
    value: bool

class OfflineUserDataJobServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> OfflineUserDataJobServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> OfflineUserDataJobServiceClient: ...
    @classmethod
    def offline_user_data_job_path(
        cls, customer: Any, offline_user_data_job: Any
    ) -> str: ...
    transport: Union[
        OfflineUserDataJobServiceGrpcTransport,
        Callable[[Credentials, type], OfflineUserDataJobServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                OfflineUserDataJobServiceGrpcTransport,
                Callable[[Credentials, type], OfflineUserDataJobServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def create_offline_user_data_job(
        self,
        customer_id: str,
        job: Union[Dict[str, Any], OfflineUserDataJob],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CreateOfflineUserDataJobResponse: ...
    def get_offline_user_data_job(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> OfflineUserDataJob: ...
    def add_offline_user_data_job_operations(
        self,
        resource_name: str,
        enable_partial_failure: Union[BoolValueDict, BoolValue],
        operations: List[Union[Dict[str, Any], OfflineUserDataJobOperation]],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AddOfflineUserDataJobOperationsResponse: ...
    def run_offline_user_data_job(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> Operation: ...
