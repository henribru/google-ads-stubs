from typing import Any, Optional

class SharedCriterionServiceStub:
    GetSharedCriterion: Any = ...
    MutateSharedCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class SharedCriterionServiceServicer:
    def GetSharedCriterion(self, request: Any, context: Any) -> None: ...
    def MutateSharedCriteria(self, request: Any, context: Any) -> None: ...

def add_SharedCriterionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class SharedCriterionService:
    @staticmethod
    def GetSharedCriterion(
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
    def MutateSharedCriteria(
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
