from typing import Any, Optional

class ManagedPlacementViewServiceStub:
    GetManagedPlacementView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ManagedPlacementViewServiceServicer:
    def GetManagedPlacementView(self, request: Any, context: Any) -> None: ...

def add_ManagedPlacementViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ManagedPlacementViewService:
    @staticmethod
    def GetManagedPlacementView(
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
