from typing import Any, Optional

class ConversionActionServiceStub:
    GetConversionAction: Any = ...
    MutateConversionActions: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ConversionActionServiceServicer:
    def GetConversionAction(self, request: Any, context: Any) -> None: ...
    def MutateConversionActions(self, request: Any, context: Any) -> None: ...

def add_ConversionActionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ConversionActionService:
    @staticmethod
    def GetConversionAction(
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
    def MutateConversionActions(
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
