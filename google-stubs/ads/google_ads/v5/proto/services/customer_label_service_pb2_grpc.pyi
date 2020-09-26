from typing import Any, Optional

class CustomerLabelServiceStub:
    GetCustomerLabel: Any = ...
    MutateCustomerLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerLabelServiceServicer:
    def GetCustomerLabel(self, request: Any, context: Any) -> None: ...
    def MutateCustomerLabels(self, request: Any, context: Any) -> None: ...

def add_CustomerLabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CustomerLabelService:
    @staticmethod
    def GetCustomerLabel(
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
    def MutateCustomerLabels(
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
