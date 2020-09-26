from typing import Any, Optional

class ConversionAdjustmentUploadServiceStub:
    UploadConversionAdjustments: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ConversionAdjustmentUploadServiceServicer:
    def UploadConversionAdjustments(self, request: Any, context: Any) -> None: ...

def add_ConversionAdjustmentUploadServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ConversionAdjustmentUploadService:
    @staticmethod
    def UploadConversionAdjustments(
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
