from typing import Any, Optional

class TopicViewServiceStub:
    GetTopicView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class TopicViewServiceServicer:
    def GetTopicView(self, request: Any, context: Any) -> None: ...

def add_TopicViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class TopicViewService:
    @staticmethod
    def GetTopicView(
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
