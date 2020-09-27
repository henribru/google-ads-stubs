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
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v5.proto.services import (
    user_data_service_pb2 as user_data_service_pb2,
)
from google.ads.google_ads.v5.services import (
    user_data_service_client_config as user_data_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    user_data_service_grpc_transport as user_data_service_grpc_transport,
)
from google.ads.google_ads.v5.types import (
    CustomerMatchUserListMetadata,
    UploadUserDataResponse,
    UserDataOperation,
)

class UserDataServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserDataServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserDataServiceClient: ...
    transport: Union[
        user_data_service_grpc_transport.UserDataServiceGrpcTransport,
        Callable[
            [Credentials, type],
            user_data_service_grpc_transport.UserDataServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                user_data_service_grpc_transport.UserDataServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    user_data_service_grpc_transport.UserDataServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def upload_user_data(
        self,
        customer_id: str,
        operations: List[Union[Dict[str, Any], UserDataOperation]],
        customer_match_user_list_metadata: Optional[
            Union[Dict[str, Any], CustomerMatchUserListMetadata]
        ] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UploadUserDataResponse: ...
