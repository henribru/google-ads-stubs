from typing import Any, Optional

class SharedSetServiceStub:
    GetSharedSet: Any = ...
    MutateSharedSets: Any = ...
    def __init__(self, channel: Any) -> None: ...

class SharedSetServiceServicer:
    def GetSharedSet(self, request: Any, context: Any) -> None: ...
    def MutateSharedSets(self, request: Any, context: Any) -> None: ...

def add_SharedSetServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class SharedSetService:
    @staticmethod
    def GetSharedSet(
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
    def MutateSharedSets(
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
