from typing import Any, Optional

class CustomerClientLinkServiceStub:
    GetCustomerClientLink: Any = ...
    MutateCustomerClientLink: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerClientLinkServiceServicer:
    def GetCustomerClientLink(self, request: Any, context: Any) -> None: ...
    def MutateCustomerClientLink(self, request: Any, context: Any) -> None: ...

def add_CustomerClientLinkServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CustomerClientLinkService:
    @staticmethod
    def GetCustomerClientLink(
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
    def MutateCustomerClientLink(
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
