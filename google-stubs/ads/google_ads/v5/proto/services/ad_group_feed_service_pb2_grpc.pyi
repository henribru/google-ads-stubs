from typing import Any, Optional

class AdGroupFeedServiceStub:
    GetAdGroupFeed: Any = ...
    MutateAdGroupFeeds: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupFeedServiceServicer:
    def GetAdGroupFeed(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupFeeds(self, request: Any, context: Any) -> None: ...

def add_AdGroupFeedServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdGroupFeedService:
    @staticmethod
    def GetAdGroupFeed(
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
    def MutateAdGroupFeeds(
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
