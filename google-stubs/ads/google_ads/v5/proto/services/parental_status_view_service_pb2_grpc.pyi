from typing import Any, Optional

class ParentalStatusViewServiceStub:
    GetParentalStatusView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ParentalStatusViewServiceServicer:
    def GetParentalStatusView(self, request: Any, context: Any) -> None: ...

def add_ParentalStatusViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class ParentalStatusViewService:
    @staticmethod
    def GetParentalStatusView(
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
