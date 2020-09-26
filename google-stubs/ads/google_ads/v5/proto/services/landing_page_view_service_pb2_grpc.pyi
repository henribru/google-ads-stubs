from typing import Any, Optional

class LandingPageViewServiceStub:
    GetLandingPageView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class LandingPageViewServiceServicer:
    def GetLandingPageView(self, request: Any, context: Any) -> None: ...

def add_LandingPageViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class LandingPageViewService:
    @staticmethod
    def GetLandingPageView(
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
