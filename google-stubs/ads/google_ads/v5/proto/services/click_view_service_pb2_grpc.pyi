from typing import Any, Optional

class ClickViewServiceStub:
    GetClickView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ClickViewServiceServicer:
    def GetClickView(self, request: Any, context: Any) -> None: ...

def add_ClickViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class ClickViewService:
    @staticmethod
    def GetClickView(
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
