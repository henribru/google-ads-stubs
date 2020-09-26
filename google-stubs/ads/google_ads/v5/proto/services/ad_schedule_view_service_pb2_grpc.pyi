from typing import Any, Optional

class AdScheduleViewServiceStub:
    GetAdScheduleView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdScheduleViewServiceServicer:
    def GetAdScheduleView(self, request: Any, context: Any) -> None: ...

def add_AdScheduleViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AdScheduleViewService:
    @staticmethod
    def GetAdScheduleView(
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
