from typing import Any

class PaymentsAccountServiceStub:
    ListPaymentsAccounts: Any = ...
    def __init__(self, channel: Any) -> None: ...

class PaymentsAccountServiceServicer:
    def ListPaymentsAccounts(self, request: Any, context: Any) -> None: ...

def add_PaymentsAccountServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...