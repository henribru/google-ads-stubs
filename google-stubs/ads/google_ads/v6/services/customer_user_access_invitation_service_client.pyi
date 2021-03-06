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

import grpc
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.oauth2 import service_account as service_account  # type: ignore

from google.ads.google_ads.v6.proto.services import (
    customer_user_access_invitation_service_pb2 as customer_user_access_invitation_service_pb2,
)
from google.ads.google_ads.v6.services import (
    customer_user_access_invitation_service_client_config as customer_user_access_invitation_service_client_config,
)
from google.ads.google_ads.v6.services.transports import (
    customer_user_access_invitation_service_grpc_transport as customer_user_access_invitation_service_grpc_transport,
)
from google.ads.google_ads.v6.types import CustomerUserAccessInvitation

class CustomerUserAccessInvitationServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerUserAccessInvitationServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> CustomerUserAccessInvitationServiceClient: ...
    @classmethod
    def customer_user_access_invitation_path(
        cls, customer_id: Any, invitation_id: Any
    ) -> str: ...
    transport: Union[
        customer_user_access_invitation_service_grpc_transport.CustomerUserAccessInvitationServiceGrpcTransport,
        Callable[
            [Credentials, type],
            customer_user_access_invitation_service_grpc_transport.CustomerUserAccessInvitationServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                customer_user_access_invitation_service_grpc_transport.CustomerUserAccessInvitationServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    customer_user_access_invitation_service_grpc_transport.CustomerUserAccessInvitationServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_customer_user_access_invitation(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CustomerUserAccessInvitation: ...
    def mutate_customer_user_access_invitation(
        self,
        customer_id: str,
        operation_: Union[
            Dict[str, Any],
            customer_user_access_invitation_service_pb2.CustomerUserAccessInvitationOperation,
        ],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> customer_user_access_invitation_service_pb2.MutateCustomerUserAccessInvitationResponse: ...
