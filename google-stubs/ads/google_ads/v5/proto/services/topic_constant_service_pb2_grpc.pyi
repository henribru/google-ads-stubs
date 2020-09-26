from typing import Any, Optional

class TopicConstantServiceStub:
    GetTopicConstant: Any = ...
    def __init__(self, channel: Any) -> None: ...

class TopicConstantServiceServicer:
    def GetTopicConstant(self, request: Any, context: Any) -> None: ...

def add_TopicConstantServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class TopicConstantService:
    @staticmethod
    def GetTopicConstant(
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
