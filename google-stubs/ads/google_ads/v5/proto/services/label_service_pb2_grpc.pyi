from typing import Any, Optional

class LabelServiceStub:
    GetLabel: Any = ...
    MutateLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class LabelServiceServicer:
    def GetLabel(self, request: Any, context: Any) -> None: ...
    def MutateLabels(self, request: Any, context: Any) -> None: ...

def add_LabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class LabelService:
    @staticmethod
    def GetLabel(
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
    def MutateLabels(
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
