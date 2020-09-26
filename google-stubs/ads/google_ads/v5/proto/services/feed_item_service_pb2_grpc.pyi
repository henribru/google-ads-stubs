from typing import Any, Optional

class FeedItemServiceStub:
    GetFeedItem: Any = ...
    MutateFeedItems: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedItemServiceServicer:
    def GetFeedItem(self, request: Any, context: Any) -> None: ...
    def MutateFeedItems(self, request: Any, context: Any) -> None: ...

def add_FeedItemServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class FeedItemService:
    @staticmethod
    def GetFeedItem(
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
    def MutateFeedItems(
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
