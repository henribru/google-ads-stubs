from typing import Any, Optional

class AdParameterServiceStub:
    GetAdParameter: Any = ...
    MutateAdParameters: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdParameterServiceServicer:
    def GetAdParameter(self, request: Any, context: Any) -> None: ...
    def MutateAdParameters(self, request: Any, context: Any) -> None: ...

def add_AdParameterServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdParameterService:
    @staticmethod
    def GetAdParameter(
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
    def MutateAdParameters(
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
