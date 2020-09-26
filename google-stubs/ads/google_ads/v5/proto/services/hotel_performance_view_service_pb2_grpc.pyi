from typing import Any, Optional

class HotelPerformanceViewServiceStub:
    GetHotelPerformanceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class HotelPerformanceViewServiceServicer:
    def GetHotelPerformanceView(self, request: Any, context: Any) -> None: ...

def add_HotelPerformanceViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class HotelPerformanceViewService:
    @staticmethod
    def GetHotelPerformanceView(
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
