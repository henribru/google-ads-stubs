from typing import Any, Optional

class AgeRangeViewServiceStub:
    GetAgeRangeView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AgeRangeViewServiceServicer:
    def GetAgeRangeView(self, request: Any, context: Any) -> None: ...

def add_AgeRangeViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class AgeRangeViewService:
    @staticmethod
    def GetAgeRangeView(
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
