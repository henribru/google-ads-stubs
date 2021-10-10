import abc
import typing
from typing import Any

from google.api_core import gapic_v1
from google.auth import credentials

from google.ads.googleads.v7.resources.types import account_budget
from google.ads.googleads.v7.services.types import account_budget_service

class AccountBudgetServiceTransport(metaclass=abc.ABCMeta):
    AUTH_SCOPES: Any
    def __init__(
        self,
        *,
        host: str = ...,
        credentials: credentials.Credentials = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    @property
    def get_account_budget(
        self,
    ) -> typing.Callable[
        [account_budget_service.GetAccountBudgetRequest], account_budget.AccountBudget
    ]: ...
