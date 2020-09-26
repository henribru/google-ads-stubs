from typing import Any, Optional

class AdGroupLabelServiceStub:
    GetAdGroupLabel: Any = ...
    MutateAdGroupLabels: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupLabelServiceServicer:
    def GetAdGroupLabel(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupLabels(self, request: Any, context: Any) -> None: ...

def add_AdGroupLabelServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdGroupLabelService:
    @staticmethod
    def GetAdGroupLabel(
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
    def MutateAdGroupLabels(
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
