from typing import Any, Optional

class GeographicViewServiceStub:
    GetGeographicView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class GeographicViewServiceServicer:
    def GetGeographicView(self, request: Any, context: Any) -> None: ...

def add_GeographicViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class GeographicViewService:
    @staticmethod
    def GetGeographicView(
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
