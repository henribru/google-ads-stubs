from typing import Any, Optional

class CustomerFeedServiceStub:
    GetCustomerFeed: Any = ...
    MutateCustomerFeeds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomerFeedServiceServicer:
    def GetCustomerFeed(self, request: Any, context: Any) -> None: ...
    def MutateCustomerFeeds(self, request: Any, context: Any) -> None: ...

def add_CustomerFeedServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CustomerFeedService:
    @staticmethod
    def GetCustomerFeed(
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
    def MutateCustomerFeeds(
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
