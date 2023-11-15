import abc
from typing import Awaitable, Callable, Optional, Sequence, Union

from _typeshed import Incomplete
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import account_budget_proposal_service

class AccountBudgetProposalServiceTransport(abc.ABC):
    AUTH_SCOPES: Incomplete
    DEFAULT_HOST: str
    def __init__(
        self,
        *,
        host: str = "googleads.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs
    ) -> None: ...
    def close(self) -> None: ...
    @property
    def mutate_account_budget_proposal(
        self,
    ) -> Callable[
        [account_budget_proposal_service.MutateAccountBudgetProposalRequest],
        Union[
            account_budget_proposal_service.MutateAccountBudgetProposalResponse,
            Awaitable[
                account_budget_proposal_service.MutateAccountBudgetProposalResponse
            ],
        ],
    ]: ...
