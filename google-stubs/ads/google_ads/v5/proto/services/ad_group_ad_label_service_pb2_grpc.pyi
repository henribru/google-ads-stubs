from typing import Any, Optional

class AdGroupAdLabelServiceStub:
    GetAdGroupAdLabel: Any = ...
    MutateAdGroupAdLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupAdLabelServiceServicer:
    def GetAdGroupAdLabel(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupAdLabels(self, request: Any, context: Any) -> None: ...

def add_AdGroupAdLabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdGroupAdLabelService:
    @staticmethod
    def GetAdGroupAdLabel(
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
    def MutateAdGroupAdLabels(
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
