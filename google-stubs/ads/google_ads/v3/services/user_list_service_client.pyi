from google.ads.google_ads.v3.proto.services import (
    user_list_service_pb2 as user_list_service_pb2,
)
from google.ads.google_ads.v3.services import (
    user_list_service_client_config as user_list_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    user_list_service_grpc_transport as user_list_service_grpc_transport,
)
from google.oauth2 import service_account as service_account  # type: ignore
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.user_list_service_grpc_transport import (
    UserListServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.proto.resources.user_list_pb2 import UserList
from google.ads.google_ads.v3.proto.services.user_list_service_pb2 import (
    UserListOperation,
    MutateUserListsResponse,
)

class UserListServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserListServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserListServiceClient: ...
    @classmethod
    def user_list_path(cls, customer: Any, user_list: Any) -> str: ...
    transport: Union[
        UserListServiceGrpcTransport,
        Callable[[Credentials, type], UserListServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                UserListServiceGrpcTransport,
                Callable[[Credentials, type], UserListServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_user_list(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UserList: ...
    def mutate_user_lists(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], UserListOperation]],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateUserListsResponse: ...
