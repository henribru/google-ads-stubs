from typing import Any, Optional

class ShoppingPerformanceViewServiceStub:
    GetShoppingPerformanceView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ShoppingPerformanceViewServiceServicer:
    def GetShoppingPerformanceView(self, request: Any, context: Any) -> None: ...

def add_ShoppingPerformanceViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ShoppingPerformanceViewService:
    @staticmethod
    def GetShoppingPerformanceView(
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
