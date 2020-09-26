from typing import Any, Optional

class FeedItemTargetServiceStub:
    GetFeedItemTarget: Any = ...
    MutateFeedItemTargets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedItemTargetServiceServicer:
    def GetFeedItemTarget(self, request: Any, context: Any) -> None: ...
    def MutateFeedItemTargets(self, request: Any, context: Any) -> None: ...

def add_FeedItemTargetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class FeedItemTargetService:
    @staticmethod
    def GetFeedItemTarget(
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
    def MutateFeedItemTargets(
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
