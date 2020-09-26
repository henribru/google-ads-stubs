from typing import Any, Optional

class DynamicSearchAdsSearchTermViewServiceStub:
    GetDynamicSearchAdsSearchTermView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class DynamicSearchAdsSearchTermViewServiceServicer:
    def GetDynamicSearchAdsSearchTermView(self, request: Any, context: Any) -> None: ...

def add_DynamicSearchAdsSearchTermViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class DynamicSearchAdsSearchTermViewService:
    @staticmethod
    def GetDynamicSearchAdsSearchTermView(
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
