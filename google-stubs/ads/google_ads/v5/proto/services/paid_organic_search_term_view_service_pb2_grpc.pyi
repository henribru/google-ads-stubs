from typing import Any, Optional

class PaidOrganicSearchTermViewServiceStub:
    GetPaidOrganicSearchTermView: Any = ...
    def __init__(self, channel: Any) -> None: ...

class PaidOrganicSearchTermViewServiceServicer:
    def GetPaidOrganicSearchTermView(self, request: Any, context: Any) -> None: ...

def add_PaidOrganicSearchTermViewServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...

class PaidOrganicSearchTermViewService:
    @staticmethod
    def GetPaidOrganicSearchTermView(
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
