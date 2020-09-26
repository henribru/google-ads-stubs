from typing import Any, Optional

class UserLocationViewServiceStub:
    GetUserLocationView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class UserLocationViewServiceServicer:
    def GetUserLocationView(self, request: Any, context: Any) -> None: ...

def add_UserLocationViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class UserLocationViewService:
    @staticmethod
    def GetUserLocationView(
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
