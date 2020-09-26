from typing import Any, Optional

class ConversionUploadServiceStub:
    UploadClickConversions: Any = ...
    UploadCallConversions: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ConversionUploadServiceServicer:
    def UploadClickConversions(self, request: Any, context: Any) -> None: ...
    def UploadCallConversions(self, request: Any, context: Any) -> None: ...

def add_ConversionUploadServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ConversionUploadService:
    @staticmethod
    def UploadClickConversions(
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
    def UploadCallConversions(
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
