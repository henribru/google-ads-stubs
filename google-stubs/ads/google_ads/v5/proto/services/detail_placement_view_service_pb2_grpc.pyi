from typing import Any, Optional

class DetailPlacementViewServiceStub:
    GetDetailPlacementView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DetailPlacementViewServiceServicer:
    def GetDetailPlacementView(self, request: Any, context: Any) -> None: ...

def add_DetailPlacementViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class DetailPlacementViewService:
    @staticmethod
    def GetDetailPlacementView(
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
