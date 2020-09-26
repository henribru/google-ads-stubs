from typing import Any, Optional

class FeedServiceStub:
    GetFeed: Any = ...
    MutateFeeds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedServiceServicer:
    def GetFeed(self, request: Any, context: Any) -> None: ...
    def MutateFeeds(self, request: Any, context: Any) -> None: ...

def add_FeedServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class FeedService:
    @staticmethod
    def GetFeed(
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
    def MutateFeeds(
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
