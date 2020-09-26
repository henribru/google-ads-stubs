from typing import Any, Optional

class ExpandedLandingPageViewServiceStub:
    GetExpandedLandingPageView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ExpandedLandingPageViewServiceServicer:
    def GetExpandedLandingPageView(self, request: Any, context: Any) -> None: ...

def add_ExpandedLandingPageViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ExpandedLandingPageViewService:
    @staticmethod
    def GetExpandedLandingPageView(
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
