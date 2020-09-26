from typing import Any, Optional

class AdGroupCriterionServiceStub:
    GetAdGroupCriterion: Any = ...
    MutateAdGroupCriteria: Any = ...
    def __init__(self, channel: Any) -> None: ...

class AdGroupCriterionServiceServicer:
    def GetAdGroupCriterion(self, request: Any, context: Any) -> None: ...
    def MutateAdGroupCriteria(self, request: Any, context: Any) -> None: ...

def add_AdGroupCriterionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class AdGroupCriterionService:
    @staticmethod
    def GetAdGroupCriterion(
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
    def MutateAdGroupCriteria(
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
