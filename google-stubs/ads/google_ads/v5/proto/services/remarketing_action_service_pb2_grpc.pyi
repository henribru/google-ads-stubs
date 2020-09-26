from typing import Any, Optional

class RemarketingActionServiceStub:
    GetRemarketingAction: Any = ...
    MutateRemarketingActions: Any = ...
    def __init__(self, channel: Any) -> None: ...

class RemarketingActionServiceServicer:
    def GetRemarketingAction(self, request: Any, context: Any) -> None: ...
    def MutateRemarketingActions(self, request: Any, context: Any) -> None: ...

def add_RemarketingActionServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class RemarketingActionService:
    @staticmethod
    def GetRemarketingAction(
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
    def MutateRemarketingActions(
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
