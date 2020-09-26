from typing import Any, Optional

class GenderViewServiceStub:
    GetGenderView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GenderViewServiceServicer:
    def GetGenderView(self, request: Any, context: Any) -> None: ...

def add_GenderViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class GenderViewService:
    @staticmethod
    def GetGenderView(
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
