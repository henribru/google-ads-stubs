from typing import Any, Optional

class LocationViewServiceStub:
    GetLocationView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class LocationViewServiceServicer:
    def GetLocationView(self, request: Any, context: Any) -> None: ...

def add_LocationViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class LocationViewService:
    @staticmethod
    def GetLocationView(
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
