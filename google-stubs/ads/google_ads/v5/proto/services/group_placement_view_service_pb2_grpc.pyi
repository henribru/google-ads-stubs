from typing import Any, Optional

class GroupPlacementViewServiceStub:
    GetGroupPlacementView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GroupPlacementViewServiceServicer:
    def GetGroupPlacementView(self, request: Any, context: Any) -> None: ...

def add_GroupPlacementViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class GroupPlacementViewService:
    @staticmethod
    def GetGroupPlacementView(
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
