from typing import Any, Optional

class FeedPlaceholderViewServiceStub:
    GetFeedPlaceholderView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class FeedPlaceholderViewServiceServicer:
    def GetFeedPlaceholderView(self, request: Any, context: Any) -> None: ...

def add_FeedPlaceholderViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class FeedPlaceholderViewService:
    @staticmethod
    def GetFeedPlaceholderView(
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
