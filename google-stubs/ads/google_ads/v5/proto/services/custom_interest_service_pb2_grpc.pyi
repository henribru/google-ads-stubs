from typing import Any, Optional

class CustomInterestServiceStub:
    GetCustomInterest: Any = ...
    MutateCustomInterests: Any = ...
    def __init__(self, channel: Any) -> None: ...

class CustomInterestServiceServicer:
    def GetCustomInterest(self, request: Any, context: Any) -> None: ...
    def MutateCustomInterests(self, request: Any, context: Any) -> None: ...

def add_CustomInterestServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class CustomInterestService:
    @staticmethod
    def GetCustomInterest(
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
    @staticmethod
    def MutateCustomInterests(
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
