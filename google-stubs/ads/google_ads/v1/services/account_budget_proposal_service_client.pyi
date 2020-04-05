import grpc  # type: ignore
from google.ads.google_ads.v1.services.transports.account_budget_proposal_service_grpc_transport import (
    AccountBudgetProposalServiceGrpcTransport,
)
from google.auth.credentials import Credentials  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from typing import Optional, Dict, Any, List, Sequence, Tuple, Union, Callable, ClassVar
from google.ads.google_ads.v1.proto.resources.account_budget_proposal_pb2 import (
    AccountBudgetProposal,
)
from google.ads.google_ads.v1.proto.services.account_budget_proposal_service_pb2 import (
    AccountBudgetProposalOperation,
    MutateAccountBudgetProposalResponse,
)

class AccountBudgetProposalServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AccountBudgetProposalServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> AccountBudgetProposalServiceClient: ...
    @classmethod
    def account_budget_proposal_path(
        cls, customer: Any, account_budget_proposal: Any
    ) -> str: ...
    transport: Union[
        AccountBudgetProposalServiceGrpcTransport,
        Callable[[Credentials, type], AccountBudgetProposalServiceGrpcTransport],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                AccountBudgetProposalServiceGrpcTransport,
                Callable[
                    [Credentials, type], AccountBudgetProposalServiceGrpcTransport
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_account_budget_proposal(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> AccountBudgetProposal: ...
    def mutate_account_budget_proposal(
        self,
        customer_id: str,
        operation_: Union[Dict[str, Any], AccountBudgetProposalOperation],
        validate_only: Optional[bool] = ...,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> MutateAccountBudgetProposalResponse: ...
