from typing import Any, Optional

class ChangeStatusServiceStub:
    GetChangeStatus: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ChangeStatusServiceServicer:
    def GetChangeStatus(self, request: Any, context: Any) -> None: ...

def add_ChangeStatusServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class ChangeStatusService:
    @staticmethod
    def GetChangeStatus(
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
