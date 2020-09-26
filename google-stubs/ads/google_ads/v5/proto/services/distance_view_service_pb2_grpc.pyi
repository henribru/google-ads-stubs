from typing import Any, Optional

class DistanceViewServiceStub:
    GetDistanceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DistanceViewServiceServicer:
    def GetDistanceView(self, request: Any, context: Any) -> None: ...

def add_DistanceViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class DistanceViewService:
    @staticmethod
    def GetDistanceView(
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
