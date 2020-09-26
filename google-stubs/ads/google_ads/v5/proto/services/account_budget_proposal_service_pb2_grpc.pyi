from typing import Any, Optional

class AccountBudgetProposalServiceStub:
    GetAccountBudgetProposal: Any = ...
    MutateAccountBudgetProposal: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AccountBudgetProposalServiceServicer:
    def GetAccountBudgetProposal(self, request: Any, context: Any) -> None: ...
    def MutateAccountBudgetProposal(self, request: Any, context: Any) -> None: ...

def add_AccountBudgetProposalServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AccountBudgetProposalService:
    @staticmethod
    def GetAccountBudgetProposal(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
    @staticmethod
    def MutateAccountBudgetProposal(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
