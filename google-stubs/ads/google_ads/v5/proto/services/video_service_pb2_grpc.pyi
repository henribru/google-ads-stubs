from typing import Any, Optional

class VideoServiceStub:
    GetVideo: Any = ...
    def __init__(self, channel: Any) -> None: ...

class VideoServiceServicer:
    def GetVideo(self, request: Any, context: Any) -> None: ...

def add_VideoServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class VideoService:
    @staticmethod
    def GetVideo(
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
