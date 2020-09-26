from typing import Any, Optional

class CustomerManagerLinkServiceStub:
    GetCustomerManagerLink: Any = ...
    MutateCustomerManagerLink: Any = ...
    MoveManagerLink: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerManagerLinkServiceServicer:
    def GetCustomerManagerLink(self, request: Any, context: Any) -> None: ...
    def MutateCustomerManagerLink(self, request: Any, context: Any) -> None: ...
    def MoveManagerLink(self, request: Any, context: Any) -> None: ...

def add_CustomerManagerLinkServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class CustomerManagerLinkService:
    @staticmethod
    def GetCustomerManagerLink(
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
    def MutateCustomerManagerLink(
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
    def MoveManagerLink(
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
