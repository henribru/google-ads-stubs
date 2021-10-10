import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials

from google.ads.googleads.v8.resources.types import account_budget_proposal
from google.ads.googleads.v8.services.types import account_budget_proposal_service

class AccountBudgetProposalServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: ga_credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_account_budget_proposal(
        self,
    ) -> typing.Callable[
        [account_budget_proposal_service.GetAccountBudgetProposalRequest],
        account_budget_proposal.AccountBudgetProposal,
    ]: ...
    @property
    def mutate_account_budget_proposal(
        self,
    ) -> typing.Callable[
        [account_budget_proposal_service.MutateAccountBudgetProposalRequest],
        account_budget_proposal_service.MutateAccountBudgetProposalResponse,
    ]: ...
