from typing import Any, Optional

class AdGroupAudienceViewServiceStub:
    GetAdGroupAudienceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupAudienceViewServiceServicer:
    def GetAdGroupAudienceView(self, request: Any, context: Any) -> None: ...

def add_AdGroupAudienceViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AdGroupAudienceViewService:
    @staticmethod
    def GetAdGroupAudienceView(
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
