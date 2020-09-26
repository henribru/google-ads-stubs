from typing import Any, Optional

class AccountBudgetServiceStub:
    GetAccountBudget: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AccountBudgetServiceServicer:
    def GetAccountBudget(self, request: Any, context: Any) -> None: ...

def add_AccountBudgetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AccountBudgetService:
    @staticmethod
    def GetAccountBudget(
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
