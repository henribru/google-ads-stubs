from typing import Any, Optional

class InvoiceServiceStub:
    ListInvoices: Any = ...
    def __init__(self, channel: Any) -> None: ...

class InvoiceServiceServicer:
    def ListInvoices(self, request: Any, context: Any) -> None: ...

def add_InvoiceServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class InvoiceService:
    @staticmethod
    def ListInvoices(
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
