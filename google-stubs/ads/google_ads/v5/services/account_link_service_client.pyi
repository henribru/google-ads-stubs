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
    account_link_service_pb2 as account_link_service_pb2,
)
from google.ads.google_ads.v5.services import (
    account_link_service_client_config as account_link_service_client_config,
)
from google.ads.google_ads.v5.services.transports import (
    account_link_service_grpc_transport as account_link_service_grpc_transport,
)
from google.ads.google_ads.v5.types import AccountLink, CreateAccountLinkResponse

class AccountLinkServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AccountLinkServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AccountLinkServiceClient: ...
    @classmethod
    def account_link_path(cls, customer: Any, account_link: Any) -> str: ...
    transport: Union[
        account_link_service_grpc_transport.AccountLinkServiceGrpcTransport,
        Callable[
            [Credentials, type],
            account_link_service_grpc_transport.AccountLinkServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                account_link_service_grpc_transport.AccountLinkServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    account_link_service_grpc_transport.AccountLinkServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
        client_options: Optional[Union[Dict[str, Any], ClientOptions]] = ...,
    ) -> None: ...
    def get_account_link(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AccountLink: ...
    def create_account_link(
        self,
        customer_id: str,
        operations: Union[Dict[str, Any], AccountLink],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> CreateAccountLinkResponse: ...
    def mutate_account_link(
        self,
        customer_id: str,
        operation_: Union[
            Dict[str, Any], account_link_service_pb2.AccountLinkOperation
        ],
        partial_failure: Optional[bool] = ...,
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> account_link_service_pb2.MutateAccountLinkResponse: ...
