from typing import Any, Optional

class MediaFileServiceStub:
    GetMediaFile: Any = ...
    MutateMediaFiles: Any = ...
    def __init__(self, channel: Any) -> None: ...

class MediaFileServiceServicer:
    def GetMediaFile(self, request: Any, context: Any) -> None: ...
    def MutateMediaFiles(self, request: Any, context: Any) -> None: ...

def add_MediaFileServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class MediaFileService:
    @staticmethod
    def GetMediaFile(
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
    def MutateMediaFiles(
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
