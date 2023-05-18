from typing import Dict, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v13.services.types import account_budget_proposal_service

from .transports.base import AccountBudgetProposalServiceTransport

class AccountBudgetProposalServiceClientMeta(type):
    def get_transport_class(
        cls, label: Optional[str] = ...
    ) -> Type[AccountBudgetProposalServiceTransport]: ...

class AccountBudgetProposalServiceClient(
    metaclass=AccountBudgetProposalServiceClientMeta
):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> AccountBudgetProposalServiceTransport: ...
    def __enter__(self) -> AccountBudgetProposalServiceClient: ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def account_budget_path(customer_id: str, account_budget_id: str) -> str: ...
    @staticmethod
    def parse_account_budget_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def account_budget_proposal_path(
        customer_id: str, account_budget_proposal_id: str
    ) -> str: ...
    @staticmethod
    def parse_account_budget_proposal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def billing_setup_path(customer_id: str, billing_setup_id: str) -> str: ...
    @staticmethod
    def parse_billing_setup_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Optional[Union[str, AccountBudgetProposalServiceTransport]] = ...,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def mutate_account_budget_proposal(
        self,
        request: Optional[
            Union[
                account_budget_proposal_service.MutateAccountBudgetProposalRequest, dict
            ]
        ] = ...,
        *,
        customer_id: Optional[str] = ...,
        operation: Optional[
            account_budget_proposal_service.AccountBudgetProposalOperation
        ] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: Union[float, object] = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> account_budget_proposal_service.MutateAccountBudgetProposalResponse: ...
