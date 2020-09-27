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

from google.ads.google_ads.v2.proto.resources import (
    account_budget_pb2 as account_budget_pb2,
    account_budget_proposal_pb2 as account_budget_proposal_pb2,
)
from google.ads.google_ads.v2.proto.services import (
    account_budget_proposal_service_pb2 as account_budget_proposal_service_pb2,
    account_budget_proposal_service_pb2_grpc as account_budget_proposal_service_pb2_grpc,
    account_budget_service_pb2 as account_budget_service_pb2,
    account_budget_service_pb2_grpc as account_budget_service_pb2_grpc,
)
from google.ads.google_ads.v2.services import (
    account_budget_service_client_config as account_budget_service_client_config,
    enums as enums,
)
from google.ads.google_ads.v2.services.transports import (
    account_budget_service_grpc_transport as account_budget_service_grpc_transport,
)
from google.ads.google_ads.v2.types import AccountBudget

class AccountBudgetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AccountBudgetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AccountBudgetServiceClient: ...
    @classmethod
    def account_budget_path(cls, customer: Any, account_budget: Any) -> str: ...
    transport: Union[
        account_budget_service_grpc_transport.AccountBudgetServiceGrpcTransport,
        Callable[
            [Credentials, type],
            account_budget_service_grpc_transport.AccountBudgetServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                account_budget_service_grpc_transport.AccountBudgetServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    account_budget_service_grpc_transport.AccountBudgetServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_account_budget(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AccountBudget: ...
