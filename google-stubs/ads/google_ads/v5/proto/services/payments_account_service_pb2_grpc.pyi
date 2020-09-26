from typing import Any, Optional

class PaymentsAccountServiceStub:
    ListPaymentsAccounts: Any = ...
    def __init__(self, channel: Any) -> None: ...

class PaymentsAccountServiceServicer:
    def ListPaymentsAccounts(self, request: Any, context: Any) -> None: ...

def add_PaymentsAccountServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class PaymentsAccountService:
    @staticmethod
    def ListPaymentsAccounts(
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
