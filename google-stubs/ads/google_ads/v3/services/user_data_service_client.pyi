from google.ads.google_ads.v3.proto.services import (
    user_data_service_pb2 as user_data_service_pb2,
)
from google.ads.google_ads.v3.services import (
    user_data_service_client_config as user_data_service_client_config,
)
from google.ads.google_ads.v3.services.transports import (
    user_data_service_grpc_transport as user_data_service_grpc_transport,
)
from google.oauth2 import service_account as service_account
import grpc  # type: ignore
from google.ads.google_ads.v3.services.transports.user_data_service_grpc_transport import (
    UserDataServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v3.types import (
    CustomerMatchUserListMetadata,
    UserDataOperation,
    UploadUserDataResponse,
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
        UserDataServiceGrpcTransport,
        Callable[[Credentials, type], UserDataServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                UserDataServiceGrpcTransport,
                Callable[[Credentials, type], UserDataServiceGrpcTransport],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
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
