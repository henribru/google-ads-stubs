from typing import Any, Optional

class CustomerClientServiceStub:
    GetCustomerClient: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerClientServiceServicer:
    def GetCustomerClient(self, request: Any, context: Any) -> None: ...

def add_CustomerClientServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CustomerClientService:
    @staticmethod
    def GetCustomerClient(
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
