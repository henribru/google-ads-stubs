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
    user_interest_service_pb2 as user_interest_service_pb2,
)
from google.ads.google_ads.v5.services import (
    user_interest_service_client_config as user_interest_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    user_interest_service_grpc_transport as user_interest_service_grpc_transport,
)
from google.ads.google_ads.v5.types import UserInterest

class UserInterestServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserInterestServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> UserInterestServiceClient: ...
    @classmethod
    def user_interest_path(cls, customer: Any, user_interest: Any) -> str: ...
    transport: Union[
        user_interest_service_grpc_transport.UserInterestServiceGrpcTransport,
        Callable[
            [Credentials, type],
            user_interest_service_grpc_transport.UserInterestServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                user_interest_service_grpc_transport.UserInterestServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    user_interest_service_grpc_transport.UserInterestServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_user_interest(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> UserInterest: ...
