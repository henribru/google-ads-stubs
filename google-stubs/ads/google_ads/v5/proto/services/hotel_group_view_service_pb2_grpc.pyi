from typing import Any, Optional

class HotelGroupViewServiceStub:
    GetHotelGroupView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class HotelGroupViewServiceServicer:
    def GetHotelGroupView(self, request: Any, context: Any) -> None: ...

def add_HotelGroupViewServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class HotelGroupViewService:
    @staticmethod
    def GetHotelGroupView(
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
